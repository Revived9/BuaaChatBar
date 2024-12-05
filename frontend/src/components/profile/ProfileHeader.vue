<template>
  <div class="profile-header">
    <div class="header-content">
      <div class="user-basic">
        <!-- 头像部分 -->
        <div 
          class="avatar-wrapper"
          @click="isCurrentUser && handleAvatarClick()"
          :class="{ 'clickable': isCurrentUser }"
        >
          <img :src="userAvatar" alt="用户头像" class="user-avatar" />
          <div v-if="isCurrentUser" class="avatar-hover-mask">
            <i class="fas fa-camera"></i>
            <span>更换头像</span>
          </div>
        </div>

        <!-- 用户信息部分 -->
        <div class="user-info">
          <div class="name-wrapper">
            <h1>{{ username }}</h1>
            <span class="user-level">LV.{{ userLevel }}</span>
          </div>
          <p class="registration-date">
            <i class="fas fa-clock"></i> {{ formatDate(registrationDate) }} 加入
          </p>
          <!-- 个人简介部分 -->
          <div class="bio-wrapper">
            <p 
              v-if="!isEditingBio" 
              class="bio" 
              @click="isCurrentUser && startEditBio()"
              :class="{ 'clickable': isCurrentUser }"
            >
              {{ userBio || '这个人很懒，还没有写简介' }}
              <i v-if="isCurrentUser" class="fas fa-edit bio-edit-icon"></i>
            </p>
            <div v-else class="bio-edit">
              <input 
                type="text" 
                v-model="editingBio" 
                @keyup.enter="saveBio"
                @blur="saveBio"
                ref="bioInput"
                maxlength="50"
                placeholder="写一句简介吧..."
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, nextTick, watch, computed} from 'vue'
import {useStore} from "vuex";

const store = useStore()

const props = defineProps({
  username: {
    type: String,
    required: true
  },
  userAvatar: {
    type: String,
    required: true
  },
  userLevel: {
    type: String,
    required: true
  },
  registrationDate: {
    type: String,
    required: true
  },
  userBio: {
    type: String,
    default: ''
  },
  isCurrentUser: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update-avatar', 'update-bio'])

// 编辑简介相关
const isEditingBio = ref(false)
const editingBio = ref(props.userBio)
const bioInput = ref(null)
const userAvatar = computed(() => store.state.user.avatar)

// 格式化日期
const formatDate = (date) => {
  if (!date) return '未知'
  return new Date(date).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// 处理头像点击
const handleAvatarClick = () => {
  const input = document.createElement('input')
  input.type = 'file'
  input.accept = 'image/*'
  input.onchange = async (event) => {
    const file = event.target.files?.[0]
    if (file) {
      // 使用 FormData 发送文件
      const response = avatermodify(file)
      const date = response.date
      // 如果上传成功，处理后端响应
      if (date.code === 1) {
        alert('修改成功')
        emit('update-avatar', file)
      } else {
        alert(data.message || '上传失败，请重试');
      }
    }    
  }
  input.click()
}

// 开始编辑简介
const startEditBio = () => {
  isEditingBio.value = true
  editingBio.value = props.userBio
  nextTick(() => {
    bioInput.value?.focus()
  })
}

/*
// 保存简介
const saveBio = () => {
  if (editingBio.value !== props.userBio) {
    emit('update-bio', editingBio.value)
  }
  isEditingBio.value = false
}
  */

// 保存简介
const saveBio = () => {
  if (editingBio.value !== props.userBio) {
    const bio = editingBio.value
    const response = biomodify(bio)
    const data = response.data
    // 请求成功，处理返回的结果
      if (data.code === 1) {
        alert('修改成功')
        emit('update-bio', editingBio.value)
      } else {
        console.error('保存失败:', response.message);
      }
  }
  isEditingBio.value = false
}
</script>

<style scoped>
.profile-header {
  background-color: var(--primary-color);
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 40px 0;
  color: white;
  margin-bottom: 60px;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.user-basic {
  display: flex;
  align-items: center;
  gap: 24px;
}

.avatar-wrapper {
  position: relative;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar-wrapper.clickable {
  cursor: pointer;
}

.user-avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-hover-mask {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.avatar-wrapper.clickable:hover .avatar-hover-mask {
  opacity: 1;
}

.user-info {
  flex-grow: 1;
}

.name-wrapper {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.name-wrapper h1 {
  margin: 0;
  font-size: 24px;
  font-weight: 600;
}

.user-level {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 14px;
}

.registration-date {
  opacity: 0.8;
  font-size: 14px;
  margin: 4px 0;
}

.bio-wrapper {
  margin-top: 12px;
}

.bio {
  opacity: 0.9;
  font-size: 16px;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.bio.clickable {
  cursor: pointer;
}

.bio-edit-icon {
  opacity: 0;
  transition: opacity 0.3s;
}

.bio.clickable:hover .bio-edit-icon {
  opacity: 1;
}

.bio-edit input {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  color: white;
  width: 100%;
  max-width: 400px;
  font-size: 16px;
}

.bio-edit input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.bio-edit input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.2);
}
</style> 