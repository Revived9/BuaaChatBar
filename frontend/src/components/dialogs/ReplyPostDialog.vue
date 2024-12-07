<template>
  <div class="dialog-overlay" @click.self="$emit('close')">
    <div class="dialog-content">
      <div class="dialog-header">
        <h2>回复帖子</h2>
        <button class="close-btn" @click="$emit('close')">&times;</button>
      </div>

      <div class="dialog-body">
        <div class="form-group">
          <label for="content">回复内容</label>
          <textarea 
            id="content" 
            v-model="content"
            placeholder="请输入回复内容（支持 Markdown 格式）"
            required
            ref="textarea"
          ></textarea>
        </div>

        <div class="form-group">
          <label class="file-upload-btn">
            <i class="mdi mdi-image-plus"></i>
            <span>插入图片</span>
            <input 
              type="file" 
              @change="handleImageInsert" 
              accept="image/*"
              style="display: none"
            />
          </label>
          <div class="image-preview">
            <div v-for="(image, index) in images" :key="index" class="preview-item">
              <img :src="image.url" alt="预览图片" />
              <button @click="removeImage(index)" class="remove-image">&times;</button>
            </div>
          </div>
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
import { reply} from "@/services/api.js";
import {getreplies} from "@/views/post/PostViewContainer.vue";
import { useRouter, useRoute } from 'vue-router'

const store = useStore()
const emit = defineEmits(['close'])
const router = useRouter()
const route = useRoute()

const props = defineProps({
  postId: {
    type: Number,
    required: true
  }
})

const content = ref('')
const images = ref([])
const image = ref([])
const textarea = ref(null)

// // 处理图片上传
// const handleFileUpload = (event) => {
//   const files = Array.from(event.target.files)
//   console.log(files)
//   files.forEach(file => {
//     const url = URL.createObjectURL(file)
//     images.value.push({ file, url })
//     image.value.push(file)
//   })
// }

// 删除图片
const removeImage = (index) => {
  images.value.splice(index, 1)
  image.value.splice(index, 1)
}

// 提交回复
const handleSubmit = async () => {
  if (!content.value.trim()) {
    alert('请输入回复内容')
    return
  }

  try {
    const reply_content = {
      content: content.value,
      post_id: props.postId,
      user_id: store.state.user.studentId,
      image: image.value
    }

    console.log(images.value)
    console.log(image.value)
    const response = await reply(reply_content)

    const data = response.data;
    if (data.code === 1) {
      // 在请求成功后处理响应
      alert('发布成功');
      
      // 关闭对话框
      emit('close');
      
      // 触发父组件的刷新方法
      emit('refresh');
      
      // 如果在帖子详情页，刷新路由
      if (route.path.startsWith('/posts/')) {
        router.go(0);
      }
    } else {
      // 处理发布失败的情况
      alert('发布失败: ' + data.message);
    }
  } catch (error) {
    console.error('发送回复失败:', error)
    alert('发送回复失败,请重试')
  }
}

// 处理图片插入
const handleImageInsert = async (event) => {
  const file = event.target.files[0]
  if (!file) return

  try {
    // 创建临时URL以预览图片
    const imageUrl = URL.createObjectURL(file)
    
    // 获取光标位置
    const textarea_el = textarea.value
    const start = textarea_el.selectionStart
    const end = textarea_el.selectionEnd
    
    // 在光标位置插入Markdown图片语法
    const imageMarkdown = `![图片](${imageUrl})\n`
    content.value = content.value.substring(0, start) + 
                    imageMarkdown + 
                    content.value.substring(end)
    
    // 更新光标位置
    textarea_el.focus()
    const newCursorPos = start + imageMarkdown.length
    textarea_el.setSelectionRange(newCursorPos, newCursorPos)
    
    // 将图片添加到images数组中以便后续上传
    images.value.push({ file, url: imageUrl })
    console.log(file)
    image.value.push(file)
    console.log(image.value)
  } catch (error) {
    console.error('插入图片失败:', error)
    alert('插入图片失败，请重试')
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
  padding: 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dialog-header h2 {
  margin: 0;
  font-size: 1.5rem;
  color: #333;
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
  font-weight: 600;
  color: #333;
  font-size: 0.95rem;
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
  border-color: var(--primary-color);
  outline: none;
}

.file-upload-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: var(--secondary-color);
  color: var(--primary-color);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.file-upload-btn:hover {
  background-color: #d9e9ff;
}

input[type="file"] {
  display: none;
}

.image-preview {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 16px;
  margin-top: 16px;
}

.preview-item {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.preview-item img {
  width: 100%;
  height: 120px;
  object-fit: cover;
}

.remove-image {
  position: absolute;
  top: 4px;
  right: 4px;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  border: none;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.remove-image:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

.dialog-footer {
  padding: 12px 24px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 0;
}

.submit-btn,
.cancel-btn {
  padding: 10px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all 0.3s;
}

.submit-btn {
  background-color: var(--primary-color);
  color: white;
}

.submit-btn:hover {
  opacity: 0.9;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #666;
}

.cancel-btn:hover {
  background-color: #e8e8e8;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
  transition: color 0.2s;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  color: #666;
}

.markdown-editor,
.markdown-editor:focus-within,
.toolbar,
.image-upload-btn {
  /* 删除这些样式 */
}
</style> 