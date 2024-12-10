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
export const avatermodify = async (avater) => {
  const formData = new FormData();
  formData.append('user_id', avater.user_id);
  formData.append('new_avatar',avater.new_avatar);
  formData.append('image',avater.image);
  try {
    const response = await axios.post('http://127.0.0.1:8000/AvaterModify', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response;
  } catch (error) {
    throw new Error('头像上传失败');
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

// 发布帖子
export const createpost = async (post) => {
  const formData = new FormData();
  formData.append('content',post.content)
  formData.append('user_id', post.user_id);
  formData.append('section', post.section);
  formData.append('title',post.title);

  // 处理文件数组，确保每个文件都被正确附加到 FormData
  post.image.forEach((file, index) => {
    formData.append('image[]', file); // 使用相同字段名 "image[]" 以便后端能够识别为多个文件
  });
  try {
    console.log(formData)
    const response = await axios.post('http://127.0.0.1:8000/CreatePost', formData, {
      headers: {
        'Content-Type': 'multipart/form-data' // 设置请求头，指示请求体类型
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
    const response = await axios.post('http://127.0.0.1:8000/DeletePost', JSON.stringify(post), {
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
    console.log(post)
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

export const getpersonpost = async (post) => {
  try {
    //console.log(post)
    const response = await axios.post('http://127.0.0.1:8000/GetPersonPost', JSON.stringify(post), {
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
    const response = await axios.post('http://127.0.0.1:8000/GetSinglePost', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error(error);
  }
}

//发布评论
export const reply = async (reply) => {
  const formData = new FormData();
  formData.append('content',reply.content)
  formData.append('user_id', reply.user_id);
  formData.append('post_id', reply.post_id);
  // 处理文件数组，确保每个文件都被正确附加到 FormData
  reply.image.forEach((file, index) => {
    formData.append('image[]', file); // 使用相同字段名 "image[]" 以便后端能够识别为多个文件
  });
  try {
    console.log(formData)
    const response = await axios.post('http://127.0.0.1:8000/Comment', formData, {
      headers: {
        'Content-Type': 'multipart/form-data' // 设置请求头，指示请求体类型
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD comment');
  }
}

export const getallreplies = async (post) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/GetAllReplies', JSON.stringify(post), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('BAD getallpost');
  }
}

// 使用获取经验榜单
export const fetchUsers = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/GetUsers')
    return response;
  } catch (error) {
    console.error('获取用户数据失败:', error)
  }
}

// //发布二级评论
// export const secondcomment = async (secondcomment) => {
//   try {
//     const response = await axios.get('http://127.0.0.1:8000/SecondComment', JSON.stringify(secondcomment), {
//       headers: {
//         'Content-Type': 'application/json'
//       }
//     });
//     return response;
//   } catch (error) {
//     throw new Error('BAD secondcomment');
//   }
// }

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

// 获取用户头像
export const getUserAvatar = async (userId) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/GetUserAvatar', 
      JSON.stringify({ user_id: userId }), {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response;
  } catch (error) {
    throw new Error('获取用户头像失败');
  }
}
