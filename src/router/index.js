import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import UserProfile from '@/views/UserProfile.vue'
import CreatePost from '../views/CreatePost.vue'
import Tags from '@/views/Tags.vue'

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
  {
    path: '/create-post',  // 路由路径
    name: 'CreatePost',
    component: CreatePost  // 绑定到 CreatePost 组件
  },
  {
    path: '/tags',  // 路由路径
    name: 'Tags',
    component: Tags  // 绑定到 Tags 组件
  },
  // 其他路由...
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
