<template>
  <div class="user-profile">
    <div class="profile-content">
      <div class="profile-header">
        <img :src="userAvatar" alt="用户头像" class="profile-avatar">
        <h1>{{ username }}</h1>
        <p>学号: {{ $route.params.studentId }}</p>
      </div>
      <div class="profile-details">
        <h2>个人信息</h2>
        <p>邮箱: {{ userEmail }}</p>
        <p>注册时间: {{ registrationDate }}</p>
      </div>
      <div class="user-posts">
        <h2>最近的帖子</h2>
        <!-- 这里可以添加用户最近发布的帖子列表 -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'

const route = useRoute()
const store = useStore()

const username = ref('')
const userAvatar = ref('')
const userEmail = ref('')
const registrationDate = ref('')

// 使用 computed 属性获取登录状态
const isLoggedIn = computed(() => store.state.user.isLoggedIn)

onMounted(async () => {
  if (isLoggedIn.value) {
    // 如果用户已登录，直接从 store 中获取用户信息
    const currentUser = store.state.user
    username.value = currentUser.username
    userAvatar.value = currentUser.avatar
    userEmail.value = currentUser.email || '未设置'
    registrationDate.value = currentUser.registrationDate || '未知'
  } else {
    try {
      const userInfo = await store.dispatch('user/getUserInfo', route.params.studentId)
      username.value = userInfo.username
      userAvatar.value = userInfo.avatar
      userEmail.value = userInfo.email
      registrationDate.value = new Date(userInfo.registrationDate).toLocaleDateString()
    } catch (error) {
      console.error('获取用户信息失败:', error)
    }
  }
})
</script>

<style scoped>
.user-profile {
  background-color: var(--background-color);
  min-height: 100vh;
  padding: 20px;
}

.profile-content {
  max-width: 800px;
  margin: 0 auto;
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-header {
  text-align: center;
  margin-bottom: 30px;
}

.profile-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 15px;
}

.profile-details, .user-posts {
  margin-bottom: 20px;
}

h1, h2 {
  color: var(--primary-color);
}

p {
  margin-bottom: 10px;
}
</style>
