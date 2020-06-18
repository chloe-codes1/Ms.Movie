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
        <h4 class="text-left">{{selectedGenre}} movies</h4>
      </div>
      <div v-else-if="selectedOrder">
        <h4 class="text-left">{{selectedOrder}} movies</h4>
      </div>
      <div v-else-if="keyword">
        <h4 class="text-left">Search result for movie title contains "{{keyword}}"</h4>
      </div>
      <div class="row">
        <MovieItem v-for="movie in movies" :key="movie.id" :movie="movie" class="col-md-12 col-lg-3 col-xl-2"/>
      </div>
    </div>
    <button @click="scrollToTop" class="button-bottom btn">Top</button>
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
      this.selectedOrder= null;
      this.keyword= null;
    },
    sortOrder(value) {
      this.selectedOrder = value;
      this.fetchMovies({
        params: {
          order_by: value
        }
      });
      this.selectedGenre= null;
      this.keyword= null;
    },
    searchMovie(value){
      this.keyword = value;
      this.fetchMovies({
        params:{
          keyword: value
        }
      });
      this.selectedGenre= null;
      this.selectedOrder= null;
    },
    scrollToTop: function() {
      scroll(0, 0);
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

.button-bottom {
    position: fixed;
    right: 2vw;
    bottom: 2vh;
    background-color:  #3fb883;
    padding: 4px 8px;
    color: white;
    font-weight: bold;
    z-index: 4;
}

</style>
