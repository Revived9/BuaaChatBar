<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import Header from '@/components/layout/Header.vue'
import WelcomeBanner from '@/components/layout/WelcomeBanner.vue'
import MainContent from '@/components/layout/MainContent.vue'

const store = useStore()
const route = useRoute()
const router = useRouter()

// 计算当前页面类型
const isHomePage = computed(() => route.name === 'Home')

onMounted(async () => {
  await store.dispatch('user/initUserState')
  
  // 如果在首页并且有查询参数，更新板块
  if (route.query.section && route.path === '/') {
    await store.dispatch('section/updateCurrentSection', route.query.section)
  }
})
</script>

<template>
  <div id="app">
    <Header />
    <template v-if="isHomePage">
      <WelcomeBanner />
      <MainContent />
    </template>
    <router-view v-else />
  </div>
</template>

<style>
:root {
  --primary-color: #1E90FF; /* 更活泼的蓝色 */
  --secondary-color: #E6F3FF;
  --text-color: #333333;
  --background-color: #F0F8FF;
  --border-color: #B0D4FF;
}

body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 14px;
  line-height: 1.5;
  background-color: var(--background-color);
  color: var(--text-color);
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

a {
  color: var(--primary-color);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
