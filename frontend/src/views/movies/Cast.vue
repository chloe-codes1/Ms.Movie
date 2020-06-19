<template>
  <div v-if="cast">
    <div class="row px-4 py-3">
      <div class="col-md-12 col-lg-3">
        <div class="mb-4">
          <img class="card-img-top" :src="profileURL" alt="cast-profile-image"/>
        </div>
        <div class="text-left">
          <h4 class="font-weight-bold mb-3"> Personal Info</h4>
          <h5 class="font-weight-bold mb-2">Known for</h5>
          <p>{{ cast.department}}</p>
          <h5 class="font-weight-bold mb-2">Gender</h5>
          <p>{{getGender}}</p>
          <h5 class="font-weight-bold mb-2">Birthday</h5>
          <p>{{ cast.birthday}}</p>
          <h5 class="font-weight-bold mb-2">Place of Birth</h5>
          <p>{{ cast.place_of_birth}}</p>
        </div>
      </div>
      <div class="col-md-12 col-lg-9 mt-3 text-left">
        <h2 class="font-weight-bold mb-4"> {{cast.name}}</h2>
        <h4 class="font-weight-bold mb-2"> Biography</h4>
        <div class="mb-4">{{ cast.biography}}</div>
        
        <h4 class="font-weight-bold mb-2"> Known for</h4>
        <div v-if="starredMovies.length > 1" class="row">
          <div class="col-md-6 col-lg-4 col-xl-2" v-for="(starredMovie, idx) in starredMovies" :key="idx">
            <img class="card-img-top d-block" :src="'https://image.tmdb.org/t/p/w300//' +starredMovie.poster_path " alt="movie-poster-image">
            <p class="text-center font-weight-bold mb-1"> {{starredMovie.title}} </p>
            <p class="text-center"> {{starredMovie.character}} </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

// const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY;
const TMDB_API_KEY = '763c6d15a6a1f3af5c6b8f7cb7b3fdcd';
const TMDB_BASE_URL = "https://api.themoviedb.org/3/person";

// import { mapState, mapActions } from 'vuex';
import axios from "axios";

export default {
  name: 'Cast',
  data(){
    return {
      cast: this.$route.params.item,
      starredMovies: []
    }
  },
  computed: {
    profileURL(){
      return 'https://image.tmdb.org/t/p/w500/' + this.cast.profile
    },
    getGender(){
      if (this.cast.gender == 1){
        return 'Female'
      }else {
        return 'Male'
      }
    }
  },
  methods: {
    getStarredPosters(){
      const TMDB_API_URL=`${TMDB_BASE_URL}/${this.cast.cast_id}/movie_credits?api_key=${TMDB_API_KEY}&language=en-US"`
      axios
        .get(TMDB_API_URL)
        .then(res => {
          res.data.cast.map( item => {
            if (item.poster_path){
              this.starredMovies.push(item)
            }
          })
        })
        .catch(err => console.log(err));
    }
  },
  created(){
    // this.fetchMovie(this.cast.movie[0]);
    this.getStarredPosters();
  }
}
</script>

<style>

</style>