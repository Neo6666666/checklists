import axios from 'axios';
import router from "../../../router";

export default {
    create_list({commit, state}, {fileList, listId}){
        return new Promise((resolve, reject) => {
            commit('SET_LOADING_STATUS', true);
            state.list.id = parseInt(listId);
            state.list.created = new Date;
            state.list.updated = new Date;
            state.list.survey = parseInt(listId);
            state.list.user = state.user.id;
            state.list.photo = fileList;
            state.list.answers = [];
            for (let [key, value] of Object.entries(state.answers)) {
                state.list.answers.push({question: key, body: value});
            }
            commit('SET_LOADING_STATUS', false);
            axios({
                url: '/api/v1/response/',
                headers: {
                    Authorization: 'Token ' + state.token,
                },
                data: state.list,
                method: 'POST'
            }).then(response => {
                const list = response.data;
                localStorage.setItem('list', list);
                commit('SET_LIST', list);
                resolve(response);
                router.push('/')
            }).catch(error => {
                console.log(error);
                reject(error)
            })
        })
    },
    list({commit, state}, list_id) {
        return new Promise((resolve, reject) => {
            commit('SET_LOADING_STATUS', true);
            axios({
                url: '/api/v1/lists/' + list_id + '/',
                headers: {
                    Authorization: 'Token ' + state.token,
                },
                method: 'GET'
            }).then(response => {
                commit('SET_LOADING_STATUS', false);
                const list = response.data;
                localStorage.setItem('list', list);
                commit('SET_LIST', list);
                resolve(response)
            }).catch(error => {
                console.log(error);
                reject(error)
            })
        })
    },
    lists({commit, state}) {
        return new Promise((resolve, reject) => {
            commit('SET_LOADING_STATUS', true);
            axios({
                url: '/api/v1/lists/',
                headers: {
                    Authorization: 'Token ' + state.token,
                },
                method: 'GET'
            }).then(response => {
                commit('SET_LOADING_STATUS', false);
                const lists = response.data;
                localStorage.setItem('lists', lists);
                commit('SET_LISTS', lists);
                resolve(response)
            }).catch(error => {
                console.log(error);
                reject(error)
            })
        })
    }
}
