<template>
    <div class="post-content">
      <!-- 主贴 -->
      <div id="floor-1" class="post-item main-post">
        <div class="post-meta">
          <div class="author-info">
            <img :src="post.author.avatar" :alt="post.author.name" class="avatar" />
            <span class="author-name">{{ post.author.name }}</span>
          </div>
          <div class="post-info">
            <span class="floor">1楼</span>
            <span class="time">{{ formatTime(post.createTime) }}</span>
          </div>
        </div>
        <div class="post-body" v-html="renderMarkdown(post.content)">
        </div>
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
            <img :src="reply.author.avatar" :alt="reply.author.name" class="avatar" />
            <span class="author-name">{{ reply.author.name }}</span>
          </div>
          <div class="post-info">
            <span class="floor">{{ index + 2 }}楼</span>
            <span class="time">{{ formatTime(reply.createTime) }}</span>
          </div>
        </div>
        <div class="post-body" v-html="renderMarkdown(reply.content)">
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import MarkdownIt from 'markdown-it'
  import hljs from 'highlight.js'
  import 'highlight.js/styles/github.css' // 可以选择其他主题，比如 'atom-one-dark.css'
  
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
  
  const displayReplies = computed(() => {
    if (props.authorOnly) {
      return props.replies.filter(reply => reply.author.id === props.post.author.id)
    }
    return props.replies
  })
  
  const formatTime = (date) => {
    return new Date(date).toLocaleString()
  }
  
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
      return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
    }
  })
  
  // 修改 markdown 渲染函数
  const renderMarkdown = (content) => {
    return md.render(content || '')
  }
  </script>
  
  <style scoped>
  .post-content {
    flex: 1;
    background: white;
    min-height: calc(100vh - 60px);
  }
  
  .post-item {
    padding: 24px 32px;
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
  
  /* 添加 markdown 样式 */
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
  
  /* 修改代码块样式 */
  .post-body :deep(pre.hljs) {
    background-color: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;
    font-size: 14px;
    line-height: 1.45;
    margin: 1em 0;
  }
  
  .post-body :deep(pre.hljs code) {
    background-color: transparent;
    padding: 0;
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
  </style>