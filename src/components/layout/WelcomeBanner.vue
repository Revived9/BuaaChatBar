<template>
  <div class="welcome-banner" :style="{ backgroundColor: themeColor }">
    <h1>{{ welcomeMessage }}</h1>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const themeColor = computed(() => store.state.theme.themeColor)
const welcomeMessage = computed(() => store.state.theme.welcomeMessage)
</script>

<style scoped>
.welcome-banner {
  padding: 40px 20px;
  text-align: center;
  color: white;
  transition: background-color 0.3s;
}

.welcome-banner h1 {
  margin: 0;
  font-size: 2rem;
  font-weight: 500;
}
</style> 