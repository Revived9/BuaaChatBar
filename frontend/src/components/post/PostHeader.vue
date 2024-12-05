<template>
    <div class="post-header-wrapper" :style="{  backgroundColor: getColor(post.section) }">
      <div class="post-header">
        <h1 class="post-title">{{ post.post_title }}</h1>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    post: {
      type: Object,
      required: true
    }
  })

  const sectionColors = {
  announcement: '#FF4D4F',
  featured: '#722ED1',
  study: '#FADB14',
  life: '#52C41A',
  lost: '#13C2C2',
  confession: '#FF85C0',
};

// 根据 id 获取 color
const getColor = (id) => {
  return sectionColors[id] || '#FFFFFF'; // 如果没有匹配的 id，则返回默认颜色
};
  </script>
  
  <style scoped>
  .post-header-wrapper {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    color: white;
  }
  
  .post-header {
    max-width: 1200px;
    margin: 0 auto;
    padding: 24px 20px;
  }
  
  .post-tags {
    margin-bottom: 12px;
  }
  
  .tag {
    display: inline-block;
    padding: 4px 12px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    margin-right: 8px;
    font-size: 0.9rem;
  }
  
  .post-title {
    font-size: 1.8rem;
    margin: 0;
    font-weight: 500;
  }
  </style>