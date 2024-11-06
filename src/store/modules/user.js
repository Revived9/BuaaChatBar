import { getUserProfile } from '@/services/api'

export default {
  namespaced: true,
  state: {
    currentUser: null,
  },
  mutations: {
    SET_CURRENT_USER(state, user) {
      state.currentUser = user
    },
  },
  actions: {
    async getUserInfo({ commit }, studentId) {
      try {
        const response = await getUserProfile(studentId)
        commit('SET_CURRENT_USER', response.data)
        return response.data
      } catch (error) {
        console.error('获取用户信息失败:', error)
        throw error
      }
    },
  },
}
