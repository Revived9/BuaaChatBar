<template>
  <div class="dialog-overlay" @click="$emit('close')">
    <div class="dialog-content" @click.stop>
      <h2>登录</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <input id="studentId" v-model="form.student_id" type="text" placeholder="学号" required>
        </div>
        <div class="form-group password-input">
          <input 
            id="password" 
            v-model="form.password" 
            :type="showPassword ? 'text' : 'password'" 
            placeholder="密码" 
            required
          >
          <button type="button" class="toggle-password" @click="togglePassword">
            <i :class="showPassword ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
          </button>
        </div>
        <div class="form-options">
          <label class="remember-me">
            <input type="checkbox" v-model="form.rememberMe">
            <span>记住密码</span>
          </label>
          <a href="#" class="forgot-password" @click.prevent="handleForgotPassword">忘记密码？</a>
        </div>
        <button type="submit" class="submit-btn">登录</button>
      </form>
      <div v-if="loginError" class="error-message">{{ loginError }}</div>
      <button class="close-btn" @click="$emit('close')">&times;</button>
    </div>
  </div>
  <SuccessDialog 
    v-if="showSuccessDialog" 
    message="登录成功" 
    @close="handleSuccessDialogClose"
  />
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { login } from '@/services/api'
import SuccessDialog from '@/components/common/SuccessDialog.vue'

const store = useStore()
const router = useRouter()
const emit = defineEmits(['close'])

const form = reactive({
  student_id: '',
  password: '',
  rememberMe: false
})

const showPassword = ref(false)
const loginError = ref('')
const showSuccessDialog = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

// 这里存储了登录的信息，请不要修改，会导致刷新后丢失登录状态
const handleLogin = async () => {
  try {
    loginError.value = ''
    const response = await login(form)
    const data = response.data
    
    if (data.code === 1) {
      localStorage.setItem('token', data.token)
      const userInfo = {
        username: data.username,
        avatar: data.path,
        studentId: form.student_id,
        bio: data.bio
      }
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
      await store.dispatch('user/setLoginStatus', true)
      await store.dispatch('user/setCurrentUser', userInfo)
      showSuccessDialog.value = true
    } else {
      alert(data.message || '登录失败，请重试');
    }
  } catch (error) {
    console.error('登录失败:', error)
    loginError.value = error.message || '登录失败，请重试'
  }
}

const handleSuccessDialogClose = () => {
  showSuccessDialog.value = false
  emit('close')
  router.push('/')
}

const handleForgotPassword = () => {
  console.log('忘记密码')
  // 这里可以实现忘记密码的逻辑
}
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex; 
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  width: 350px;
  max-width: 90%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: var(--primary-color);
  font-size: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

input[type="email"],
input[type="password"],
input[type="text"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  height: 38px;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.3s;
}

input[type="email"]:focus,
input[type="password"]:focus,
input[type="text"]:focus {
  border-color: var(--primary-color);
}

.password-input {
  position: relative;
}

.password-input input {
  padding-right: 40px;
}

.toggle-password {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--primary-color);
  cursor: pointer;
  font-size: 1rem;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.remember-me {
  display: flex;
  align-items: center;
}

.remember-me input {
  margin-right: 0.5rem;
}

.forgot-password {
  color: var(--primary-color);
  text-decoration: none;
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #1a7ee6;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #999;
}

.error-message {
  color: red;
  margin-bottom: 1rem;
  text-align: center;
}
</style>
