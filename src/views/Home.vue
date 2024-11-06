<template>
  <div class="home">
    <div class="filters">
      <div class="filter-container">
        <div class="sort-options">
          <select v-model="currentSort" @change="handleSortChange">
            <option value="latest">最新回复</option>
            <option value="hot">热门</option>
            <option value="new">最新发布</option>
          </select>
        </div>
        <div class="filter-options">
          <select v-model="currentFilter" @change="handleFilterChange">
            <option value="all">全部问题</option>
            <option value="unsolved">待解决问题</option>
            <option value="solved">已解决问题</option>
          </select>
        </div>
      </div>
    </div>
    <div class="post-list">
      <div v-for="post in filteredPosts" :key="post.id" class="post-item">
        <div class="post-avatar">
          <img :src="post.author.avatar" :alt="post.author.name">
        </div>
        <div class="post-content">
          <h3 class="post-title">{{ post.title }}</h3>
          <div class="post-meta">
            <span class="author">{{ post.author.name }}</span>
            <span class="time">{{ formatTime(post.lastReplyTime) }}</span>
            <span class="category">{{ post.category }}</span>
          </div>
        </div>
        <div class="post-stats">
          <span class="reply-count">{{ post.replyCount }} 回复</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import RightSidebar from '@/components/layout/RightSidebar.vue'

const store = useStore()
const currentSort = ref('latest')
const currentFilter = ref('all')

const posts = ref([
  {
    id: 1,
    title: "Vue 3 组件通信最佳实践",
    author: { name: "张三", avatar: "/avatars/zhangsan.jpg" },
    lastReplyTime: new Date("2023-05-10T10:30:00"),
    category: "前端开发",
    replyCount: 15,
    solved: true
  },
  {
    id: 2,
    title: "如何优化 Webpack 构建速度？",
    author: { name: "李四", avatar: "/avatars/lisi.jpg" },
    lastReplyTime: new Date("2023-05-09T16:45:00"),
    category: "工程化",
    replyCount: 8,
    solved: false
  },
  // 添加更多帖子...
])

const handleSortChange = () => {
  // 这里应该调用 API 来获取排序后的帖子
  console.log('Sort changed to:', currentSort.value)
}

const handleFilterChange = () => {
  // 这里应该调用 API 来获取筛选后的帖子
  console.log('Filter changed to:', currentFilter.value)
}

const filteredPosts = computed(() => {
  // 这里应该根据 currentSort 和 currentFilter 来过滤和排序帖子
  // 现在只是简单地返回所有帖子
  return posts.value
})

const formatTime = (date) => {
  // 这里可以使用一个日期格式化库，如 date-fns
  return date.toLocaleString()
}
</script>

<style scoped>
.home {
  width: 100%;
}

.content-wrapper {
  width: 100%;
  display: flex;
}

.main-content {
  background-color: #fff;
  /* 移除了 border-radius 和 box-shadow */
  padding: 0px;
  flex-grow: 1;
}

.sort-options, .filter-options {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}

.sort-options button, .filter-options button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.sort-options button.active, .filter-options button.active {
  background-color: var(--primary-color);
  color: white;
}


.post-item {
  display: flex;
  align-items: center;
  padding: 15px 0;
  /* 移除了 border-bottom */
}

.post-avatar img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 15px;
}

.post-content {
  flex-grow: 1;
}

.post-title {
  font-size: 1.1rem;
  margin: 0 0 5px 0;
}

.post-meta {
  font-size: 0.9rem;
  color: #666;
}

.post-meta > * {
  margin-right: 10px;
}

.post-stats {
  font-size: 0.9rem;
  color: #666;
}

@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
  }
}

.sort-options select {
  padding: 5px 10px;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background-color: white;
  font-size: 0.9rem;
  color: var(--text-color);
  cursor: pointer;
}

.sort-options select:focus {
  outline: none;
  border-color: var(--primary-color);
}

.filter-container {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
}

.sort-options,
.filter-options {
  position: relative;
  width: 150px;
}

.sort-options select,
.filter-options select {
  width: 100%;
  height: 40px;
  padding: 5px 10px;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background-color: white;
  font-size: 0.9rem;
  color: var(--text-color);
  cursor: pointer;
}

.sort-options select:focus,
.filter-options select:focus {
  outline: none;
  border-color: var(--primary-color);
}

/* 自定义下拉列表选项样式 */
.sort-options select option,
.filter-options select option {
  padding: 10px;
  background-color: white;
  color: var(--text-color);
}

/* 使用 ::-ms-expand 来隐藏 IE 中的下拉箭头 */
.sort-options select::-ms-expand,
.filter-options select::-ms-expand {
  display: none;
}

/* 使用 ::selection 来自定义选中时的背景色 */
.sort-options select option::selection,
.filter-options select option::selection {
  background-color: var(--primary-color);
  color: white;
}

/* 使用 :checked 伪类来自定义选中项的样式 */
.sort-options select option:checked,
.filter-options select option:checked {
  background-color: var(--secondary-color);
  color: var(--primary-color);
}

/* 其他样式保持不变 */
</style>
