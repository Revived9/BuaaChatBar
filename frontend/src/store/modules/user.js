import { getUserProfile } from '@/services/api'

export default {
  namespaced: true,
  state: {
    isLoggedIn: false,
    studentId: null,
    username: null,
    avatar: null,
    bio: null
  },
  mutations: {
    setLoginStatus(state, status) {
      state.isLoggedIn = status
    },
    setCurrentUser(state, userData) {
      state.username = userData.username
      state.avatar = userData.avatar
      state.studentId = userData.studentId
      state.bio = userData.bio
    },
    setUsername(state, newUsername) {
      state.username = newUsername;
      const userInfo = JSON.parse(localStorage.getItem('userInfo') || '{}');
      userInfo.username = newUsername;
      localStorage.setItem('userInfo', JSON.stringify(userInfo));
    },
    clearUserData(state) {
      state.isLoggedIn = false
      state.username = null
      state.avatar = null
      state.studentId = null
    },
    SET_AVATAR(state, avatarUrl) {
      state.avatar = avatarUrl
      const userInfo = JSON.parse(localStorage.getItem('userInfo') || '{}')
      userInfo.avatar = avatarUrl
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
    }
  },
  actions: {
    setLoginStatus({ commit }, status) {
      commit('setLoginStatus', status)
    },
    setCurrentUser({ commit }, userData) {
      commit('setCurrentUser', userData)
    },
    updateUsername({ commit }, newUsername) {
      commit('setUsername', newUsername);
    },
    logout({ commit }) {
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
      commit('clearUserData')
    },
    async initUserState({ commit }) {
      const token = localStorage.getItem('token')
      if (token) {
        try {
          commit('setLoginStatus', true)
          const userInfo = JSON.parse(localStorage.getItem('userInfo') || '{}')
          if (userInfo.username) {
            commit('setCurrentUser', userInfo)
          }
        } catch (error) {
          console.error('初始化用户状态失败:', error)
          commit('clearUserData')
          localStorage.removeItem('token')
          localStorage.removeItem('userInfo')
        }
      }
    },
    updateAvatar({ commit }, avatarUrl) {
      commit('SET_AVATAR', avatarUrl)
    }
  }
}
