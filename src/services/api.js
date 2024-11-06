import axios from 'axios';

const api = axios.create({
  baseURL: 'http://your-backend-api-url', // 替换为实际的后端 API 地址
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// 请求拦截器，用于添加认证令牌
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// 响应拦截器，用于处理错误
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // 处理错误，例如显示错误消息、重定向到登录页等
    console.error('API Error:', error.response);
    return Promise.reject(error);
  }
);

export default api;

// 模拟登录函数
export const login = (credentials) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (credentials.studentId === '123' && credentials.password === '123456') {
        resolve({
          data: {
            token: 'fake-jwt-token',
            user: {
              studentId: '123',
              username: '测试用户',
              avatar: 'https://example.com/avatar.jpg'
            }
          }
        });
      } else {
        reject({ message: '学号或密码错误' });
      }
    }, 1000); // 模拟网络延迟
  });
};

export const register = (userData) => api.post('/auth/register', userData);

export const getPosts = (params) => api.get('/posts', { params });

export const createPost = (postData) => api.post('/posts', postData);

export const getPostById = (postId) => api.get(`/posts/${postId}`);

export const updatePost = (postId, postData) => api.put(`/posts/${postId}`, postData);

export const deletePost = (postId) => api.delete(`/posts/${postId}`);

export const addComment = (postId, commentData) => api.post(`/posts/${postId}/comments`, commentData);

export const getUserProfile = (studentId) => {
  return api.get(`/users/${studentId}`)
};

export const updateUserProfile = (userData) => api.put('/user/profile', userData);
