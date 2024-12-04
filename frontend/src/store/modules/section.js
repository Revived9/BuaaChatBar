// section.js

export default {
    namespaced: true,

    state: {
        currentSection: 'all', // 默认值
    },
    mutations: {
        setCurrentSection(state, sectionId) {
            state.currentSection = sectionId;
        },
    },
    actions: {
        async updateCurrentSection({ commit }, sectionId) {
            // 这里可以进行异步操作，比如请求数据
            commit('setCurrentSection', sectionId);
        }
    }
}