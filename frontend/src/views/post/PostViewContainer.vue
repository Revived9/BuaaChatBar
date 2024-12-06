<template>
    <div class="post-view-container">
      <div class="post-view">
        <PostHeader :post="post" />
        <div class="post-content-wrapper">
          <PostContent :post="post" :replies="replies" />
          <PostRightSideBar 
            :totalFloors="replies.length + 1"
            :authorId="post?.author?.id"
            :postId="postId"
            @scrollToFloor="handleScrollToFloor"
            @toggleAuthorOnly="handleToggleAuthorOnly"
            @reply="handleReply"
            @share="handleShare"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import PostHeader from '@/components/post/PostHeader.vue'
  import PostContent from '@/components/post/PostContent.vue'
  import PostRightSideBar from '@/components/post/PostRightSideBar.vue'
  import {getsinglepost} from "@/services/api.js";
  import { watch } from 'vue';
  
  const route = useRoute()
  const postId = parseInt(route.params.id)

  
  // 初始化空数据
  const post = ref({})
  const replies = ref([])

  watch(post, (newPost) => {
    console.log('post updated:', newPost)
  })
  
  // 处理楼层跳转
  const handleScrollToFloor = (floor) => {
    const element = document.querySelector(`#floor-${floor}`)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }
  
  // 处理只看楼主
  const handleToggleAuthorOnly = () => {
    // 实现只看楼主的逻辑
  }
  
  // 处理回复
  const handleReply = () => {
    // 实现回复的逻辑
  }
  
  // 处理分享
  const handleShare = () => {
    // 实现分享的逻辑
  }

  // 在组件挂载时获取数据
onMounted(async () => {
  try {
    console.log(postId)
    post.value = await getpost(postId);  // 获取帖子
    replies.value = await getreplies(postId);  // 获取回复
  } catch (error) {
    console.error('加载帖子或回复时出错:', error);
  }
});
  </script>

<script>
  // 获取帖子
  import {getsinglepost, getallreplies} from "@/services/api.js";

  export const getpost = async (postid) => {
    try {
      const post = {
        post_id : postid
      }
      console.log(post)
      const response = await getsinglepost(post);
      const data = response.data;

      console.log(data)

      if (data.code === 1) {
        return data
      } else {
        alert(data.message || '打开失败，请��试');
      }
    } catch (error) {
      console.error('打开失败:', error);
    }
  };

    export const getreplies = async (postid) => {
    try {
            const post = {
        post_id : postid
      }
      const response = await getallreplies(post);
      const data = response.data;

      console.log(data)
      if (data.code === 1) {
        //replies.value = data.replies;
        return data.data
      } else {
        alert(data.message || '打开失败，请重试');
      }
    } catch (error) {
      console.error('打开失败:', error);
    }
  };
</script>
  
  <style scoped>
  .post-view-container {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    background-color: white;
  }
  
  .post-view {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .post-content-wrapper {
    display: flex;
    gap: 20px;
    padding: 20px;
    box-sizing: border-box;
  }
  </style>