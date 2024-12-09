<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { createpost } from '@/services/api'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios';

const store = useStore()
const emit = defineEmits(['close'])
const router = useRouter()
const route = useRoute()

const post = ref({
  title: '',
  content: '',
  section: '',  // 当前选中的板块
  tags: [],
  images: [],
  image: [],
  user_id: store.state.user.studentId
})

const tagInput = ref('')
const textarea = ref(null)

// 获取所有非筛选类板块
const sections = [
  {
    id: 'announcement',
    name: '公告',
    icon: 'mdi mdi-bullhorn-outline',
    iconActive: 'mdi mdi-bullhorn',
    color: '#FF4D4F',
  },
  {
    id: 'featured',
    name: '精华',
    icon: 'mdi mdi-crown-outline',
    iconActive: 'mdi mdi-crown',
    color: '#722ED1',
  },
  {
    id: 'study',
    name: '学习',
    icon: 'mdi mdi-school-outline',
    iconActive: 'mdi mdi-school',
    color: '#FADB14',
  },
  {
    id: 'life',
    name: '生活',
    icon: 'mdi mdi-coffee-outline',
    iconActive: 'mdi mdi-coffee',
    color: '#52C41A',
  },
  {
    id: 'lost',
    name: '拾遗',
    icon: 'mdi mdi-package-variant-closed',
    iconActive: 'mdi mdi-package-variant',
    color: '#13C2C2',
  },
  {
    id: 'confession',
    name: '表白墙',
    icon: 'mdi mdi-heart-outline',
    iconActive: 'mdi mdi-heart',
    color: '#FF85C0',
  }
]

const selectSection = (section) => {
  post.value.section = section.id
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
    post.value.content = post.value.content.substring(0, start) + 
                        imageMarkdown + 
                        post.value.content.substring(end)
    
    // 更新光标位置
    textarea_el.focus()
    const newCursorPos = start + imageMarkdown.length
    textarea_el.setSelectionRange(newCursorPos, newCursorPos)
    
    // 将图片添加到images数组中以便后续上传
    post.value.images.push({ file, url: imageUrl })
    post.value.image.push(file)
  } catch (error) {
    console.error('插入图片失败:', error)
    alert('插入图片失败，请重试')
  }
}

// 删除图片
const removeImage = (index) => {
  post.value.images.splice(index, 1)
  post.value.image.splice(index, 1)
}

// 添加标签
const addTag = () => {
  if (tagInput.value.trim() && !post.value.tags.includes(tagInput.value.trim())) {
    post.value.tags.push(tagInput.value.trim())
    tagInput.value = ''
  }
}

// 删除标签
const removeTag = (tag) => {
  post.value.tags = post.value.tags.filter(t => t !== tag)
}

// 提交帖子
const submitPost = async () => {
  try {
    // 调用 createpost 函数进行帖子发布
    const response = await createpost(post.value);
    const data = response.data;
    if (data.code === 1) {
      // 在请求成功后处理响应
      alert('发布成功');
      
      // 关闭对话框
      emit('close');
      
      // 触发父组件的刷新方法
      emit('refresh');
      
      // 如果在首页，刷新路由
      if (route.path === '/') {
        router.go(0);
      } else {
        // 跳转到首页
        router.push('/');
      }
    } else {
      // 处理发布失败的情况
      alert('发布失败: ' + data.message);
    }
  } catch (error) {
    console.error(error);
    alert(error.message);  // 显示捕获到的错误信息
  }
}


// 添加获取板块样式的方法
const getSectionStyle = (section) => {
  const isActive = post.value.section === section.id
  return {
    '--section-color': section.color,
    'color': isActive ? 'white' : section.color,
    'background-color': isActive ? section.color : 'transparent',
    'border-color': section.color
  }
}

</script>

<template>
  <div class="dialog-overlay" @click.self="emit('close')">
    <div class="dialog-content">
      <div class="dialog-header">
        <h2>发布主题</h2>
        <button class="close-btn" @click="emit('close')">&times;</button>
      </div>

      <div class="dialog-body">
        <div class="form-group">
          <label for="title">标题</label>
          <input type="text" id="title" v-model="post.title" placeholder="请输入标题" required />
        </div>

        <div class="form-group">
          <label>选择板块</label>
          <div class="section-selector">
            <button v-for="section in sections" :key="section.id" class="section-btn"
              :class="{ active: post.section === section.id }" :style="getSectionStyle(section)"
              @click="selectSection(section)">
              <div class="section-icon" :style="{ background: post.section === section.id ? 'white' : section.color }">
                <i :class="post.section === section.id ? section.iconActive : section.icon"
                  :style="{ color: post.section === section.id ? section.color : 'white' }"></i>
              </div>
              <span class="section-name">{{ section.name }}</span>
            </button>
          </div>
        </div>

        <div class="form-group">
          <label for="content">内容</label>
          <textarea 
            id="content" 
            v-model="post.content" 
            placeholder="请输入内容（支持 Markdown 格式）" 
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
            <div v-for="(image, index) in post.images" :key="index" class="preview-item">
              <img :src="image.url" alt="预览图片" />
              <button @click="removeImage(index)" class="remove-image">&times;</button>
            </div>
          </div>
        </div>
      </div>

      <div class="dialog-footer">
        <button class="cancel-btn" @click="emit('close')">取消</button>
        <button class="submit-btn" @click="submitPost">发布</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background: white;
  border-radius: 12px;
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
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
  padding: 24px;
}

/* 板块选择器样式优化 */
.section-selector {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
  gap: 12px;
  margin-top: 8px;
}

.section-btn {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 8px 6px;
  border: 1.5px solid transparent;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.section-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: currentColor;
  opacity: 0.08;
  transition: opacity 0.3s;
  border-radius: 10px;
}

.section-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.section-btn:hover::before {
  opacity: 0.12;
}

.section-btn.active {
  border-color: currentColor;
}

.section-btn.active::before {
  opacity: 0.15;
}

.section-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  transition: all 0.3s;
}

.section-icon i {
  font-size: 18px;
  line-height: 1;
  z-index: 1;
  transition: color 0.3s;
}

.section-name {
  font-size: 0.8rem;
  font-weight: 500;
  transition: color 0.3s;
}

.section-btn:hover .section-icon {
  transform: scale(1.1);
}

/* 表单组样式优化 */
.form-group {
  margin-bottom: 24px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #333;
  font-size: 0.95rem;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  box-sizing: border-box;
  font-size: 0.95rem;
  transition: border-color 0.3s;
}

input[type="text"]:focus,
textarea:focus {
  border-color: var(--primary-color);
  outline: none;
}

textarea {
  min-height: 180px;
  resize: vertical;
}

/* 标签输入区域样式 */
.tag-input input {
  margin-bottom: 12px;
}

.tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.tag {
  background-color: var(--secondary-color);
  color: var(--primary-color);
  padding: 6px 12px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.9rem;
}

.remove-tag {
  background: none;
  border: none;
  color: var(--primary-color);
  cursor: pointer;
  padding: 0;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  transition: background-color 0.2s;
}

.remove-tag:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

/* 图片上传区域样式 */
input[type="file"] {
  display: none;
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

.image-preview {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
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
  top: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  border: none;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.remove-image:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* 底部按钮样式 */
.dialog-footer {
  padding: 20px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
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
  background-color: #1a7fd1;
  transform: translateY(-1px);
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
</style>