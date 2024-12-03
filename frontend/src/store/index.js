import { createStore } from 'vuex'
import theme from './modules/theme'
import user from './modules/user'

export default createStore({
  modules: {
    theme,
    user
  }
})
