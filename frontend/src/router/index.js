import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Movies from '@/views/movies/Movies.vue'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'

import ReviewListCreate from '@/views/reviews/ReviewListCreate.vue'
import ReviewDetailView from '@/views/reviews/ReviewDetailView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies,
    meta: {
      title: 'Ms.Move | Movies'
    }
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView,
    meta: {
      title: 'Sign In'
    }
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView,
    meta: {
      title: 'Sign Up'
    }
  },
  {
    path: '/reviews/:id',
    name: 'ReviewListCreate',
    component: ReviewListCreate,
    meta: {
      title: 'Ms.Movie | Reviews'
    }
  },
  
  {
    path: '/reviews/detail/:id',
    name: 'ReviewDetailView',
    component: ReviewDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Ms. Movie';
  next()
})
export default router
