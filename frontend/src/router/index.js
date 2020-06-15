import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Movies from '@/views/movies/Movies.vue'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'

import ReviewListView from '@/views/reviews/ReviewListView.vue'
import ReviewCreateView from '@/views/reviews/ReviewCreateView.vue'
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
      title: 'Ms.Movie | Movies'
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
    path: '/reviews',
    name: 'ReviewListView',
    component: ReviewListView,
    meta: {
      title: 'Ms.Movie | Reviews'
    }
  },
  {
    path: '/reviews/create',
    name: 'ReviewCreateView',
    component: ReviewCreateView,
    meta: {
      title: 'Ms.Movie | Write a review'
    }
  },
  {
    path: '/reviews/:id',
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
