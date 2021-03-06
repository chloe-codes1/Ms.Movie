import Cast from '@/views/movies/Cast.vue'
import CreateProfile from '@/views/accounts/CreateProfile.vue'
import Home from '@/views/Home.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import Movies from '@/views/movies/Movies.vue'
import Profile from '@/views/accounts/Profile.vue'
import ReviewCreate from '@/views/reviews/ReviewCreate.vue'
import ReviewDetailView from '@/views/reviews/ReviewDetailView.vue'
import ReviewListCreate from '@/views/reviews/ReviewListCreate.vue'
import ReviewUpdate from '@/views/reviews/ReviewUpdate.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

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
    path: '/cast',
    name: 'Cast',
    component: Cast,
    meta: {
      title: 'Ms.Movie | Cast'
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
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView,
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
    path: '/accounts/favorite',
    name: 'CreateProfile',
    component: CreateProfile
  },
  {
    path: '/accounts/:id',
    name: 'Profile',
    component: Profile
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
    path: '/reviews/:id/create',
    name: 'ReviewCreate',
    component: ReviewCreate,
    meta: {
      title: 'Ms.Movie | Write a review'
    }
  },
  {
    path: '/reviews/:movieId/detail/:id',
    name: 'ReviewDetailView',
    component: ReviewDetailView,
  },
  {
    path: '/reviews/:movieId/detail/:id/update',
    name: 'ReviewUpdate',
    component: ReviewUpdate,
    meta: {
      title: 'Ms.Movie | Update a review'
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// title & authorization 처리 ^^
router.beforeEach((to, from, next) => {

  // title 설정하기 ^^
  document.title = to.meta.title || 'Ms. Movie';

    const isAuthenticated = store.getters.isLoggedIn;

    if (isAuthenticated) {
      next()
    } else if(to.name === 'LoginView' || to.name === 'SignupView') {
      next()
    } else { 
    next({name: 'LoginView'})
    }

  });

export default router
