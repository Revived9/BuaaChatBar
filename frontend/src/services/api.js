import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/', // 替换为实际的后端 API 地址
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
// export const login = (credentials) => {
//   return new Promise((resolve, reject) => {
//     setTimeout(() => {
//       if (credentials.studentId === '123' && credentials.password === '123456') {
//         const userData = {
//           studentId: '123',
//           username: 'Nameless9',
//           avatar: '/src/assets/profile.png'
//         }

//         resolve({
//           data: {
//             code: 1,
//             token: 'fake-jwt-token',
//             user: userData,
//             message: '登录成功'
//           }
//         });
//       } else {
//         reject({
//           data: {
//             code: 0,
//             message: '学号或密码错误'
//           }
//         });
//       }
//     }, 1000);
//   });
// };

//登录函数
export const login = async (userData) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/Login', JSON.stringify(userData), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD login');
  }
}

//注册函数
export const register = async (userData) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/Register', JSON.stringify(userData), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD register');
  }
}

//修改密码
export const passwordmodify = async (password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/PasswordModify', JSON.stringify(password), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD password modify');
  }
}

//修改邮箱
export const emailmodify = async (email) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/EmailModify', JSON.stringify(email), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD emailmodify');
  }
}

//修改用户名
export const usernamemodify = async (username) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/UsernameModify', JSON.stringify(username), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD usernamemodify');
  }
}

//修改用户头像
// 使用 FormData 发送文件
export const avatermodify = async (avater) => {
  const formData = new FormData();
  formData.append('avatar', avater); // 'avatar' 是后端接收文件的字段名
  try {
    const response = await axios.post('http://127.0.0.1:8000/AvaterModify', formData, {
      headers: {
        'Content-Type': 'multipart/form-data' // 设置请求头，指示请求体类型
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD avatermodify');
  }
}

//修改简介
export const biomodify = async (bio) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/BioModify', JSON.stringify(bio), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD biomodify');
  }
}

//发布帖子
// export const createpost = async (post) => {
//   try {
//     const response = await axios.post('http://127.0.0.1:8000/CreatePost', post, {
//       headers: {
//         'Content-Type': 'multipart/form-data'
//       }
//     });
//     return response;
//   } catch (error) {
//     throw new Error('BAD createpost');
//   }
// }

// 发布帖子
export const createpost = async (post) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/CreatePost', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'  // 这里改成 JSON 格式
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD createpost');
  }
}


//删除帖子
export const deletepost = async (post) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/DeletePost', JSON.stringify(bio), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD deletepost');
  }
}

//查看帖子列表（全部）
export const getallpost = async (post) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/GetAllPost', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD getallpost');
  }
}

//查看帖子列表（标签）
export const gettagpost = async (post) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/GetTagPost', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD gettagpost');
  }
}

//查看帖子
export const getsinglepost = async (post) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/GetSinglePost', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD getsinglepost');
  }
}

//发布评论
export const comment = async (comment) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/Comment', JSON.stringify(comment), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD comment');
  }
}

//发布二级评论
export const secondcomment = async (secondcomment) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/SecondComment', JSON.stringify(secondcomment), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD secondcomment');
  }
}

//收藏帖子
export const collectpost = async (collectpost) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/CollectPost', JSON.stringify(secondcommentcollectpost), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD collectpost');
  }
}

//帖子置顶
export const toppost = async (toppost) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/TopPost', JSON.stringify(toppost), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD toppost');
  }
}

//添加标签
export const createtag = async (createtag) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/CreateTag', JSON.stringify(createtag), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD createtag');
  }
}

//删除标签
export const deletetag = async (deletetag) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/DeleteTag', JSON.stringify(createtag), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD deletetag');
  }
}

//给帖子添加标签
export const addtagtopost = async (addtagtopost) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/AddTagToPost', JSON.stringify(addtagtopost), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD addtagtopost');
  }
}

//给帖子删除标签
export const deteletagtopost = async (deteletagtopost) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/DeleteTagToPost', JSON.stringify(deteletagtopost), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD deteletagtopost');
  }
}

//搜索帖子
export const searchpost = async (searchpost) => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/SearchPost', JSON.stringify(searchpost), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD searchpost');
  }
}

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
