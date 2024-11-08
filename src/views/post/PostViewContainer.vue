<template>
    <div class="post-view-container">
      <div class="post-view">
        <PostHeader :post="post" />
        <div class="post-content-wrapper">
          <PostContent :post="post" :replies="replies" />
          <PostRightSideBar 
            :totalFloors="replies.length + 1"
            :authorId="post?.author?.id"
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
  
  const route = useRoute()
  const postId = parseInt(route.params.id)
  
  // 模拟帖子数据
  const post = ref({
    id: postId,
    title: "Vue 3 组件通信最佳实践",
    content: "在 Vue 3 中，组件之间的通信方式主要包括：props/emit、provide/inject、Vuex 等。本文将详细介绍这些通信方式的最佳实践...",
    author: {
      id: 1,
      name: "张三",
      avatar: "/avatars/zhangsan.jpg"
    },
    createTime: new Date("2024-01-10T10:30:00"),
    section: {
      id: 'study',
      name: '学习',
      color: '#FADB14'
    },
    tags: ['Vue3', '前端开发', '组件通信']
  })
  
  // 模拟回复数据
  const replies = ref([
    {
      id: 1,
      content: "感谢分享，这篇文章对我很有帮助！",
      author: {
        id: 3,
        name: "王五",
        avatar: "/avatars/wangwu.jpg"
      },
      createTime: new Date("2024-01-10T11:30:00")
    },
    {
      id: 2,
      content: "关于 provide/inject 的部分还请详细解释一下...",
      author: {
        id: 4,
        name: "赵六",
        avatar: "/avatars/zhaoliu.jpg"
      },
      createTime: new Date("2024-01-10T13:45:00")
    }
  ])
  
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