<template>
  <header class="app-header">
    <div class="header-content">
      <div class="logo" @click="goToHome">
        <img src="@/assets/logo.png" alt="航吧" class="logo-image">
      </div>
      <nav>
        <router-link to="/" class="nav-item" :class="{ active: isActive === 'all' }"
          @click="setActive('all')">全部讨论</router-link>
        <router-link to="/tags" class="nav-item" :class="{ active: isActive === 'tags' }"
          @click="setActive('tags')">标签</router-link>
      </nav>
      <div class="user-actions">
        <div class="search-container">
          <input type="text" placeholder="搜索" class="search-input" v-model="searchQuery" />
          <i class="iconfont icon-search" @click="performSearch"></i>
        </div>
        <!-- <template v-if="false"> -->
        <template v-if="!isLoggedIn">
          <button @click="showLoginDialog" class="btn btn-login">登录</button>
          <button @click="showRegisterDialog" class="btn btn-register">注册</button>
        </template>
        <div v-else class="user-info-dropdown" @click="toggleDropdown" ref="dropdownRef">
          <div class="user-info" :class="{ 'active': isDropdownOpen }">
            <img :src="userAvatar" alt="用户头像" class="user-avatar" />
            <span class="username">{{ username }}</span>
          </div>
          <div v-if="isDropdownOpen" class="dropdown-menu">
            <router-link :to="'/user/' + userStudentId" class="dropdown-item">个人主页</router-link>
            <a href="#" @click.prevent="handleLogout" class="dropdown-item">退出</a>
          </div>
        </div>
      </div>
    </div>
  </header>
  <LoginDialog v-if="isLoginDialogVisible" @close="closeLoginDialog" />
  <RegisterDialog v-if="isRegisterDialogVisible" @close="closeRegisterDialog" />
</template>

 

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import LoginDialog from '@/components/auth/LoginDialog.vue'
import RegisterDialog from '@/components/auth/RegisterDialog.vue'

const store = useStore()
const router = useRouter()

const isLoggedIn = computed(() => store.state.user.isLoggedIn)
const username = computed(() => store.state.user.username)
const userAvatar = computed(() => store.state.user.avatar)
const userStudentId = computed(() => store.state.user.studentId)

const isLoginDialogVisible = ref(false)
const isRegisterDialogVisible = ref(false)
const isDropdownOpen = ref(false)
const dropdownRef = ref(null)
const isActive = ref('all')
const searchQuery = ref('')

const showLoginDialog = () => {
  isLoginDialogVisible.value = true
}

const showRegisterDialog = () => {
  isRegisterDialogVisible.value = true
}

const closeLoginDialog = () => {
  isLoginDialogVisible.value = false
}

const closeRegisterDialog = () => {
  isRegisterDialogVisible.value = false
}

async function sendDataToBackend() {
      // 准备要发送的数据，这里简单地创建一个JSON对象
      const userData = {
        username: 'john_doe',
        email: 'john.doe@example.com'
      };
 
      // 使用Fetch API发送POST请求到后端
      const response = await fetch('http://localhost:5173/', {
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });
 
      // 解析后端返回的JSON响应
      const responseData = await response.json();
 
      // 打印后端返回的数据
      console.log(responseData);
    }

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const handleLogout = () => {
  store.dispatch('user/logout')
  router.push('/')
  isDropdownOpen.value = false
}

const handleClickOutside = (event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    isDropdownOpen.value = false
  }
}

const goToHome = () => {
  router.push('/')
}

const setActive = (item) => {
  isActive.value = item
}

const performSearch = () => {
  if (searchQuery.value.trim()) {
    console.log('搜索:', searchQuery.value)
    // 在这里实现搜索的逻辑，比如导航到搜索结果页面
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>


<style scoped>
.app-header {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  background-color: #ffffff;
}

.header-content {
  width: 70%;
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  box-sizing: border-box;
}

.logo {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.logo-image {
  height: 50px;
  width: auto;
}

nav {
  display: flex;
  gap: 15px;
}

.nav-item {
  color: var(--text-color);
  font-weight: 500;
  font-size: 0.9rem;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.nav-item:hover,
.nav-item.active {
  background-color: var(--secondary-color);
}

.user-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-container {
  position: relative;
}

.search-input {
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.9rem;
}

.search-input:hover {
  border-color: var(--primary-color); /* 定义悬浮时的边框色 */
}

.icon-search {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  width: 20px;
  height: 20px;
  color: #888;
  /* 设置图标颜色为灰色 */
}

.btn {
  padding: 5px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.btn-login {
  background-color: var(--secondary-color);
  color: var(--primary-color);
}

.btn-register {
  background-color: var(--primary-color);
  color: #fff;
}

.btn-login:hover,
.btn-register:hover {
  background-color: blue; /* 自定义悬浮时的颜色 */
  color: white; /* 鼠标悬浮时文本颜色 */
}

.user-info-dropdown {
  position: relative;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 3px 10px 3px 3px;
  border-radius: 20px;
  background-color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.user-info:hover,
.user-info.active {
  background-color: var(--primary-color);
}

.user-info:hover .username,
.user-info.active .username {
  color: white;
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.username {
  font-weight: 500;
  color: var(--text-color);
  transition: color 0.3s;
  font-size: 0.9rem;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 10px 0;
  z-index: 1000;
}

.dropdown-item {
  display: block;
  padding: 10px 20px;
  color: var(--text-color);
  text-decoration: none;
  transition: background-color 0.3s;
}

.dropdown-item:hover {
  background-color: var(--secondary-color);
}

@media (max-width: 1024px) {
  .header-content {
    width: 90%;
  }
}

@media (max-width: 768px) {
  .header-content {
    width: 95%;
    flex-direction: column;
    gap: 10px;
  }

  nav,
  .user-actions {
    width: 100%;
    justify-content: center;
  }
}
</style>
