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

    account: null,
    othersAccount: null,
    
    movies: [],
    starredMovie: null,
    
    reviews: [],
    id: null,
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: () => ({headers: { Authorization: `Token ${cookies.get('auth-token')}` }}),
  }, 
  mutations:{ 
    SET_TOKEN(state, token){
      state.authToken = token
      cookies.set('auth-token', token) 
    }, 
    SET_ACCOUNT(state, user){
      state.account = user
    },
    SET_OTHERS_ACCOUNT(state, user){
      state.othersAccount = user
    },
    SET_MOVIES(state, movies){
      state.movies = movies
    },
    SET_MOVIE(state, movie){
      state.starredMovie = movie
    },
    SET_REVIEWS(state, reviews){
      state.reviews = reviews
    },
  },
  actions: { 
    postAuthData({ commit }, info){
      axios.post(SERVER.URL + info.location, info.data)
      .then(res => {
        console.log(res.data, 'res.data')
        commit('SET_TOKEN', res.data.key)
        router.push({ name: 'Home'})
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
      dispatch('postAuthData', info) 
    },
    login( { dispatch }, loginData){
      const info = {  
        data: loginData,  
        location: SERVER.ROUTES.login
      }       
      console.log('info', info);
      dispatch('postAuthData', info)
    },
    logout({ commit }){
      axios.get(SERVER.URL + SERVER.ROUTES.logout) // 데이터는 없어도 되지만 header가 필요함
        .then( ()=> { //Django DB에서는 삭제되어 있음 but, cookie, state에는 남아있음
          // cookies.remove가 null 뒤에 들어가야함!
          commit('SET_TOKEN', null)  // commit은 state 를 바꿀 수 있는 유일한 방법!!! -> state 에서도 삭제
          cookies.remove('auth-token') //cookie 에서는 삭제
          router.push('/')
        })
        .catch(err => console.log(err.response.data))
    },
    getAccount({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.profile)
        .then(response => {
          commit('SET_ACCOUNT', response.data)
        })
        .catch(err => console.log(err.response.data))
    },
    getOthersAccount({ commit }, id ) {
      axios.get(SERVER.URL + SERVER.ROUTES.othersProfile + `${id}/`)
        .then(response => {
          commit('SET_OTHERS_ACCOUNT', response.data)
        })
        .catch(err => console.log(err.response.data))
    },
    fetchMovies({ commit} ) {
      axios.get( SERVER.URL + SERVER.ROUTES.movieList)
        .then(response => commit('SET_MOVIES', response.data))
        .catch(err => console.log(err))
    },
    fetchMovie({ commit }, id){
      axios.get(SERVER.URL + SERVER.ROUTES.movieList + id)
        .then(response => commit('SET_MOVIE',response.data))
    },
    // ReviewList
    getReviews({commit}, id) {
      axios.get(SERVER.URL +`/reviews/${id}/`)
        .then(response => commit('SET_REVIEWS', response.data))
        .catch(err => console.log(err))       
    },
    createReview( {getters}, data) {
      console.log(cookies.get('auth-token'));
      console.log(getters.config) 
      axios.post(SERVER.URL + `/reviews/${data.id}/`, data.reviewData, getters.config)
        .then(() => {
          router.push(`/reviews/${data.id}/`)
        })
        .catch(err => console.log(err))
    },
    // Detail
    getReview( { commit }, info ) {
      axios.get(SERVER.URL + `/reviews/detail/` + info)
        .then(response => commit('SET_REVIEWS', response.data))
        .catch(err => console.log(err))
    },
    // get Comment list


    // Comment Create
    createComment( {getters}, data ) {
      axios.post(SERVER.URL + `/reviews/${data.id}/comments/`, data.commentData, getters.config)
      .then(() => {
        router.history.go(0)
      })
    }
  },
  modules: {
  }
})