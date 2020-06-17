<template>
  <div>
    <MovieFilter
      @search-movie-clicked="searchMovie"
      @order-sort-clicked="sortOrder"
      @genre-sort-clicked="sortGenre"
      class="left-side nav flex-column position-fixed"
    />
    <div class="right-side mt-3">
      <div v-if="selectedGenre">
        <h3 class="text-left">{{selectedGenre}} movies</h3>
      </div>
      <div v-else-if="selectedOrder">
        <h3 class="text-left">{{selectedOrder}} movies</h3>
      </div>
      <div v-else-if="keyword">
        <h3 class="text-left">Search result for movie title contains "{{keyword}}"</h3>
      </div>
      <div class="row">
        <MovieItem v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieItem from "@/components/MovieItem";
import MovieFilter from "@/components/MovieFilter";

export default {
  name: "Movies",
  components: {
    MovieItem,
    MovieFilter
  },
  data() {
    return {
      selectedGenre: null,
      selectedOrder: null,
      keyword: null,
    };
  },
  computed: {
    ...mapState(["movies"]),
    rows() {
      return this.movies.length;
    }
  },
  methods: {
    ...mapActions(["fetchMovies"]),
    sortGenre(value) {
      this.selectedGenre = value;
      this.fetchMovies({
        params: {
          genre: value
        }
      });
    },
    sortOrder(value) {
      this.selectedOrder = value;
      this.fetchMovies({
        params: {
          order_by: value
        }
      });
    },
    searchMovie(value){
      this.keyword = value;
      this.fetchMovies({
        params:{
          keyword: value
        }
      })
    }
  },
  //mouted 되는 시점에 바로 실행
  created() {
    this.fetchMovies();
  }
};
</script>

<style scoped>
.left-side {
  width: 100px;
  height: 100%;
  margin-top: 40px;
  font-family: "FV Almelo", Arial, sans-serif;
  font-size: large;
  z-index: 3;
}

.right-side {
  padding-left: 100px;
}
</style>
