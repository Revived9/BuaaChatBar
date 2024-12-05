<template>
    <div class="home">
      <!-- 标签筛选区域 -->
      <div class="tags-container">
        <!-- 标签栏 -->
        <div class="tags">
          <span
            v-for="tag in visibleTags"
            :key="tag.id"
            :class="['tag', { selected: selectedTags.includes(tag.id) }]"
            @click="toggleTagSelection(tag.id)"
          >
            {{ tag.name }}
          </span>
          <span class="more-tags" @click="toggleMoreTags">更多</span>
        </div>
  
        <!-- 已选标签显示 -->
        <div class="selected-tags">
          <span
            v-for="tag in selectedTags"
            :key="tag"
            class="selected-tag"
            @click="removeSelectedTag(tag)"
          >
            {{ getTagNameById(tag) }} <span class="remove-tag">&times;</span>
          </span>
        </div>
  
        <!-- 更多标签的下拉列表 -->
        <div v-if="showMoreTags" class="more-tags-dropdown">
          <span
            v-for="tag in moreTags"
            :key="tag.id"
            :class="['tag', { selected: selectedTags.includes(tag.id) }]"
            @click="toggleTagSelection(tag.id)"
          >
            {{ tag.name }}
          </span>
        </div>
      </div>
  
      <!-- 帖子列表 -->
      <div class="post-list">
        <div v-for="post in filteredPosts" :key="post.id" class="post-item">
          <div class="post-avatar">
            <img :src="post.author.avatar" :alt="post.author.name" />
          </div>
          <div class="post-content">
            <h3 class="post-title">{{ post.title }}</h3>
            <div class="post-meta">
              <span class="author">{{ post.author.name }}</span>
              <span class="time">{{ formatTime(post.lastReplyTime) }}</span>
              <span class="category">{{ post.category }}</span>
            </div>
            <div class="post-tags">
              <!-- 显示帖子的标签 -->
              <span
                v-for="tagId in post.tagIds"
                :key="tagId"
                class="post-tag"
              >
                {{ getTagNameById(tagId) }}
              </span>
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
  import { gettagpost } from '@/services/api';
  
  // 标签数据
  const tags = [
    { id: 1, name: "Vue" },
    { id: 2, name: "React" },
    { id: 3, name: "JavaScript" },
    { id: 4, name: "Node.js" },
    { id: 5, name: "CSS" },
    { id: 6, name: "HTML" },
    { id: 7, name: "TypeScript" },
    { id: 8, name: "GraphQL" },
    { id: 9, name: "Web性能" },
    { id: 10, name: "前端工程化" }
  ]
  
  // 当前选择的标签（存储标签 ID）
  const selectedTags = ref([])
  
  // 控制更多标签的显示/隐藏
  const showMoreTags = ref(false)
  
  // 切换标签的选中状态
  const toggleTagSelection = (tagId) => {
    const index = selectedTags.value.indexOf(tagId)
    if (index === -1) {
      selectedTags.value.push(tagId) // 选中标签
    } else {
      selectedTags.value.splice(index, 1) // 取消选中
    }
  }
  
  // 切换显示更多标签
  const toggleMoreTags = () => {
    showMoreTags.value = !showMoreTags.value
  }
  
  /*
  // 根据选中的标签过滤帖子
  const filteredPosts = computed(() => {
    if (selectedTags.value.length === 0) {
      return posts.value // 如果没有选择标签，返回所有帖子
    }
    return posts.value.filter(post =>
      post.tagIds.some(tagId => selectedTags.value.includes(tagId))
    )
  })
    */

    // 根据选中的标签过滤帖子
    const filteredPosts = computed(() => {
    const response = gettagpost(selectedTags)
    const data = response.date
    return data
    // if (selectedTags.value.length === 0) {
    //   return posts.value // 如果没有选择标签，返回所有帖子
    // }
    // return posts.value.filter(post =>
    //   post.tagIds.some(tagId => selectedTags.value.includes(tagId))
    // )
  })
  
  // 模拟帖子数据
  const posts = ref([
    {
      id: 1,
      title: "Vue 3 组件通信最佳实践",
      author: { name: "张三", avatar: "/avatars/zhangsan.jpg" },
      lastReplyTime: new Date("2023-05-10T10:30:00"),
      category: "前端开发",
      replyCount: 15,
      tagIds: [1, 3] // 关联标签ID
    },
    {
      id: 2,
      title: "如何优化 Webpack 构建速度？",
      author: { name: "李四", avatar: "/avatars/lisi.jpg" },
      lastReplyTime: new Date("2023-05-09T16:45:00"),
      category: "工程化",
      replyCount: 8,
      tagIds: [2, 5] // 关联标签ID
    },
    {
      id: 3,
      title: "深入理解 JavaScript 闭包",
      author: { name: "王五", avatar: "/avatars/wangwu.jpg" },
      lastReplyTime: new Date("2023-05-08T14:45:00"),
      category: "前端开发",
      replyCount: 10,
      tagIds: [3, 6] // 关联标签ID
    },
    // 更多帖子...
  ])
  
  // 格式化时间
  const formatTime = (date) => {
    return date.toLocaleString()
  }
  
  // 获取标签名称
  const getTagNameById = (tagId) => {
    const tag = tags.find(tag => tag.id === tagId)
    return tag ? tag.name : ''
  }
  
  // 显示的标签（最多显示6个标签，剩余的显示“更多”）
  const visibleTags = computed(() => {
    return tags.slice(0, 6)
  })
  
  // 更多标签列表
  const moreTags = computed(() => {
    return tags.slice(6)
  })
  
  // 移除已选标签
  const removeSelectedTag = (tagId) => {
    const index = selectedTags.value.indexOf(tagId)
    if (index !== -1) {
      selectedTags.value.splice(index, 1)
    }
  }
  </script>
  
  <style scoped>
  .home {
    width: 100%;
  }
  
  .tags-container {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  
  .tags {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
  }
  
  .tag {
    padding: 5px 10px;
    background-color: #f0f0f0;
    border-radius: 20px;
    cursor: pointer;
  }
  
  .tag.selected {
    background-color: #007bff;
    color: white;
  }
  
  .more-tags {
    margin-left: 10px;
    color: #007bff;
    cursor: pointer;
  }
  
  .selected-tags {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  
  .selected-tag {
    padding: 5px 10px;
    background-color: #007bff;
    color: white;
    border-radius: 20px;
    cursor: pointer;
  }
  
  .selected-tag .remove-tag {
    margin-left: 5px;
    cursor: pointer;
  }
  
  .more-tags-dropdown {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
  }
  
  .post-list {
    display: flex;
    flex-direction: column;
  }
  
  .post-item {
    display: flex;
    align-items: center;
    padding: 15px;
    margin-bottom: 10px;
    background-color: white;
    transition: background-color 0.2s, transform 0.2s;
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
  
  .post-meta > * {
    margin-right: 10px;
  }
  
  .post-tags {
    margin-top: 5px;
    font-size: 0.9rem;
  }
  
  .post-tag {
    display: inline-block;
    padding: 3px 6px;
    background-color: #e0e0e0;
    border-radius: 12px;
    margin-right: 5px;
  }
  
.post-stats {
    font-size: 0.9rem;
    color: #666;
}
    
@media (max-width: 1024px) {
    tags-container {
    flex-direction: column;
    }
}
</style>