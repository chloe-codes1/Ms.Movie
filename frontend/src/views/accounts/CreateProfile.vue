<template>
  <div class="w-50 m-auto pt-5 mt-5">
    <h4 class="my-5 pt-4">What is your favorite genre of movie?</h4>
    <b-form-group
      class="mb-4"
      label-for="favorite"
      description="Choose your favorite genre. We'll recommend movies based on your choice."
    >
      <b-form-select :options="options" id="favorite" v-model="favoriteGenre"></b-form-select>
    </b-form-group>
    <b-button @click="createProfile({favorite: favoriteGenre })" id="genreSubmitButton">Submit</b-button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name : 'CreateProfile',
  data(){
    return {
      favoriteGenre: null,
      options: [
          { value: 'Adventure', text: 'Adventure' },
          { value: 'Fantasy', text: 'Fantasy' },
          { value: 'Animation', text: 'Animation' },
          { value: 'Drama', text: 'Drama' },
          { value: 'Horror', text: 'Horror' },
          { value: 'Action', text: 'Action' },
          { value: 'Comedy', text: 'Comedy' },
          { value: 'History', text: 'History' },
          { value: 'Western', text: 'Western' },
          { value: 'Thriller', text: 'Thriller' },
          { value: 'Crime', text: 'Crime' },
          { value: 'Documentary', text: 'Documentary' },
          { value: 'Science Fiction', text: 'Science Fiction' },
          { value: 'Mystery', text: 'Mystery' },
          { value: 'Music', text: 'Music' },
          { value: 'Romance', text: 'Romance' },
          { value: 'Family', text: 'Family' },
          { value: 'War', text: 'War' },
          { value: 'TV Movie', text: 'TV Movie' },
        ]
    }
  },
  methods: {
    ...mapActions(['createProfile'])
  }
}
</script>

<style scoped>

#genreSubmitButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#genreSubmitButton:hover {
    background-color: #3baa7a;
}
</style>