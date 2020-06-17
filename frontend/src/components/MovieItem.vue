<template>
  <div  class="movieListItem col-md-12 col-lg-3 col-xl-2" data-toggle="modal" :data-target="`#movieDetail-${movie.id}`">
      <div class="card my-3" style="width: 100%" >
        <img class="card-img-top" :src="posterURL" alt="movie-poster-image">
      </div>
      <MovieDetailModal :movie="movie"/>
  </div>
</template>

<script>
import MovieDetailModal from '@/components/MovieDetailModal.vue'

export default {
  name: 'MovieItem',
  components: {
    MovieDetailModal
  },
  props: ['movie'],
  computed: {
    posterURL(){
      return 'https://image.tmdb.org/t/p/w780//' + this.movie.poster
    }
  }
}
</script>

<style>
.movieListItem .card:hover {
  transform: scale(1.5); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
  z-index: 1;
}


</style>