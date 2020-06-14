<template>
  <div>
    <h1 >Movies</h1>
      <div class="row">
        <MovieItem v-for="movie in movies" :key="movie.id" :movie='movie' />
      </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'Movies',
  components:{
    MovieItem
  },
  data(){
    return{
      perPage:3,
      currentPage:1,
    }
  },
  computed: {
    ...mapState(['movies']),
    rows(){
      return this.movies.length
    }
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
