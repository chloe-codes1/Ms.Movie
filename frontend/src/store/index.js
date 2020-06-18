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

    recommendations: [],
    
    reviews: [],
    likeCount: null,
    dislikeCount: null,
    userId: cookies.get('user'),
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: () => ({headers: { Authorization: `Token ${cookies.get('auth-token')}` }}),
    id: () => ({user: cookies.get('user')}),
    movies: state => state.movies
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
    SET_RECOMMENDSTIONS(state, recommendations){
      state.recommendations = recommendations
    },
    SET_MOVIE(state, movie){
      state.starredMovie = movie
    },
    SET_REVIEWS(state, reviews){
      state.reviews = reviews
      state.likeCount = reviews.likes
      state.dislikeCount = reviews.dislikes
    },
    SET_USER_ID(state, id) {
      cookies.set('user', id) 
    },
    SET_LIKE(state, like) {
      state.likeCount = like
    },
    SET_DISLIKE(state, dislike) {
      state.dislikeCount = dislike
    },
    SET_PAGE(state, movie) {
      state.movies.push(movie)
    }

  },
  actions: { 
    
    postAuthData({ commit }, info){
      axios.post(SERVER.URL + info.location, info.data)
      .then(res => {
        console.log(res.data, 'res.data')
        commit('SET_TOKEN', res.data.key)
        commit('SET_USER_ID', res.data.user)
        if (info.location == SERVER.ROUTES.signup){
          router.push({ name: 'CreateProfile' })
        }
        else {
          router.push({ name: 'Movies'})
        }
      })
      .catch(
        err => { 
          console.log(err.response.data)
          alert(Object.values(err.response.data)[0])
        }
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
          commit('SET_USER_ID', [])
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
    createProfile({getters}, favorite) {
      axios.post(SERVER.URL + SERVER.ROUTES.profile, favorite, getters.config)
        .then( () => {
          router.push('/')
        })
        .catch( err => console.log(err.response.data))
    },
    getOthersAccount({ commit }, id ) {
      axios.get(SERVER.URL + SERVER.ROUTES.othersProfile + `${id}/`)
        .then(response => {
          commit('SET_OTHERS_ACCOUNT', response.data)
        })
        .catch(err => console.log(err.response.data))
    },
    fetchMovies({ commit}, params ) {
      axios.get( SERVER.URL + SERVER.ROUTES.movieList, {...params})
        .then(response => commit('SET_MOVIES', response.data))
        .catch(err => console.log(err))
    },
    fetchRecommendation({commit, getters}){
      const user_pk = parseInt(getters.id['user'])
      axios.get( SERVER.URL + SERVER.ROUTES.movieRecommendation+ user_pk +'/')
        .then( response => commit('SET_RECOMMENDSTIONS', response.data))
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
    getReview( { commit }, data ) {
      axios.get(SERVER.URL + `/reviews/${data.movie}/detail/${data.id}`)
        .then(response => commit('SET_REVIEWS', response.data))
        .catch(err => console.log(err))
    },
    updateReview( {getters}, data) {
      
      console.log(data)
      axios.put(SERVER.URL + `/reviews/${data.movie}/detail/${data.id}/`, data.reviewData, getters.config)
        .then(() => {
          router.push(`/reviews/${data.movie}/detail/${data.id}/`)
        })
        .catch(err => console.log(err))
    },
    deleteReview( {getters}, data) {
      console.log(data)
      axios.delete(SERVER.URL + `/reviews/${data.movie}/detail/${data.id}/`, getters.config)
        .then(() => {
          router.push(`/reviews/${data.movie}`)
        })
    },
    // Comment 
    createComment( {getters}, data ) {
      axios.post(SERVER.URL + `/reviews/${data.id}/comments/`, data.commentData, getters.config)
      .then(() => {
        router.history.go(0)
      })
    },
    updateComment( {getters}, data ) {
      axios.put(SERVER.URL + `/reviews/${data.review_id}/comments/${data.comment_id}`, data.commentData, getters.config)
        .then(() => {
          router.history.go(0)
        })
    },
    deleteComment( {getters}, data ) {
      console.log(data)
      axios.delete(SERVER.URL + `/reviews/${data.review}/comments/${data.comment}`, getters.config)
        .then(() => {
        router.history.go(0)
        })
    },
    likeReview( {getters, commit}, data) {
      axios.put(SERVER.URL + `/reviews/${data}/like/`, getters.id)
        .then( (res) => {
          const likeThumb = document.querySelector('#likeThumb')
          if (res.data.liked_users.includes(Number(getters.id.user))) { 
            likeThumb.classList.add('fas')
            likeThumb.classList.remove('far')
          }
          else {
            likeThumb.classList.add('far')
            likeThumb.classList.remove('fas')
          }
          commit('SET_LIKE', res.data.liked_users.length)
        })
    },
    dislikeReview( {getters, commit}, data) {
      axios.put(SERVER.URL + `/reviews/${data}/dislike/`, getters.id)
        .then( (res) => {
          const dislikeThumb = document.querySelector('#dislikeThumb')
          if (res.data.disliked_users.includes(Number(getters.id.user))) { 
            dislikeThumb.classList.add('fas')
            dislikeThumb.classList.remove('far')
          }
          else {
            dislikeThumb.classList.add('far')
            dislikeThumb.classList.remove('fas')
          }
          commit('SET_DISLIKE', res.data.disliked_users.length)
        })
    },
    //paginations
    setPage({commit}, id) {
      axios.get(SERVER.URL + `/movies/${id}`)
        .then(res => {
          commit('SET_PAGE', res.data)
        })
    }
    

  },
  modules: {
  }
})