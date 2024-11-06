<template>
  <header class="app-header">
    <div class="header-content">
      <div class="logo" @click="goToHome">
        <img src="@/assets/logo.svg" alt="航吧" class="logo-image">
      </div>
      <nav>
        <router-link to="/" class="nav-item">全部讨论</router-link>
        <router-link to="/tags" class="nav-item">标签</router-link>
      </nav>
      <div class="user-actions">
        <input type="text" placeholder="搜索" class="search-input" />
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

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const handleLogout = () => {
  store.dispatch('logout')
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

.nav-item:hover, .nav-item.router-link-active {
  background-color: var(--secondary-color);
}

.user-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-input {
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.9rem;
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

.user-info-dropdown {
  position: relative;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 6px; /* 减小头像和昵称之间的间隙 */
  padding: 3px 10px 3px 3px; /* 减小左侧内边距，保持右侧内边距 */
  border-radius: 20px;
  background-color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.user-info:hover, .user-info.active {
  background-color: var(--primary-color);
}

.user-info:hover .username, .user-info.active .username {
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
  font-size: 0.9rem; /* 可以稍微减小字体大小以适应更紧凑的布局 */
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
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

  nav, .user-actions {
    width: 100%;
    justify-content: center;
  }
}
</style>
