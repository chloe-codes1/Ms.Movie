<template>
  <div class="home container mt-4">
    <h4 class="my-3">Movie recommendations just for {{othersAccount.username}}!</h4>
    <p>Movie filtering based on preferences of movie recommendation algorithm.</p>
    <div class="row">
      <MovieItem v-for="movie in recommendations" :key="movie.id" :movie="movie" class="col-md-12 col-lg-4 col-xl-3" />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";
import MovieItem from "@/components/MovieItem";

export default {
  name: "Home",
  components: {
    MovieItem,
  },
  computed: {
    ...mapState(["recommendations",'othersAccount']),
    ...mapGetters(['id'])
  },
  methods: {
    ...mapActions(["fetchRecommendation", "getOthersAccount"]),
  },
  mounted() {
    this.fetchRecommendation();
    this.getOthersAccount(parseInt(this.id['user']));
  }
};
</script>
<style scoped>

</style>
