<template>
  <ul>
    <li class="nav-item dropright">
      <a
        class="nav-link active dropdown-toggle shadow-none"
        href="#"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <i class="fa fa-search" style="font-size:36px"></i>
      </a>
      <div class="dropdown-menu px-2" aria-labelledby="dropdownMenuButton">
        <b-form-group class="text-center mb-2" label-for="searchInput">
          <b-form-input v-model="keyword" placeholder="Search movies" id="searchInput"></b-form-input>
          <button @click="searchMovie" class="btn btn-secondary">Search!</button>
        </b-form-group>
      </div>
    </li>
    <li class="nav-item dropright">
      <a
        class="nav-link drop-toggle shadow-none"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
        href="#"
      >Order by</a>
      <div class="dropdown-menu px-2 m-0" aria-labelledby="dropdownMenuButton">
        <b-form-group class="text-center mb-2" label-for="orderSortForm">
          <b-form-select
            :options="orderOptions"
            id="orderSortForm"
            class="d-inline"
            v-model="selectedOrder"
          ></b-form-select>
          <button @click="sortOrder" class="btn btn-secondary">Sort!</button>
        </b-form-group>
      </div>
    </li>
    <li class="nav-item dropright">
      <a
        class="nav-link drop-toggle shadow-none"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
        href="#"
      >Genres</a>
      <div class="dropdown-menu px-2 m-0" aria-labelledby="dropdownMenuButton">
        <b-form-group class="text-center mb-2" label-for="genreSortForm">
          <b-form-select
            :options="genreOptions"
            id="genreSortForm"
            class="d-inline"
            v-model="selectedGenre"
          ></b-form-select>
          <button @click="sortGenre" class="btn btn-secondary">Sort!</button>
        </b-form-group>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "MovieFilter",
  data() {
    return {
      selectedOrder: null,
      selectedGenre: null,
      keyword: null,
      genreOptions: [
        { value: "Adventure", text: "Adventure" },
        { value: "Fantasy", text: "Fantasy" },
        { value: "Animation", text: "Animation" },
        { value: "Drama", text: "Drama" },
        { value: "Horror", text: "Horror" },
        { value: "Action", text: "Action" },
        { value: "Comedy", text: "Comedy" },
        { value: "History", text: "History" },
        { value: "Western", text: "Western" },
        { value: "Thriller", text: "Thriller" },
        { value: "Crime", text: "Crime" },
        { value: "Documentary", text: "Documentary" },
        { value: "Science Fiction", text: "Science Fiction" },
        { value: "Mystery", text: "Mystery" },
        { value: "Music", text: "Music" },
        { value: "Romance", text: "Romance" },
        { value: "Family", text: "Family" },
        { value: "War", text: "War" },
        { value: "TV Movie", text: "TV Movie" }
      ],
      orderOptions: [
        { value: "Top rating", text: "Top rating" },
        { value: "Latest", text: "Latest" },
        { value: "Oldest", text: "Oldest" }
      ]
    };
  },
  methods: {
    sortGenre() {
      this.$emit("genre-sort-clicked", this.selectedGenre);
    },
    sortOrder() {
      this.$emit("order-sort-clicked", this.selectedOrder);
    },
    searchMovie(){
      this.$emit("search-movie-clicked", this.keyword)
    },
    preventClosing() {
      let domElement = this.$el;

      const dropdownToggles = domElement.getElementsByClassName(
        "dropdown-menu"
      );
      dropdownToggles.forEach(dropdownToggle => {
        dropdownToggle.addEventListener("click", e => {
          e.stopPropagation();
        });
      });
    }
  },
  mounted() {
    this.preventClosing();
  }
};
</script>

<style>
</style>