<template>
  <div class="register">
    <h2>用户注册</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="studentId">学号</label>
        <input 
          id="studentId" 
          v-model="form.studentId" 
          type="text" 
          required
        >
      </div>
      <div class="form-group">
        <label for="username">用户名</label>
        <input 
          id="username" 
          v-model="form.username" 
          type="text" 
          required
        >
      </div>
      <div class="form-group">
        <label for="email">邮箱</label>
        <input 
          id="email" 
          v-model="form.email" 
          type="email" 
          required
        >
      </div>
      <div class="form-group">
        <label for="password">密码</label>
        <input 
          id="password" 
          v-model="form.password" 
          type="password" 
          required
        >
      </div>
      <button type="submit">注册</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

const form = reactive({
  studentId: '',
  username: '',
  email: '',
  password: ''
})

const handleRegister = async () => {
  try {
    await store.dispatch('user/register', form)
    router.push('/login')
  } catch (error) {
    console.error('注册失败:', error)
    // 显示错误消息
  }
}
</script>

<style scoped>
.register {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}

/* 添加更多样式... */
</style>
