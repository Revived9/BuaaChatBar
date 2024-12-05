<template>
    <div class="right-sidebar">
      <div class="action-buttons">
        <button @click="showReplyDialog" class="action-btn reply-btn">
          <i class="mdi mdi-reply"></i>
          <span>{{ isLoggedIn ? '回复帖子' : '登录以回复' }}</span>
        </button>
  
        <button @click="$emit('toggleAuthorOnly')" class="action-btn">
          <i class="mdi mdi-account-eye"></i>
          <span>只看楼主</span>
        </button>
  
        <button @click="$emit('share')" class="action-btn">
          <i class="mdi mdi-share"></i>
          <span>分享帖子</span>
        </button>
  
        <button @click="toggleFloorPicker" class="action-btn">
          <i class="mdi mdi-format-list-numbered"></i>
          <span>跳转楼层</span>
        </button>
  
        <button @click="scrollToTop" class="action-btn">
          <i class="mdi mdi-arrow-up"></i>
          <span>返回顶部</span>
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
  
    <ReplyPostDialog 
      v-if="isReplyDialogVisible" 
      :postId="postId"
      @close="closeReplyDialog" 
    />
  
    <LoginDialog
      v-if="isLoginDialogVisible"
      @close="closeLoginDialog"
    />
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { useStore } from 'vuex'
  import ReplyPostDialog from '@/components/dialogs/ReplyPostDialog.vue'
  import LoginDialog from '@/components/auth/LoginDialog.vue'
  
  const store = useStore()
  
  // 添加登录状态检查
  const isLoggedIn = computed(() => store.state.user.isLoggedIn)
  
  defineProps({
    totalFloors: {
      type: Number,
      required: true
    },
    postId: {
      type: Number,
      required: true
    }
  })
  
  defineEmits(['scrollToFloor', 'toggleAuthorOnly', 'reply', 'share'])
  
  const showFloorPicker = ref(false)
  const isReplyDialogVisible = ref(false)
  const isLoginDialogVisible = ref(false)
  
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
  
  const showReplyDialog = () => {
    if (isLoggedIn.value) {
      isReplyDialogVisible.value = true
    } else {
      isLoginDialogVisible.value = true
    }
  }
  
  const closeReplyDialog = () => {
    isReplyDialogVisible.value = false
  }
  
  const closeLoginDialog = () => {
    isLoginDialogVisible.value = false
  }
  </script>
  
  <style scoped>
  .right-sidebar {
    position: sticky;
    top: 20px;
    width: 140px;
    align-self: flex-start;
    margin-left: 32px;
  }
  
  .action-buttons {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .action-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 8px 12px;
    border: none;
    border-radius: 4px;
    background-color: #e4edf6;
    color: #000;
    cursor: pointer;
    transition: all 0.3s;
    height: 36px;
  }
  
  .action-btn i {
    font-size: 1rem;
  }
  
  .action-btn span {
    font-size: 0.85rem;
    white-space: nowrap;
  }
  
  .action-btn:hover {
    background: #d1e1f0;
  }
  
  .reply-btn {
    background: #0153b8;
    color: white;
  }
  
  .reply-btn:hover {
    background: #013A80;
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