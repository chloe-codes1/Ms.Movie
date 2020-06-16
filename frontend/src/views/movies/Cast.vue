<template>
  <div v-if="cast">
    <div class="row px-4 py-3">
      <div class="col-3">
        <div class="mb-4">
          <img class="card-img-top" :src="profileURL" alt="cast-profile-image">
        </div>
        <div class="text-left">
          <h4 class="font-weight-bold mb-3"> Personal Info</h4>
          <h5 class="font-weight-bold mb-2">Gender</h5>
          <p>{{getGender}}</p>
          <h5 class="font-weight-bold mb-2">Birthday</h5>
          <p>{{ cast.birthday}}</p>
          <h5 class="font-weight-bold mb-2">Place of Birth</h5>
          <p>{{ cast.place_of_birth}}</p>
        </div>
      </div>
      <div class="col-9 mt-3 text-left">
        <h2 class="font-weight-bold mb-4"> {{cast.name}}</h2>
        <h4 class="font-weight-bold mb-2"> Biography</h4>
        <div class="mb-4">{{ cast.biography}}</div>

        <h4 class="font-weight-bold mb-2"> Known for</h4>
        <div class="col-2">
           <img class="card-img-top d-block" :src="posterURL" alt="movie-poster-image">
           <p class="text-center"> {{starredMovie.title}} </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Cast',
  data(){
    return {
      cast: this.$route.params.item
    }
  },
  computed: {
    ...mapState(['starredMovie']),
    profileURL(){
      return 'https://image.tmdb.org/t/p/w500/' + this.cast.profile
    },
    posterURL(){
      return 'https://image.tmdb.org/t/p/w300//' + this.starredMovie.poster
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
      ...mapActions(['fetchMovie'])
  },
  mounted(){
    this.fetchMovie(this.cast.movie[0]);
  }
}
</script>

<style>

</style>