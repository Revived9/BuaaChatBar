export default {
  namespaced: true,
  
  state: {
    themeColor: '#1890FF', // 默认主题色
    welcomeMessage: '欢迎来到论坛' // 默认欢迎语
  },

  mutations: {
    setThemeColor(state, color) {
      state.themeColor = color
      // 更新 CSS 变量
      document.documentElement.style.setProperty('--primary-color', color)
      // 生成 RGB 值用于透明度
      const rgb = hexToRgb(color)
      document.documentElement.style.setProperty('--primary-color-rgb', `${rgb.r}, ${rgb.g}, ${rgb.b}`)
    },
    
    setWelcomeMessage(state, message) {
      state.welcomeMessage = message
    }
  }
}

// 辅助函数：将十六进制颜色转换为 RGB
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex)
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null
} 