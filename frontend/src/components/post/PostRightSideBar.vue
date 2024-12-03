<template>
    <div class="right-sidebar">
      <div class="action-buttons">
        <button @click="scrollToTop" class="action-btn">
          <i class="mdi mdi-arrow-up"></i>
          <span>返回顶部</span>
        </button>
  
        <button @click="toggleFloorPicker" class="action-btn">
          <i class="mdi mdi-format-list-numbered"></i>
          <span>跳转楼层</span>
        </button>
  
        <button @click="$emit('toggleAuthorOnly')" class="action-btn">
          <i class="mdi mdi-account-eye"></i>
          <span>只看楼主</span>
        </button>
  
        <button @click="$emit('reply')" class="action-btn primary">
          <i class="mdi mdi-reply"></i>
          <span>回复帖子</span>
        </button>
  
        <button @click="$emit('share')" class="action-btn">
          <i class="mdi mdi-share"></i>
          <span>分享帖子</span>
        </button>
      </div>
  
      <!-- 楼层选择器 -->
      <div v-if="showFloorPicker" class="floor-picker">
        <div class="floor-picker-header">
          <h3>跳转到楼层</h3>
          <button @click="toggleFloorPicker" class="close-btn">&times;</button>
        </div>
        <div class="floor-list">
          <button 
            v-for="floor in totalFloors" 
            :key="floor"
            @click="jumpToFloor(floor)"
            class="floor-btn"
          >
            {{ floor }}楼
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  defineProps({
    totalFloors: {
      type: Number,
      required: true
    }
  })
  
  defineEmits(['scrollToFloor', 'toggleAuthorOnly', 'reply', 'share'])
  
  const showFloorPicker = ref(false)
  
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
  
  const toggleFloorPicker = () => {
    showFloorPicker.value = !showFloorPicker.value
  }
  
  const jumpToFloor = (floor) => {
    emit('scrollToFloor', floor)
    showFloorPicker.value = false
  }
  </script>
  
  <style scoped>
  .right-sidebar {
    position: sticky;
    top: 20px;
    width: 200px;
    align-self: flex-start;
  }
  
  .action-buttons {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  
  .action-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background: white;
    cursor: pointer;
    transition: all 0.3s;
  }
  
  .action-btn:hover {
    background: #f0f0f0;
  }
  
  .action-btn.primary {
    background: var(--primary-color);
    color: white;
  }
  
  .action-btn.primary:hover {
    opacity: 0.9;
  }
  
  .floor-picker {
    position: absolute;
    top: 0;
    right: 0;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 16px;
    width: 240px;
  }
  
  .floor-picker-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  
  .floor-picker-header h3 {
    margin: 0;
    font-size: 1rem;
  }
  
  .close-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0;
  }
  
  .floor-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    max-height: 240px;
    overflow-y: auto;
  }
  
  .floor-btn {
    padding: 4px 8px;
    border: 1px solid #eee;
    border-radius: 4px;
    background: none;
    cursor: pointer;
  }
  
  .floor-btn:hover {
    background: #f0f0f0;
  }
  </style>