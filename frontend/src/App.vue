<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> | 
      <router-link to="/reviews">Review List</router-link> | 
      <span v-if="isLoggedIn">
        <router-link to="/accounts/logout" @click.native="logout">Logout</router-link>
      </span>
      <span v-else>
        <router-link to="/accounts/login">Login</router-link> | 
        <router-link to="/accounts/signup">Sign Up</router-link>
      </span>
    </div>
    <router-view @submit-login-data="login" @submit-signup-data="signup"/>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER = 'http://localhost:8000'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedIn = true
    },
    signup(signupData) {
      axios.post(`${SERVER}/rest-auth/signup/`, signupData)
        .then(res => {
          console.log(`${SERVER}/rest-auth/signup/`)
          this.setCookie(res.data.key)
          this.$router.push('/')
        .catch(err => console.log(err.response.data))
        })
    },
    login(loginData) {
      axios.post(`${SERVER}/rest-auth/login/`, loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push('/')
        .catch(err => console.log(err.response.data))
        })
    },
    logout() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${SERVER}/rest-auth/logout/`,null, requestHeaders)
        .then(res => {
          console.log(res.data)
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push('/articless')
        })
    },

    
  },
  mounted(){
  this.isLoggedIn = this.$cookies.isKey('auth-token')
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
