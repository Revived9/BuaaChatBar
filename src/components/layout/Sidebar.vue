<script setup>
import { h } from 'vue';

// 定义 SVG 图标组件
const Icon = ({ path }) => h('svg', { 
  xmlns: 'http://www.w3.org/2000/svg', 
  viewBox: '0 0 24 24', 
  fill: 'currentColor', 
  width: '1em', 
  height: '1em' 
}, [h('path', { d: path })]);

// 定义各个图标的路径
const icons = {
  comments: 'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10z',
  book: 'M12 21V5c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2v-7h-10v9zm0-11h8V7h-8v3z',
  users: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5z',
  bell: 'M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z'
};
</script>

<template>
  <aside class="sidebar">
    <button class="new-topic-btn">发布主题</button>
    <nav class="sidebar-nav">
      <h3>板块</h3>
      <ul>
        <li>
          <a href="#">
            <Icon :path="icons.comments" />
            <span>综合讨论</span>
          </a>
        </li>
        <li>
          <a href="#">
            <Icon :path="icons.book" />
            <span>学习交流</span>
          </a>
        </li>
        <li>
          <a href="#">
            <Icon :path="icons.users" />
            <span>校园生活</span>
          </a>
        </li>
        <li>
          <a href="#">
            <Icon :path="icons.bell" />
            <span>活动公告</span>
          </a>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 200px;
  padding: 0 20px; /* 移除顶部内边距 */
  background-color: #fff;
  flex-shrink: 0;
}

.new-topic-btn {
  width: 100%;
  padding: 10px;
  height: 40px;
  line-height: 20px;
  background-color: var(--primary-color);
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  margin: 20px 0; /* 改为上下margin */
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.new-topic-btn:hover {
  background-color: #1a7ee6;
}

.sidebar-nav h3 {
  font-size: 1rem;
  color: var(--text-color);
  margin-bottom: 10px;
}

.sidebar-nav ul {
  list-style-type: none;
  padding: 0;
}

.sidebar-nav li {
  margin-bottom: 10px;
}

.sidebar-nav a {
  color: var(--text-color);
  text-decoration: none;
  display: flex;
  align-items: center;
  padding: 5px 0;
  transition: color 0.2s;
}

.sidebar-nav a:hover {
  color: var(--primary-color);
}

.sidebar-nav a svg {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

@media (max-width: 1024px) {
  .sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid var(--border-color);
  }
}
</style>
