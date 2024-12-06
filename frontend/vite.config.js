import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      },
      '/upload': {  // 这部分配置要在 proxy 下面
        target: 'https://sm.ms',
        changeOrigin: true,
        pathRewrite: { '^/upload': '/upload' }, // 这里将 `/upload` 重写成空路径，代理到 https://sm.ms
      },
    }
  },
  base: '/',
})