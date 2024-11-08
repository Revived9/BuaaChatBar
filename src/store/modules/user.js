import { getUserProfile } from '@/services/api'

export default {
  namespaced: true,
  state: {
    isLoggedIn: false,
    studentId: null,
    username: null,
    avatar: null
  },
  mutations: {
    setLoginStatus(state, status) {
      state.isLoggedIn = status
    },
    setCurrentUser(state, userData) {
      state.username = userData.username
      state.avatar = userData.avatar
      state.studentId = userData.studentId
    },
    clearUserData(state) {
      state.isLoggedIn = false
      state.username = null
      state.avatar = null
      state.studentId = null
    }
  },
  actions: {
    setLoginStatus({ commit }, status) {
      commit('setLoginStatus', status)
    },
    setCurrentUser({ commit }, userData) {
      commit('setCurrentUser', userData)
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
    }
  }
}
