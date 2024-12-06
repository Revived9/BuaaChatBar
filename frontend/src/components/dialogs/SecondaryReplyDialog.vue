<template>
  <div class="dialog-overlay" @click.self="$emit('close')">
    <div class="dialog-content">
      <div class="dialog-header">
        <h2>回复 {{ replyToUsername }}</h2>
        <button class="close-btn" @click="$emit('close')">&times;</button>
      </div>

      <div class="dialog-body">
        <div class="form-group">
          <label for="content">回复内容</label>
          <textarea 
            id="content" 
            v-model="content"
            placeholder="请输入回复内容"
            required
          ></textarea>
        </div>
      </div>

      <div class="dialog-footer">
        <button class="cancel-btn" @click="$emit('close')">取消</button>
        <button class="submit-btn" @click="handleSubmit">发布回复</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const emit = defineEmits(['close'])
const content = ref('')

const props = defineProps({
  postId: {
    type: Number,
    required: true
  },
  replyToFloor: {
    type: Number,
    required: true
  },
  replyToUsername: {
    type: String,
    required: true
  }
})

const handleSubmit = async () => {
  if (!content.value.trim()) {
    alert('请输入回复内容')
    return
  }

  try {
    // TODO: 调用API发送二级回复
    const replyData = {
      content: content.value,
      post_id: props.postId,
      reply_to_floor: props.replyToFloor,
      user_id: store.state.user.studentId
    }
    
    console.log('发送二级回复:', replyData)
    // 这里添加发送二级回复的API调用
    
    emit('close')
  } catch (error) {
    console.error('发送回复失败:', error)
    alert('发送回复失败,请重试')
  }
}
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background: white;
  border-radius: 12px;
  width: 95%;
  max-width: 800px;
  max-height: 95vh;
  overflow-y: auto;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
}

.dialog-header {
  padding: 20px 24px;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dialog-header h2 {
  margin: 0;
  font-size: 1.25rem;
  color: #333;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #999;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}

.close-btn:hover {
  color: #666;
}

.dialog-body {
  padding: 20px 24px 0;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #333;
}

textarea {
  width: 100%;
  min-height: 200px;
  padding: 12px 16px;
  border: 2px solid #e8e8e8;
  border-radius: 8px;
  resize: vertical;
  font-size: 15px;
  line-height: 1.6;
  transition: border-color 0.3s;
}

textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}

.dialog-footer {
  padding: 12px 24px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 0;
}

.cancel-btn, .submit-btn {
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn {
  background: #f5f5f5;
  border: 1px solid #d9d9d9;
  color: #666;
}

.cancel-btn:hover {
  background: #e8e8e8;
}

.submit-btn {
  background: var(--primary-color);
  border: 1px solid var(--primary-color);
  color: white;
}

.submit-btn:hover {
  opacity: 0.85;
}

.submit-btn:disabled {
  background: #ccc;
  border-color: #ccc;
  cursor: not-allowed;
}
</style> 