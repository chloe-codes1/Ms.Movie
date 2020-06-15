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
    reviews: [],
    id: null,
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: state => ({headers: { Authorization: `Token ${state.authToken}` }}),
  },
  mutations:{
    SET_TOKEN(state, token){
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_MOVIES(state, movies){
      state.movies = movies
    },
    SET_REVIEWS(state, reviews){
      state.reviews = reviews
    },
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
    signup({ dispatch }, signupData){
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup
      }
      dispatch('postAuthData', info) // 인자 하나만 넘길 수 있어서 info 로 묶음
    },
    // 첫번째 인자로 context가 들어오는데 그 중 dispatch 사용할거라서 { dispatch } => de-structuring!
    login( { dispatch }, loginData){
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login
      }
      dispatch('postAuthData', info)
    },
    logout({ getters, commit }){
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config ) // 데이터는 없어도 되지만 header가 필요함
        .then( ()=> { //Django DB에서는 삭제되어 있음 but, cookie, state에는 남아있음
          // cookies.remove가 null 뒤에 들어가야함!
          commit('SET_TOKEN',null)  // commit은 state 를 바꿀 수 있는 유일한 방법!!! -> state 에서도 삭제
          cookies.remove('auth-token') //cookie 에서는 삭제
          router.push({name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
    },
    fetchMovies({ commit} ) {
      axios.get( SERVER.URL + SERVER.ROUTES.movieList)
        .then(response => commit('SET_MOVIES', response.data))
        .catch(err => console.log(err))
    },
    // ReviewList
    getReviews({commit}, id) {
      axios.get(SERVER.URL +`/reviews/${id}/`)
        .then(response => commit('SET_REVIEWS', response.data))
        .catch(err => console.log(err))       
    },
    createReview( {getters}, id, reviewData ) {
      axios.post(SERVER.URL + `/reviews/${id}/`, reviewData, getters.config)
        .then(() => {
          router.push(`/reviews/${id}/`)
        })
        .catch(err => console.log(err))
    },
    // Detail
    getReview( { commit }, info ) {
      axios.get(SERVER.URL + SERVER.ROUTES.reviewDetail + info)
        .then(response => commit('SET_REVIEWS', response.data))
        .catch(err => console.log(err))
    },
  },
  modules: {
  }
})