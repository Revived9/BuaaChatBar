<template>
  <aside class="right-sidebar">
    <div class="monthly-active">
      <h3>经验榜单</h3>
      <ul class="user-list">
        <li v-for="user in activeUsers" :key="user.id">
          <img :src="user.avatar" :alt="user.username" />
          <div class="user-info">
            <span class="username">{{ user.username }}</span>
            <div class="experience-info">
              <i class="mdi mdi-chat"></i>
              <span>{{ user.experience }}</span>
            </div>
          </div>
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
  margin-bottom: 20px;
}

.monthly-active {
  padding: 0;
}

.monthly-active h3 {
  color: var(--primary-color);
  margin-bottom: 10px;
  padding: 0 15px;
}

.user-list {
  list-style-type: none;
  padding: 15px;
  background-color: #e4edf6;
  border-radius: 4px;
  height: fit-content;
}

.user-list li {
  display: flex;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}

.user-list li:last-child {
  border-bottom: none;
}

.user-list img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 12px;
}

.user-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.username {
  font-weight: 500;
  color: #333;
  font-size: 1.1em;
}

.experience-info {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #666;
  font-size: 0.9em;
}

.experience-info i {
  font-size: 1.1em;
  color: #666;
}
</style>
