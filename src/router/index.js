import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import UserProfile from '@/views/UserProfile.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/:studentId',
    name: 'UserProfile',
    component: UserProfile
  },
  // 其他路由...
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
