<template>
  <div>
    <h1>Movies</h1>
    <div v-for="movie in movies" :key="movie.id">
      <MovieItem :movie='movie' />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'Movies',
  data: () => ({
    query: ''
  }),
  component:{
    MovieItem
  },
  computed: {
    ...mapState(['movies']),
  },
  methods: {
    ...mapActions(['fetchMovies'])
  },
  //mouted 되는 시점에 바로 실행
  created(){
    this.fetchMovies()
  }
}
</script>

<style>

</style>
