<template>
  <div id="app">

    <nav class="navbar navbar-expand-md navbar-light sticky-top d-inline-flex justify-content-between w-100" style="background-color:white; box-shadow: 0 2px 2px -2px rgba(0,0,0,.3);">
      <ul class="navbar " style="position: absolute; left: 50%; top:0%; transform: translateX(-50%); ">
        <li class="list-unstyled">
          <router-link to="/" class="text-decoration-none nav-links py-2 site-logo"> Ms. Movie</router-link>
        </li>
      </ul>
      <div>
        <div class="d-block d-sm-none" style="height:40px;" >
          <button style="position: absolute;left:10px; top: 10px;" class="navbar-toggler mr-auto border-0" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"> 
            <span class="navbar-toggler-icon"></span>
          </button>  
        </div>
        <div class="collapse navbar-collapse py-0 w-100" id="navbarNav">
          <ul class="navbar-nav mr-auto w-100 pr-0">
              <li class="nav-item active">
                <router-link to="/movies" class="text-decoration-none nav-links mr-3 py-2">Movies</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <router-link :to="'/accounts/'+userId" class="text-decoration-none nav-links mr-3 py-2">Profile</router-link>
              </li>
              <li v-if="isLoggedIn" class="nav-item">
                <router-link to="/accounts/logout" class="text-decoration-none nav-links py-2">Logout</router-link>
              </li>
              <li v-if="!isLoggedIn" class="nav-item active">
                <router-link to="/accounts/login" class="text-decoration-none nav-links mr-3 py-2">Login</router-link>
              </li>
              <li v-if="!isLoggedIn" class="nav-item">
                <router-link to="/accounts/signup" class="text-decoration-none nav-links py-2">Sign Up</router-link>
              </li>
          </ul>
      </div>  
      </div>
    </nav> 
    <router-view />
  </div>
</template>

<script>
import {mapState, mapActions, mapGetters} from 'vuex'

export default { 
  name: 'App',
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapState(['userId']),
    ...mapGetters(['isLoggedIn'])
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

.site-logo{
  font-size: 1.2rem;
}

.nav-item {
  font-weight: bold;
  color: #3fb883;
}

.nav-links{
  color: #3fb883;
  font-weight: bold;
}
</style>
