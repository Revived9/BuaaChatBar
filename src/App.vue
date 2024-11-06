<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import Header from '@/components/layout/Header.vue'
import WelcomeBanner from '@/components/common/WelcomeBanner.vue'
import MainContent from '@/components/layout/MainContent.vue'

const route = useRoute()
const store = useStore()

const isUserProfilePage = computed(() => route.name === 'UserProfile')
const isLoggedIn = computed(() => store.state.user.isLoggedIn)
</script>

<template>
  <div id="app">
    <Header />
    <template v-if="!isUserProfilePage">
      <WelcomeBanner />
      <MainContent />
    </template>
    <router-view v-else></router-view>
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
