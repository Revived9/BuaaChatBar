<template>
    <div class="post-header-wrapper" :style="{ backgroundColor: post.section.color }">
      <div class="post-header">
        <div class="post-tags">
          <span 
            v-for="tag in post.tags" 
            :key="tag" 
            class="tag"
          >
            {{ tag }}
          </span>
        </div>
        <h1 class="post-title">{{ post.title }}</h1>
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