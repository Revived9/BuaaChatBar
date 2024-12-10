<template>
  <div class="home">
    <div class="filters">
      <div class="filter-container">
        <div class="sort-options">
          <el-select
            v-model="currentSort"
            @change="handleSortChange"
            class="sort-select"
            size="large"
          >
            <el-option 
              value="hot"
              label="热门"
            >
              <span class="option-label">
                <i class="mdi mdi-fire"></i>
                热门
              </span>
            </el-option>
            <el-option 
              value="new"
              label="最新发布"
            >
              <span class="option-label">
                <i class="mdi mdi-clock-outline"></i>
                最新发布
              </span>
            </el-option>
          </el-select>
        </div>
<!--        <div class="search-container">-->
<!--          <input type="text" placeholder="搜索" class="search-input" v-model="searchQuery" />-->
<!--          <i class="iconfont icon-search" @click="performSearch"></i>-->
<!--        </div>-->
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
            <span class="author">
              <i class="mdi mdi-account"></i>
              <span>{{ post.username }}</span>
            </span>
            <span class="time">
              <i class="mdi mdi-clock-outline"></i>
              <span>{{ formatTime(post.post_time) }}</span>
            </span>
          </div>
        </div>
        <div class="post-stats">
          <span class="reply-count">
            <i class="mdi mdi-chat"></i>
            <span>{{ post.post_heat }}</span>
          </span>
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

const handleSortChange = (value) => {
  currentSort.value = value
}
</script>

<script>

</script>

<style scoped>
.home {
  width: 100%;
}

.sort-select {
  width: 160px;
  margin: 20px 0 0 0;
}

.option-label {
  display: flex;
  align-items: center;
  gap: 8px;
}

.option-label i {
  font-size: 1.2em;
  color: var(--primary-color);
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
  font-weight: 600;  /* 加粗 */
  color: #1a1a1a;  /* 更深的颜色 */
}

.post-meta {
  font-size: 0.9rem;
  color: #666;
  display: flex;
  align-items: center;
  gap: 20px;  /* 增大间距 */
}

.author, .time {
  display: flex;
  align-items: center;
  gap: 4px;
  color: #999;  /* 统一使用浅灰色 */
}

.author {
  font-weight: normal;  /* 取消加粗 */
  font-size: 0.9em;  /* 恢复默认大小 */
}

.author i, .time i {
  font-size: 1.1em;
}

.post-stats {
  font-size: 0.9rem;
  color: #666;
  display: flex;
  align-items: center;
}

.reply-count {
  display: flex;
  align-items: center;
  gap: 8px;  /* 增大间距 */
}

.reply-count i {
  font-size: 1.1em;
}

@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
  }
}

.filter-container {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
}

.sort-options,
.filter-options {
  position: relative;
  width: 120px;
}
</style>
