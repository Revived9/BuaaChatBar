<template>
    <div class="post-content">
      <!-- 主贴 -->
      <div id="floor-1" class="post-item main-post">
        <div class="post-meta">
          <div class="author-info">
            <img :src="post.author.avatar" :alt="post.author.name" class="avatar" />
            <span class="author-name">{{ post.author.name }}</span>
          </div>
          <div class="post-info">
            <span class="floor">1楼</span>
            <span class="time">{{ formatTime(post.createTime) }}</span>
          </div>
        </div>
        <div class="post-body">
          {{ post.content }}
        </div>
      </div>
  
      <!-- 回复列表 -->
      <div 
        v-for="(reply, index) in displayReplies" 
        :key="reply.id"
        :id="`floor-${index + 2}`"
        class="post-item reply"
      >
        <div class="post-meta">
          <div class="author-info">
            <img :src="reply.author.avatar" :alt="reply.author.name" class="avatar" />
            <span class="author-name">{{ reply.author.name }}</span>
          </div>
          <div class="post-info">
            <span class="floor">{{ index + 2 }}楼</span>
            <span class="time">{{ formatTime(reply.createTime) }}</span>
          </div>
        </div>
        <div class="post-body">
          {{ reply.content }}
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  
  const props = defineProps({
    post: {
      type: Object,
      required: true
    },
    replies: {
      type: Array,
      default: () => []
    },
    authorOnly: {
      type: Boolean,
      default: false
    }
  })
  
  const displayReplies = computed(() => {
    if (props.authorOnly) {
      return props.replies.filter(reply => reply.author.id === props.post.author.id)
    }
    return props.replies
  })
  
  const formatTime = (date) => {
    return new Date(date).toLocaleString()
  }
  </script>
  
  <style scoped>
  .post-content {
    flex: 1;
    background: white;
    min-height: calc(100vh - 60px);
  }
  
  .post-item {
    padding: 24px 32px;
    position: relative;
  }
  
  /* 为除了最后一个回复之外的所有回复添加分割线 */
  .post-item:not(:last-child)::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 32px;
    right: 32px;
    height: 1px;
    background-color: #f0f0f0;
  }
  
  .post-meta {
    display: flex;
    justify-content: space-between;
    margin-bottom: 16px;
  }
  
  .author-info {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  
  .author-name {
    font-weight: 500;
    color: #333;
  }
  
  .post-info {
    color: #8c8c8c;
    font-size: 0.9rem;
    display: flex;
    gap: 12px;
  }
  
  .post-body {
    line-height: 1.8;
    color: #262626;
    font-size: 1rem;
    padding-left: 52px; /* 与头像对齐 */
  }
  
  .main-post {
    padding-top: 32px;
  }
  
  /* 移除主贴的背景色 */
  .main-post {
    background-color: transparent;
  }
  </style>