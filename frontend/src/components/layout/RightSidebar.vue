<template>
  <aside class="right-sidebar">
    <div class="monthly-active">
      <h3>经验榜单</h3>
      <ul class="user-list">
        <li v-for="user in activeUsers" :key="user.id">
          <img :src="user.avatar" :alt="user.username" />
          <span>{{ user.username }}</span>
          <span class="score">{{ user.experience }}</span>
        </li>
      </ul>
    </div>
  </aside>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import {fetchUsers} from "@/services/api.js";

const activeUsers = ref([])

// 页面加载时调用 fetchUsers
onMounted(async () => {
  const response = await fetchUsers()
  activeUsers.value = response.data.data  // 假设返回的数据是一个数组
  console.log(activeUsers.value)
})

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

.monthly-active h3{
  color: var(--primary-color);
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
