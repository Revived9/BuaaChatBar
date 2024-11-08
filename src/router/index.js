import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import UserProfile from '@/views/UserProfile.vue'
import Tags from '@/views/Tags.vue'
import PostViewContainer from '@/views/post/PostViewContainer.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/posts/:id',
    name: 'PostView',
    component: PostViewContainer
  },
  {
    path: '/user/:studentId',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/tags',
    name: 'Tags',
    component: Tags
  }
  // 其他路由...
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
