import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import router from '@/router'
import axios from 'axios'
import SERVER from '@/api/drf'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    movies: [],
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: state => ({headers: { Authorization: `Token ${state.authToken}` }})
  },
  mutations:{
    SET_TOKEN(state, token){
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_MOVIES(state, movies){
      state.movies = movies
    }
  },
  actions: {
    postAuthData({ commit }, info){
      axios.post(SERVER.URL + info.location, info.data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        router.push({ name: 'Home '})
      })
      .catch(
        err => console.log(err.response.data)
      )
    },
    // signup({ dispatch }, signupData)
  },
  modules: {
  }
})
