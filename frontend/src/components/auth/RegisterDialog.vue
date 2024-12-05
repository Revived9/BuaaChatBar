<template>
  <div class="dialog-overlay" @click="$emit('close')">
    <div class="dialog-content" @click.stop>
      <h2>注册</h2>
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <input id="studentId" v-model="form.student_id" type="text" placeholder="学号" required>
        </div>
        <div class="form-group">
          <input id="username" v-model="form.username" type="text" placeholder="用户名" required>
        </div>
        <div class="form-group">
          <input id="email" v-model="form.email" type="email" placeholder="邮箱" required>
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
        <div class="form-group agreement">
          <label>
            <input type="checkbox" v-model="form.agreeTerms" required>
            <span>我已同意<a href="#" @click.prevent="showTerms">《航吧守则》</a></span>
          </label>
        </div>
        <button type="submit" class="submit-btn" :disabled="!form.agreeTerms">注册</button>
      </form>
      <button class="close-btn" @click="$emit('close')">&times;</button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { register } from '@/services/api'

const store = useStore()
const router = useRouter()
const emit = defineEmits(['close'])

const form = reactive({
  student_id: '',
  username: '',
  email: '',
  password: '',
  agreeTerms: false
})

const showPassword = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const showTerms = () => {
  // 这里可以实现显示《航吧守则》的逻辑
  console.log('显示航吧守则')
  // 例如，可以打开一个新的对话框或导航到一个包含守则的页面
}

async function handleRegister() {
  try {
    const result = await register(form);
    const data = result.data
    if (data.code === 1) {
      // 注册成功，执行成功后的操作，如跳转到登录页面
      alert('注册成功');
      window.location.href = '/';  // 假设跳转到登录页面
    } else {
      // 根据后端返回的 message 提示用户注册失败的原因
      alert(data.message || '注册失败，请重试');
    }
  } catch (error) {
    console.error(error);
    alert(error.message);  // 显示捕获到的错误信息
  }
}


// const handleRegister = async () => {
//   if (!form.agreeTerms) {
//     console.error('请同意航吧守则')
//     return
//   }
  
//   try {
//     const response = await register(form)
//     // 假设后端返回的数据中包含 token
//     const { token } = response.data
//     localStorage.setItem('token', token)
//     await store.dispatch('user/setUser', response.data.user)
//     router.push('/')
//     emit('close')
//   } catch (error) {
//     console.error('注册失败:', error)
//     // 显示错误消息
//   }
// }
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

input[type="text"],
input[type="email"],
input[type="password"] {
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

input[type="text"]:focus,
input[type="email"]:focus,
input[type="password"]:focus {
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

.agreement {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.agreement input[type="checkbox"] {
  margin-right: 0.5rem;
}

.agreement a {
  color: var(--primary-color);
  text-decoration: none;
}

.agreement a:hover {
  text-decoration: underline;
}

.submit-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
