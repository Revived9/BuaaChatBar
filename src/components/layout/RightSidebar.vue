<template>
  <aside class="right-sidebar">
    <div class="monthly-active">
      <h3>月活榜单</h3>
      <ul class="user-list">
        <li v-for="user in activeUsers" :key="user.id">
          <img :src="user.avatar" :alt="user.name" />
          <span>{{ user.name }}</span>
          <span class="score">{{ user.score }}</span>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'

const activeUsers = ref([
  { id: 1, name: '用户1', avatar: 'path/to/avatar1.jpg', score: 100 },
  { id: 2, name: '用户2', avatar: 'path/to/avatar2.jpg', score: 90 },
  { id: 3, name: '用户3', avatar: 'path/to/avatar3.jpg', score: 80 },
  // 添加更多用户...
])
</script>

<style scoped>
.right-sidebar {
  background-color: #fff;
  /* 移除了 border-radius 和 box-shadow */
  margin-bottom: 20px;
}

.monthly-active {
  padding: 15px;
}

.user-list {
  list-style-type: none;
  padding: 0;
}

.user-list li {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.user-list img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}

.user-list .score {
  margin-left: auto;
  font-weight: bold;
  color: var(--primary-color);
}
</style>
