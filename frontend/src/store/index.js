//index.js
import { createStore } from 'vuex'
import theme from './modules/theme'
import user from './modules/user'
import section from './modules/section';

export default createStore({
  modules: {
    theme,
    user,
    section
  }
})