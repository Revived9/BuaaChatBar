<script setup>
import Sidebar from '@/components/layout/Sidebar.vue'
import RightSidebar from '@/components/layout/RightSidebar.vue'
import Home from '@/views/Home.vue'
import Tags from '@/views/Tags.vue'
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'

const route = useRoute()
const store = useStore()
const isHomePage = computed(() => route.name === 'Home')
</script>

<template>
  <main class="main-content">
    <div class="main-content-inner">
      <Sidebar />
      <div class="center-content">
        <template v-if="isHomePage">
          <Home />
        </template>
        <router-view v-else>
          <Tags />
        </router-view>
      </div>
      <RightSidebar />
    </div>
  </main>
</template>

<style scoped>
.main-content {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  background-color: #ffffff;
}

.main-content-inner {
  width: 70%;
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  padding: 20px 0;
  box-sizing: border-box;
}

.center-content {
  flex-grow: 1;
  padding: 0 20px;
}

@media (max-width: 1024px) {
  .main-content-inner {
    width: 90%;
    flex-direction: column;
  }
  
  .center-content {
    padding: 20px 0;
  }
}

@media (max-width: 768px) {
  .main-content-inner {
    width: 95%;
  }
}
</style>
