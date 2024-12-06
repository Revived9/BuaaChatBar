<template>
    <div class="post-content">
      <!-- 主贴 -->
      <div id="floor-1" class="post-item main-post">
        <div class="post-meta">
          <div class="author-info">
            <img :src="post.avatar" :alt="post.username" class="avatar" />
            <span class="author-name">{{ post.username }}</span>
          </div>
          <div class="post-info">
            <span class="floor">1楼</span>
            <span class="time">{{ formatTime(post.post_time) }}</span>
          </div>
        </div>
        <div class="post-body" v-html="renderedContent"></div>
<!--        <div class="reply-button" @click="handleReply(1)">回复</div>-->
      </div>
  
      <!-- 回复列表 -->
      <div 
        v-for="(reply, index) in displayReplies" 
        :key="reply.id"
        :id="`floor-${index + 2}`"
        class="post-item reply"
      >
        <div class="post-meta">
          <div class="author-info">
            <img :src="reply.avatar" :alt="reply.username" class="avatar" />
            <span class="author-name">{{ reply.username }}</span>
          </div>
          <div class="post-info">
            <span class="floor">{{ index + 2 }}楼</span>
            <span class="time">{{ formatTime(reply.reply_time) }}</span>
          </div>
        </div>
        <div class="post-body" v-html="renderMarkdown(reply.content)"></div>
<!--        <div class="reply-button" @click="handleReply(index + 2)">回复</div>-->
      </div>
    </div>
  
    <!-- 二级回复对话框 -->
    <SecondaryReplyDialog
      v-if="showSecondaryReplyDialog"
      :postId="post.id"
      :replyToFloor="replyToFloor"
      :replyToUsername="getReplyToUsername(replyToFloor)"
      @close="closeSecondaryReplyDialog"
    />
  
    <!-- 一级回复对话框 -->
    <ReplyPostDialog 
      v-if="showReplyDialog"
      :postId="post.id"
      @close="closeReplyDialog"
    />
  
    <!-- 登录对话框 -->
    <LoginDialog
      v-if="showLoginDialog"
      @close="closeLoginDialog"
    />
  </template>
  
  <script setup>
  import { computed, ref } from 'vue'
  import { useStore } from 'vuex'
  import ReplyPostDialog from '@/components/dialogs/ReplyPostDialog.vue'
  import SecondaryReplyDialog from '@/components/dialogs/SecondaryReplyDialog.vue'
  import LoginDialog from '@/components/auth/LoginDialog.vue'

import { watch } from 'vue';
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'
// 导入默认样式 - 你也可以选择其他主题
import 'highlight.js/styles/github.css'

const md = new MarkdownIt({
  html: true,
  breaks: true,
  linkify: true,
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return '<pre class="hljs"><code>' +
               hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
               '</code></pre>';
      } catch (__) {}
    }
    // 使用默认的转义
    return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
  }
})

  const props = defineProps({
    post: {
      type: Object,
      required: true
    },
    replies: {
      type: Array,
      default: () => []
    },
    authorOnly: {
      type: Boolean,
      default: false
    }
  })

    watch(() => props.post, (newPost) => {
    console.log('post updated in PostContent:', newPost);
  });
  
  const displayReplies = computed(() => {
    if (props.authorOnly) {
      return props.replies.filter(reply => reply.author.id === props.post.author.id)
    }
    return props.replies
  })
  
  const formatTime = (date) => {
    return new Date(date).toLocaleString()
  }

  // 渲染主贴内容
  const renderedContent = computed(() => {
    return renderMarkdown(props.post.content)
  })

  // Markdown 渲染函数
  const renderMarkdown = (content) => {
    if (!content) return ''
    return md.render(content)
  }

  const store = useStore()
  const showReplyDialog = ref(false)
  const showSecondaryReplyDialog = ref(false)
  const showLoginDialog = ref(false)
  const replyToFloor = ref(null)

  const handleReply = (floor) => {
    if (!store.state.user.isLoggedIn) {
      showLoginDialog.value = true
      return
    }

    replyToFloor.value = floor
    if (floor === 1) {
      showReplyDialog.value = true
    } else {
      showSecondaryReplyDialog.value = true
    }
  }

  const closeReplyDialog = () => {
    showReplyDialog.value = false
  }

  const closeSecondaryReplyDialog = () => {
    showSecondaryReplyDialog.value = false
    replyToFloor.value = null
  }

  const closeLoginDialog = () => {
    showLoginDialog.value = false
  }

  // 添加获取被回复用户名的方法
  const getReplyToUsername = (floor) => {
    if (floor === 1) {
      return props.post.username
    }
    const reply = props.replies[floor - 2]
    return reply ? reply.username : '未知用户'
  }
  </script>
  
  <style scoped>
  .post-content {
    flex: 1;
    background: white;
    min-height: calc(100vh - 60px);
  }
  
  .post-item {
    padding: 32px 32px 48px;
    position: relative;
  }
  
  /* 为除了最后一个回复之外的所有回复添加分割线 */
  .post-item:not(:last-child)::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 32px;
    right: 32px;
    height: 1px;
    background-color: #f0f0f0;
  }
  
  .post-meta {
    display: flex;
    justify-content: space-between;
    margin-bottom: 16px;
  }
  
  .author-info {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
  
  .author-name {
    font-weight: 500;
    color: #333;
  }
  
  .post-info {
    color: #8c8c8c;
    font-size: 0.9rem;
    display: flex;
    gap: 12px;
  }
  
  .post-body {
    line-height: 1.8;
    color: #262626;
    font-size: 1rem;
    padding-left: 52px; /* 与头像对齐 */
  }
  
  .main-post {
    padding-top: 32px;
  }
  
  /* 移除主贴的背景色 */
  .main-post {
    background-color: transparent;
  }

  /* 添加 Markdown 样式 */
  .post-body :deep(h1) {
    font-size: 2em;
    margin: 0.67em 0;
  }

  .post-body :deep(h2) {
    font-size: 1.5em;
    margin: 0.83em 0;
  }

  .post-body :deep(h3) {
    font-size: 1.17em;
    margin: 1em 0;
  }

  .post-body :deep(p) {
    margin: 1em 0;
  }

  .post-body :deep(code) {
    background-color: #f5f5f5;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: monospace;
  }

  .post-body :deep(pre) {
    background-color: #f5f5f5;
    padding: 1em;
    border-radius: 5px;
    overflow-x: auto;
  }

  .post-body :deep(blockquote) {
    margin: 1em 0;
    padding-left: 1em;
    border-left: 4px solid #ddd;
    color: #666;
  }

  .post-body :deep(ul), .post-body :deep(ol) {
    padding-left: 2em;
    margin: 1em 0;
  }

  .post-body :deep(img) {
    max-width: 100%;
    height: auto;
  }

  .post-body :deep(a) {
    color: var(--primary-color);
    text-decoration: none;
  }

  .post-body :deep(a:hover) {
    text-decoration: underline;
  }

  .post-body :deep(table) {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
  }

  .post-body :deep(th), .post-body :deep(td) {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  .post-body :deep(th) {
    background-color: #f5f5f5;
  }

  /* 代码块样式优化 */
  .post-body :deep(pre.hljs) {
    background-color: #f6f8fa;
    border-radius: 6px;
    padding: 16px;
    overflow-x: auto;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    font-size: 14px;
    line-height: 1.45;
    margin: 1em 0;
  }

  .post-body :deep(pre.hljs code) {
    background-color: transparent;
    padding: 0;
    border-radius: 0;
    white-space: pre;
  }

  /* 行内代码样式 */
  .post-body :deep(:not(pre) > code) {
    background-color: rgba(175, 184, 193, 0.2);
    padding: 0.2em 0.4em;
    border-radius: 6px;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    font-size: 85%;
  }

  /* 代码块标题样式 */
  .post-body :deep(pre.hljs::before) {
    content: attr(data-lang);
    display: block;
    background-color: #e1e4e8;
    color: #24292e;
    padding: 4px 16px;
    margin: -16px -16px 16px -16px;
    border-radius: 6px 6px 0 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 12px;
    font-weight: 600;
  }

  /* 回复按钮样式 */
  .reply-button {
    position: absolute;
    right: 32px;
    bottom: 16px;
    padding: 6px 12px;
    border-radius: 4px;
    background-color: var(--primary-color);
    color: white;
    font-size: 0.9rem;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.2s;
  }

  .post-item:hover .reply-button {
    opacity: 1;
  }

  .reply-button:hover {
    background-color: #0056b3;
  }
  </style>