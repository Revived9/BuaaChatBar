<template>
  <div class="profile-list">
    <div class="list-section">
      <div 
        v-for="item in mainMenuItems" 
        :key="item.id"
        :class="['list-item', { active: modelValue === item.id }]"
        @click="$emit('update:modelValue', item.id)"
      >
        <i :class="item.icon"></i>
        {{ item.name }}
        <span class="count" v-if="item.count">{{ item.count }}</span>
      </div>
    </div>
    <div class="list-section settings" v-if="isCurrentUser">
      <div 
        v-for="item in settingsMenuItems" 
        :key="item.id"
        :class="['list-item', { active: modelValue === item.id }]"
        @click="$emit('update:modelValue', item.id)"
      >
        <i :class="item.icon"></i>
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  isCurrentUser: {
    type: Boolean,
    default: false
  },
  modelValue: {
    type: String,
    required: true
  }
})

defineEmits(['update:modelValue'])

const mainMenuItems = [
  //{ id: 'replies', name: '回复', icon: 'fas fa-comment', count: 0 },
  { id: 'posts', name: '主题', icon: 'mdi mdi-comment', count: 0 },
  //{ id: 'badges', name: '徽章', icon: 'fas fa-medal', count: 0 },
  //{ id: 'likes', name: '赞', icon: 'fas fa-heart', count: 0 },
  //{ id: 'mentions', name: '被提及', icon: 'fas fa-at', count: 0 },
]

const settingsMenuItems = [
  { id: 'settings', name: '设置', icon: 'mdi mdi-cog' },
  { id: 'security', name: '安全', icon: 'mdi mdi-shield-check' },
]
</script>

<style scoped>
.profile-list {
  background: white;
  border-radius: 8px;
  padding: 16px 0;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 20px;
  height: fit-content;
}

.list-section {
  padding: 8px 0;
}

.list-section.settings {
  border-top: 1px solid #eee;
  margin-top: 16px;
  padding-top: 16px;
}

.list-item {
  padding: 12px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  color: #666;
  transition: all 0.3s;
}

.list-item i {
  width: 20px;
}

.list-item:hover {
  background: var(--secondary-color);
  color: var(--primary-color);
}

.list-item.active {
  background: var(--secondary-color);
  color: var(--primary-color);
  font-weight: 500;
}

.count {
  margin-left: auto;
  background: #eee;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.8rem;
}
</style> 