import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import UserProfile from '@/views/UserProfile.vue'
import Tags from '@/views/Tags.vue'
import PostViewContainer from '@/views/post/PostViewContainer.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { keepAlive: true }
  },
  {
    path: '/posts/:id',
    name: 'PostView',
    component: PostViewContainer,
    props: true,
    meta: { keepAlive: false }
  },
  {
    path: '/user/:studentId',
    name: 'UserProfile',
    component: UserProfile,
    props: true,
    meta: { keepAlive: false }
  },
  {
    path: '/tags',
    name: 'Tags',
    component: Tags,
    meta: { keepAlive: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
