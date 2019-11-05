import axios from 'axios';
import ApiService from "@/services/api.js";
import types from "@/store/types/reports.js"

export default {
    [types.FETCH_REPORT]({commit, state},  report_id) {
        return new Promise((resolve, reject) => {
            commit('SET_LOADING_STATUS', true);
            ApiService.get("api/v1/report", report_id)
                .then(response => {
                    commit('SET_LOADING_STATUS', false);
                    const report = response.data;
                    localStorage.setItem('report', report);
                    commit('SET_REPORT', report);
                    resolve(response)
                }).catch(error => {
                    console.log(error);
                    reject(error)
                })
        })
    },
    [types.FETCH_REPORTS]({commit, state}) {
        return new Promise((resolve, reject) => {
            commit("SET_LOADING_STATUS", true);
            ApiService.setHeader();
            ApiService.get("api/v1/reports")
                .then(response => {
                    commit("SET_LOADING_STATUS", false);
                    const reports = response.data;
                    localStorage.setItem('reports', reports);
                    commit("SET_REPORTS", reports);
                    resolve(response)
                }).catch(error => {
                    console.log(error);
                    reject(error)
                })
        })
    },
}
