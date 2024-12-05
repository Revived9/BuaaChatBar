<template>
  <div class="user-profile">
    <ProfileHeader
      :username="username"
      :user-avatar="userAvatar"
      :user-level="userLevel"
      :registration-date="registrationDate"
      :user-bio="userBio"
      :is-current-user="isCurrentUser"
      @update-avatar="handleAvatarChange"
      @update-bio="handleBioUpdate"
    />

    <div class="profile-main">
      <ProfileList
        v-model="currentSection"
        :is-current-user="isCurrentUser"
      />
      <ProfileArea
        :current-section="currentSection"
        :posts="posts"
        :is-current-user="isCurrentUser"
        @delete-post="deletePost"
      />
    </div>
  </div>
</template>

<script setup>
import {ref, computed, onMounted, watch} from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import ProfileHeader from '@/components/profile/ProfileHeader.vue'
import ProfileList from '@/components/profile/ProfileList.vue'
import ProfileArea from '@/components/profile/ProfileArea.vue'

const route = useRoute()
const store = useStore()

const username = ref('')
const userAvatar = ref('')
const userEmail = ref('')
const registrationDate = ref('')
const birthday = ref('')
const experience = ref(0)
const userLevel = ref('')  // 用户等级
const experiencePercentage = computed(() => (experience.value / 100) * 100)  // 经验百分比
const isEditMode = ref(false)
const newUsername = ref('')
const newEmail = ref('')
const newBirthday = ref('')
const newAvatarPreview = ref('')
const cropperInstance = ref(null)  // 用来保存 Cropper.js 实例
// 用户的帖子列表
const posts = ref([])

// 新增变量
const currentTab = ref('posts')
const postsCount = ref(0)
const likesReceived = ref(0)
const favorites = ref([])

const tabs = [
  { id: 'posts', name: '发布的帖子' },
  { id: 'favorites', name: '收藏的帖子' }
]

// 判断是否为当前用户的个人页面
const isCurrentUser = computed(() => {
  //return store.state.user.studentId === route.params.studentId
  //TODO
  return true
})

// 格式化日期
const formatDate = (date) => {
  if (!date) return '未知'
  return new Date(date).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

// 使用 computed 属性获取登录状态
const isLoggedIn = computed(() => store.state.user.isLoggedIn)

// 监听 store 中的用户名变化
import { watchEffect } from 'vue';

// 监听 store 中的用户名变化
watch(
 () => store.state.user.username,
 (newUsername) => {
   console.log(store.state.user.username)
   console.log(newUsername)
  username.value = newUsername;
 }
);

onMounted(async () => {
  if (isLoggedIn.value) {
    const currentUser = store.state.user
    username.value = currentUser.username
    userAvatar.value = currentUser.avatar
    userEmail.value = currentUser.email || '未设置'
    registrationDate.value = currentUser.registrationDate || '未知'
    birthday.value = currentUser.birthday || '未知'
    experience.value = currentUser.experience || 0
    userLevel.value = getUserLevel(experience.value)
     // 获取用户的帖子列表
    try {
      const userPosts = await store.dispatch('posts/getUserPosts', currentUser.student_id)
      posts.value = userPosts
    } catch (error) {
      console.error('获取用户帖子失败:', error)
    }
  } else {
    try {
      const userInfo = await store.dispatch('user/getUserInfo', route.params.studentId)
      username.value = userInfo.username
      userAvatar.value = userInfo.avatar
      userEmail.value = userInfo.email
      registrationDate.value = new Date(userInfo.registrationDate).toLocaleDateString()
      birthday.value = userInfo.birthday || '未知'
      experience.value = userInfo.experience || 0
      userLevel.value = getUserLevel(experience.value)
      // 获取用户的帖子列表
      try {
       const userPosts = await store.dispatch('posts/getUserPosts', route.params.studentId)
       posts.value = userPosts
      } catch (error) {
        console.error('获取用户信息失败:', error)
      }
    } catch (error) {
      console.error('获取用户信息失败:', error)
    }
  }

  
})



// 根据经验值计算等级
const getUserLevel = (exp) => {
  if (exp < 20) return '新手'
  if (exp < 50) return '中级'
  if (exp < 80) return '高级'
  return '专家'
}

// 删除帖子
const deletePost = async (postId) => {
  try {
    await store.dispatch('posts/deletePost', postId)  // 调用 Vuex 的 action 删除帖子
    // 从本地的 posts 数组中移除删除的帖子
    posts.value = posts.value.filter(post => post.id !== postId)
  } catch (error) {
    console.error('删除帖子失败:', error)
  }
}

// 切换编辑模式
const toggleEditMode = () => {
  isEditMode.value = !isEditMode.value
  if (isEditMode.value) {
    newUsername.value = username.value
    newEmail.value = userEmail.value
    newBirthday.value = birthday.value
  }
}

// 保存修改
const saveChanges = async () => {
  try {
    const updatedData = {
      username: newUsername.value,
      email: newEmail.value,
      birthday: newBirthday.value,
      avatar: newAvatarPreview.value || userAvatar.value,
    }
    await store.dispatch('user/updateUserInfo', updatedData)

    username.value = newUsername.value
    userEmail.value = newEmail.value
    birthday.value = newBirthday.value
    if (newAvatarPreview.value) {
      userAvatar.value = newAvatarPreview.value
    }
    isEditMode.value = false
  } catch (error) {
    console.error('保存失败:', error)
  }
}

// 取消编辑
const cancelEdit = () => {
  isEditMode.value = false
}

// 头像上传处理
const onAvatarChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onloadend = () => {
      newAvatarPreview.value = reader.result // 获取头像文件的 Base64 编码
      // 头像裁剪初始化
      if (cropperInstance.value) {
        cropperInstance.value.destroy()  // 销毁之前的 Cropper 实例
      }
      const img = new Image()
      img.src = newAvatarPreview.value
      img.onload = () => {
        cropperInstance.value = new Cropper(img, {
          aspectRatio: 1, // 头像裁剪为正方形
          viewMode: 1,
          preview: '.avatar-preview',
        })
      }
    }
    reader.readAsDataURL(file)
  }
}

// 开始裁剪
const startCropper = () => {
  if (cropperInstance.value) {
    const canvas = cropperInstance.value.getCroppedCanvas()
    newAvatarPreview.value = canvas.toDataURL() // 获取裁剪后的头像
  }
}

// 新增变量
const currentSection = ref('posts')
const userBio = ref('')
const repliesCount = ref(0)

const mainMenuItems = [
  { id: 'replies', name: '回复', icon: 'fas fa-reply', count: 0 },
  { id: 'posts', name: '主题', icon: 'fas fa-pen', count: 0 },
  { id: 'badges', name: '徽章', icon: 'fas fa-medal', count: 0 },
  { id: 'likes', name: '赞', icon: 'fas fa-heart', count: 0 },
  { id: 'mentions', name: '被提及', icon: 'fas fa-at', count: 0 },
]

const settingsMenuItems = [
  { id: 'settings', name: '设置', icon: 'fas fa-cog' },
  { id: 'security', name: '安全', icon: 'fas fa-shield-alt' },
]

// 新增变量
const isEditingBio = ref(false)
const newBio = ref('')
const bioInput = ref(null)

// 头像点击处理
const handleAvatarClick = () => {
  // 创建一个隐藏的文件输入框
  const input = document.createElement('input')
  input.type = 'file'
  input.accept = 'image/*'
  input.onchange = (event) => onAvatarChange(event)
  input.click()
}

// 开始编辑简介
const startEditBio = () => {
  isEditingBio.value = true
  newBio.value = userBio.value
  // 等待 DOM 更新后聚焦输入框
  nextTick(() => {
    bioInput.value?.focus()
  })
}

// 保存简介
const saveBio = async () => {
  if (newBio.value !== userBio.value) {
    try {
      await store.dispatch('user/updateUserBio', newBio.value)
      userBio.value = newBio.value
    } catch (error) {
      console.error('保存简介失败:', error)
    }
  }
  isEditingBio.value = false
}
</script>

<style scoped>
.user-profile {
  min-height: calc(100vh - var(--header-height));
  background-color: var(--background-color);
}

.profile-main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 24px;
  position: relative;
}
</style>

