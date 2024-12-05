<template>
  <div class="create-post">
    <h1>创建帖子</h1>
    <form @submit.prevent="submitPost">
      <div class="form-group">
        <label for="title">帖子主题</label>
        <input type="text" id="title" v-model="post.title" required placeholder="输入帖子主题" />
      </div>

      <div class="form-group">
        <label for="content">帖子内容</label>
        <textarea id="content" v-model="post.content" required placeholder="输入帖子内容"></textarea>
      </div>

      <div class="form-group">
        <label for="images">上传图片</label>
        <input type="file" id="images" @change="handleFileUpload" accept="image/*" multiple />
      </div>

      <div class="image-preview">
        <h3>预览图片</h3>
        <div class="preview-container">
          <div v-for="(image, index) in post.images" :key="index" class="image-item">
            <img :src="image.url" alt="上传的图片" class="preview-image" />
            <button @click="removeImage(index)" class="remove-button">删除</button>
          </div>
        </div>
      </div>

      <div class="form-group">
        <label for="tags">帖子标签</label>
        <div class="tag-selection">
          <select v-model="selectedTag" @change="addTag">
            <option value="">选择标签</option>
            <option v-for="tag in availableTags" :key="tag" :value="tag">{{ tag }}</option>
          </select>
          <div class="selected-tags">
            <span v-for="(tag, index) in post.tags" :key="index" class="tag">
              {{ tag }} <button @click="removeTag(tag)">x</button>
            </span>
          </div>
        </div>
      </div>


      <button type="submit" class="submit-button">发布帖子</button>
      <button type="button" @click="saveDraft" class="draft-button">保存草稿</button>

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const post = ref({
  title: '',
  content: '',
  images: [],
  tags: [],
});

const availableTags = ['技术', '生活', '学习', '分享', '其他'];
const selectedTag = ref('');

const addTag = () => {
  if (selectedTag.value && !post.value.tags.includes(selectedTag.value)) {
    post.value.tags.push(selectedTag.value);
    selectedTag.value = ''; // 清空选择
  }
};

const removeTag = (tag) => {
  post.value.tags = post.value.tags.filter(t => t !== tag);
};

const handleFileUpload = (event) => {
  const files = Array.from(event.target.files);
  files.forEach(file => {
    const url = URL.createObjectURL(file);
    post.value.images.push({ file, url }); // 存储文件和对应的临时 URL
  });
};

const removeImage = (index) => {
  post.value.images.splice(index, 1); // 删除指定索引的图片
};

/*
const submitPost = () => {
  const formData = new FormData();
  formData.append('title', post.value.title);
  formData.append('content', post.value.content);
  
  post.value.images.forEach(image => {
    formData.append('images[]', image.file); // 添加文件到表单数据中
  });
  formData.append('tags', JSON.stringify(post.value.tags));

  // 这里可以添加你的发布逻辑，比如发送到服务器
  console.log('发布帖子:', formData);
  

  // 重置表单
  localStorage.removeItem('postDraft');
  post.value.title = '';
  post.value.content = '';
  post.value.images = [];
  post.value.tags = [];

  alert('帖子已发布！');
  window.location.href = '/'; // 或者跳转到其他路径
};
*/

const submitPost = () => {
  const formData = new FormData();
  formData.append('title', post.value.title);
  formData.append('content', post.value.content);
  
  post.value.images.forEach(image => {
    formData.append('images[]', image.file); // 添加文件到表单数据中
  });
  formData.append('tags', JSON.stringify(post.value.tags));

  // 这里可以添加你的发布逻辑，比如发送到服务器
  console.log('发布帖子:', formData);
  const response = createpost(formData)
  const data = response.data
  if(data.code === 1)
  {
    alert('帖子已发布！');
    router.push('/');
    // window.location.href = '/'; // 或者跳转到其他路径
  }
  else
  {
    alert(data.message)
  }
    // 重置表单
    localStorage.removeItem('postDraft');
    post.value.title = '';
    post.value.content = '';
    post.value.images = [];
    post.value.tags = [];
    post.value.user_id = '';
};

const saveDraft = () => {
  localStorage.setItem('postDraft', JSON.stringify(post.value));
  alert('草稿已保存！');
  window.location.href = '/'; // 或者跳转到其他路径
};
</script>

<style scoped>
.create-post {
  width: 100%;
  margin: 40px auto;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

input[type="text"],
textarea,
input[type="file"] {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

input[type="text"]:focus,
textarea:focus {
  border-color: #007bff;
  outline: none;
}

textarea {
  resize: vertical;
  height: 150px;
}

.image-preview {
  margin-top: 20px;
}

.preview-container {
  display: flex;
  flex-wrap: wrap;
}

.image-item {
  position: relative;
  margin-right: 10px;
  margin-bottom: 10px;
}

.preview-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
}

.remove-button {
  position: absolute;
  top: 5px;
  right: 5px;
  background: skyblue;
  color: white;
  border: none;
  cursor: pointer;
  padding: 2px 5px;
}

.tag-selection {
  display: flex;
  flex-direction: column;
}

select {
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.selected-tags {
  margin-top: 10px;
}

.tag {
  display: inline-block;
  background-color: #e0e0e0;
  padding: 5px 10px;
  border-radius: 4px;
  margin-right: 5px;
  font-size: 14px;
}

.tag button {
  background: none;
  border: none;
  color: red;
  cursor: pointer;
  margin-left: 5px;
}

.submit-button {
  width: 100%;
  background-color: #007bff;
  color: white;
  padding: 12px;
  margin-bottom: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.submit-button:hover {
  background-color: #0056b3;
}

.draft-button {
  width: 100%;
  background-color: #ffc107;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.draft-button:hover {
  background-color: #e0a800;
}
</style>
