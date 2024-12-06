<template>
  <div class="home">
    <div class="filters">
      <div class="filter-container">
        <div class="sort-options">
          <select v-model="currentSort" @change="handleSortChange">
            <option value="hot">热门</option>
            <option value="new">最新发布</option>
          </select>
        </div>
      </div>
    </div>
    <div class="post-list">
      <div v-for="post in posts" :key="post.post_id" class="post-item" @click="navigateToPost(post.post_id)">
        <div class="post-avatar">
          <img :src="post.avatar" :alt="post.username">
        </div>
        <div class="post-content">
          <h3 class="post-title">{{ post.post_title }}</h3>
          <div class="post-meta">
            <span class="author">{{ post.username }}</span>
            <span class="time">{{ formatTime(post.post_time) }}</span>
<!--            <span class="category">{{ post.post_heat }}</span>-->
          </div>
        </div>
        <div class="post-stats">
          <span class="reply-count">{{ post.post_heat }} 热度</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { getallpost  } from '@/services/api'
import { getpost, getreplies } from "@/views/post/PostViewContainer.vue";

const store = useStore()
const router = useRouter()

const currentSort = ref('hot')
const currentFilter = ref('all')
const currentSection = computed(() => store.state.section.currentSection)

const posts = ref([])

// 监视 currentSort 和 currentFilter 的变化，实时获取更新的帖子
const filteredPosts = async () => {
  const sortfilter = {
    sort: currentSort.value,
    filter: currentFilter.value,
    section: currentSection.value
  }
  try {
    const response = await getallpost(sortfilter)
    if (response.data.code === 1) {
      posts.value = response.data.data
    } else {
      console.error('获取帖子失败:', response.data.message)
    }
  } catch (error) {
    console.error('Error fetching posts:', error)
  }
}

// 监视排序和筛选条件的变化，获取新的数据
watch([currentSort, currentFilter, currentSection], async () => {
  console.log('change')
  await filteredPosts()
})

// 初始化时获取数据（这里会使用 init_posts 作为初始数据，避免立即请求）
onMounted(async () => {
  await filteredPosts() // 直接获取后端数据
})

const formatTime = (date) => {
  return date.toLocaleString()
}

const navigateToPost = async (postId) => {
  try {
    console.log(postId)
    const post = { post_id: postId };  // 构建 `post` 对象
    // 调用获取帖子数据的函数
    //await getpost(post);
    //await getreplies(post);
    await router.push(`/posts/${postId}`);  // 跳转到帖子页面
  } catch (error) {
    console.error('获取帖子失败:', error);
  }
};
</script>

<script>

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

.sort-options,
.filter-options {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}

.sort-options button,
.filter-options button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.sort-options button.active,
.filter-options button.active {
  background-color: var(--primary-color);
  color: white;
}


/* .sort-options, .filter-options:hover {
  border-color: black; 
} */

.post-item {
  display: flex;
  align-items: center;
  padding: 15px 5px;
  transition: background-color 0.2s, transform 0.2s;
  /* 移除了 border-bottom */
  cursor: pointer;
}

.post-item:hover {
  background-color: #f9f9f9;
  transform: scale(1.02);
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

.post-meta>* {
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

.sort-options select:hover,
.filter-options select:hover {
  background-color: var(--hover-color);
  /* 定义悬浮时的背景色 */
  border-color: var(--primary-color);
  /* 定义悬浮时的边框色 */
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
