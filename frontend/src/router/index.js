import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import ReviewListView from '../views/reviews/ReviewListView.vue'
import ReviewCreateView from '../views/reviews/ReviewCreateView.vue'
import ReviewDetailView from '../views/reviews/ReviewDetailView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/reviews',
    name: 'ReviewListView',
    component: ReviewListView
  },
  {
    path: '/reviews/create',
    name: 'ReviewCreateView',
    component: ReviewCreateView
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

export default router
