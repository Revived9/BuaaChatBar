import { createStore } from 'vuex'

export default createStore({
  state: {
    user: JSON.parse(localStorage.getItem('user')) || {
      isLoggedIn: false,
      username: '',
      avatar: '',
      studentId: '',
      email: '',
      registrationDate: ''
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = { ...state.user, ...user, isLoggedIn: true }
      localStorage.setItem('user', JSON.stringify(state.user))
    },
    clearUser(state) {
      state.user = { isLoggedIn: false, username: '', avatar: '', studentId: '', email: '', registrationDate: '' }
      localStorage.removeItem('user')
    }
  },
  actions: {
    setUser({ commit }, user) {
      commit('setUser', user)
    },
    logout({ commit }) {
      commit('clearUser')
      localStorage.removeItem('token')
    }
  },
  modules: {
    // 如果有其他模块，可以在这里添加
  }
})
