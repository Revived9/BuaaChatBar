<template>
  <div class="profile-area">
    <!-- 回复列表 -->
    <div v-if="currentSection === 'replies'" class="section-content">
      <h2>我的回复</h2>
      <!-- 回复列表内容 -->
    </div>

    <!-- 主题列表 -->
    <div v-if="currentSection === 'posts'" class="section-content">
      <h2>我的主题</h2>
      <div v-if="posts.length > 0" class="posts-list">
        <div v-for="post in posts" :key="post.post_id" class="post-item">
          <div class="post-main">
            <h3 class="post-title">{{ post.post_title }}</h3>
            <div class="post-meta">
              <span>{{ formatDate(post.post_time) }}</span>
<!--              <span><i class="fal fa-clock" /> {{ formatDate(post.post_time) }}</span>-->
<!--              <span><i class="far fa-comment"></i> {{ post.replyCount }}回复</span>-->
<!--              <span><i class="far fa-heart"></i> {{ post.likeCount }}点赞</span>-->
            </div>
          </div>
          <div v-if="isCurrentUser" class="post-actions">
            <button @click="handleDeletePost(post.post_id)" class="delete-btn">
<!--              <i class="fas fa-trash"></i>-->
              删除
            </button>
          </div>
        </div>
      </div>
      <div v-else class="empty-state">
        暂无发布的主题
      </div>
    </div>

    <!-- 设置页面 -->
    <div v-if="currentSection === 'settings'" class="section-content">
      <h2>设置</h2>
      <div class="settings-container">
        <!-- 隐私设置 -->
        <div class="settings-section">
          <h3>隐私设置</h3>
          <div class="setting-item">
            <div class="setting-info">
              <span class="setting-title">公开在线状态</span>
              <span class="setting-desc">其他用户可以看到你是否在线</span>
            </div>
            <label class="switch">
              <input 
                type="checkbox" 
                v-model="settings.showOnlineStatus"
                @change="updateSetting('showOnlineStatus')"
              >
              <span class="slider"></span>
            </label>
          </div>
        </div>

        <!-- 通知设置 -->
        <div class="settings-section">
          <h3>通知设置</h3>
          <div class="setting-item">
            <div class="setting-info">
              <span class="setting-title">自动关注回复的主题</span>
              <span class="setting-desc">当你回复一个主题时自动关注该主题</span>
            </div>
            <label class="switch">
              <input 
                type="checkbox" 
                v-model="settings.autoFollowReplied"
                @change="updateSetting('autoFollowReplied')"
              >
              <span class="slider"></span>
            </label>
          </div>
          <div class="setting-item">
            <div class="setting-info">
              <span class="setting-title">新帖通知</span>
              <span class="setting-desc">有新的帖子时接收通知</span>
            </div>
            <label class="switch">
              <input 
                type="checkbox" 
                v-model="settings.notifyNewPosts"
                @change="updateSetting('notifyNewPosts')"
              >
              <span class="slider"></span>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- 安全设置页面 -->
    <div v-if="currentSection === 'security'" class="section-content">
      <h2>安全设置</h2>
      <div class="settings-container">
        <!-- 修改密码 -->
        <div class="settings-section">
          <h3>修改密码</h3>
          <div class="form-group">
            <label>当前密码</label>
            <input 
              type="password" 
              v-model="securityForm.old_password"
              placeholder="请输入当前密码"
            >
          </div>
          <div class="form-group">
            <label>新密码</label>
            <input 
              type="password" 
              v-model="securityForm.new_password"
              placeholder="请输入新密码"
            >
            <p class="input-tip">密码长度至少8位，包含字母和数字</p>
          </div>
          <div class="form-group">
            <label>确认新密码</label>
            <input 
              type="password" 
              v-model="securityForm.confirmPassword"
              placeholder="请再次输入新密码"
            >
          </div>
          <div class="form-actions">
            <button 
              class="primary-btn" 
              @click="updatePassword"
              :disabled="!canUpdatePassword"
            >
              更新密码
            </button>
          </div>
        </div>

        <!-- 修改邮箱 -->
        <div class="settings-section">
          <h3>修改邮箱</h3>
          <div class="form-group">
            <label>当前邮箱</label>
            <input 
              type="text" 
              :value="currentEmail"
              disabled
              class="disabled-input"
            >
          </div>
          <div class="form-group">
            <label>新邮箱</label>
            <input 
              type="email" 
              v-model="securityForm.newEmail"
              placeholder="请输入新邮箱"
            >
          </div>
          <div class="form-actions">
            <button 
              class="primary-btn" 
              @click="updateEmail"
              :disabled="!canUpdateEmail"
            >
              更新邮箱
            </button>
          </div>
        </div>

        <!-- 修改昵称 -->
        <div class="settings-section">
          <h3>修改昵称</h3>
          <div class="form-group">
            <label>当前昵称</label>
            <input 
              type="text" 
              :value="currentUsername"
              disabled
              class="disabled-input"
            >
          </div>
          <div class="form-group">
            <label>新昵称</label>
            <input 
              type="text" 
              v-model="securityForm.newUsername"
              placeholder="请输入新昵称"
            >
            <p class="input-tip">2-15个字符，可以是��文、字母、数字</p>
          </div>
          <div class="form-actions">
            <button 
              class="primary-btn" 
              @click="updateUsername"
              :disabled="!canUpdateUsername"
            >
              更新昵称
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import {passwordmodify, emailmodify, usernamemodify, deletepost} from "@/services/api.js";

const store = useStore()

const props = defineProps({
  currentSection: {
    type: String,
    required: true
  },
  posts: {
    type: Array,
    default: () => []
  },
  isCurrentUser: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['deletePost'])

// 用户设置
const settings = ref({
  showOnlineStatus: false,
  autoFollowReplied: false,
  notifyNewPosts: false
})

// 安全设置表单
const securityForm = ref({
  user_id: store.state.user.studentId,
  old_password: '',
  new_password: '',
  confirmPassword: '',
  newEmail: '',
  newUsername: ''
})

// 从 store 获取当前用户信息
const currentEmail = computed(() => store.state.user.email)
const currentUsername = computed(() => store.state.user.username)

// ��单验证
const canUpdatePassword = computed(() => {
  const { old_password, new_password, confirmPassword } = securityForm.value
  return old_password &&
         new_password &&
         confirmPassword && 
         new_password === confirmPassword &&
         new_password.length >= 8 &&
         /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(new_password)
})

const canUpdateEmail = computed(() => {
  const { newEmail } = securityForm.value
  return newEmail && 
         /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(newEmail) &&
         newEmail !== currentEmail.value
})

const canUpdateUsername = computed(() => {
  const { newUsername } = securityForm.value
  return newUsername && 
         newUsername.length >= 2 && 
         newUsername.length <= 15 &&
         newUsername !== currentUsername.value
})

// 获取用户设置
onMounted(async () => {
  try {
    const userSettings = await store.dispatch('user/getUserSettings')
    settings.value = {
      ...settings.value,
      ...userSettings
    }
  } catch (error) {
    console.error('获取用户设置失败:', error)
  }
})

// 更新设置
const updateSetting = async (key) => {
  try {
    await store.dispatch('user/updateUserSettings', {
      [key]: settings.value[key]
    })
  } catch (error) {
    console.error('更新设置失败:', error)
    // 如果更新失败，恢复原值
    settings.value[key] = !settings.value[key]
  }
}

const handleDeletePost = async (postId) => {
  const delpost = {
    user_id: store.state.user.studentId,
    post_id: postId
  }
  try {
    console.log(postId)
  const result = await deletepost(delpost);
  const data = result.data
  //emit('deletePost', postId)
    if (data.code === 1) {
      alert('删除成功')
    } else {
      console.error('删除失败:', data.message)
      alert(data.message || '删除失败')
    }
  } catch (error) {
    console.error(error);
    alert(error.message);  // 显示捕获到的错误信息
  }

}

const formatDate = (date) => {
  if (!date) return '未知'
  return new Date(date).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}


async function updatePassword() {
  try {
    console.log(store.state.user.studentId)
    const result = await passwordmodify(securityForm.value);
    const data = result.data
    if (data.code === 1) {
    // 清空表单
      securityForm.value.old_password = ''
      securityForm.value.new_password = ''
      securityForm.value.confirm_password = ''
      // 显示成功提示
      alert('密码修改成功')
    } else {
      console.error('更新密码失败:', data.message)
      alert(data.message || '密码修改失败')
    }
  } catch (error) {
    console.error(error);
    alert(error.message);  // 显示捕获到的错误信息
  }
}

async function updateEmail() {
  try {
    const result = await emailmodify(securityForm.value);
    const data = result.data
    if (data.code === 1) {
      // 清空表单
      securityForm.value.newEmail = ''
      // 显示成功提示
      alert('邮箱修改成功')
    } else {
      console.error('更新邮箱失败:', error)
      alert(error.message || '邮箱修改失败')
    }
  } catch (error) {
    console.error(error);
    alert(error.message);  // 显示捕获到的错误信息
  }
}


async function updateUsername() {
  try {
    const result = await usernamemodify(securityForm.value);
    const data = result.data
    if (data.code === 1) {
      // 更新 Vuex store 中的用户名
      await store.dispatch('user/updateUsername', securityForm.value.newUsername)
      // 清空表单
      securityForm.value.newUsername = ''
      // 显示成功提示
      alert('昵称修改成功')
    } else {
      console.error('更新昵称失败:', error)
      alert(error.message || '昵称修改失败')
    }
  } catch (error) {
    console.error(error);
    alert(error.message);
  }
}
</script>

<style scoped>
.profile-area {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  min-height: 600px;
}

.posts-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.post-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.post-meta {
  display: flex;
  gap: 16px;
  color: #666;
  font-size: 0.9rem;
}

.empty-state {
  text-align: center;
  color: #666;
  padding: 32px;
}

.delete-btn {
  color: #ff4d4f;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 8px;
}

.delete-btn:hover {
  background-color: #fff1f0;
  border-radius: 4px;
}

/* 设置页面样式 */
.settings-container {
  max-width: 800px;
}

.settings-section {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 24px;
}

.settings-section h3 {
  color: var(--text-color);
  font-size: 18px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #eee;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid #f5f5f5;
}

.setting-item:last-child {
  border-bottom: none;
}

.setting-info {
  flex-grow: 1;
  padding-right: 24px;
}

.setting-title {
  display: block;
  font-weight: 500;
  margin-bottom: 4px;
}

.setting-desc {
  font-size: 14px;
  color: #666;
}

/* 开关样式 */
.switch {
  position: relative;
  display: inline-block;
  width: 48px;
  height: 24px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 24px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: var(--primary-color);
}

input:checked + .slider:before {
  transform: translateX(24px);
}

input:focus + .slider {
  box-shadow: 0 0 1px var(--primary-color);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #333;
}

.form-group input {
  width: 100%;
  max-width: 400px;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-group input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px var(--secondary-color);
}

.disabled-input {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.input-tip {
  margin-top: 4px;
  font-size: 12px;
  color: #666;
}

.form-actions {
  margin-top: 24px;
}

.primary-btn {
  padding: 8px 24px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.primary-btn:hover {
  background-color: var(--primary-color-dark);
}

.primary-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style> 