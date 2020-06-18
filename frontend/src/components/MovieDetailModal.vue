<template>
  <div class="movieListItemModal">
    <!-- Modal -->
    <div
      class="modal fade"
      :id="'movieDetail-'+movie.id"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-xl" role="document">
        <div v-if="!showContent" class="modal-content">
          <div class="modal-header">
            <div>
              <div class="d-flex w-100 align-items-center">
                <h5 class="modal-title font-weight-bold" id="exampleModalLabel">{{movie.title}}</h5>
                <span class="badge badge-warning text-white ml-2">★ {{movie.vote_average}}</span>
              </div>
              <p class="mt-3 mb-1">
                <span class="mx-2">{{movie.release_date}}</span> |
                <span class="mx-2">{{movie.runtime}} mins</span> |
                <span
                  class="mx-2"
                  v-for="(country,index) in movie.countries"
                  :key="index"
                >{{country}}</span>
              </p>
            </div>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body text-left">
            <img class="card-img-top" :src="backdropURL" alt="movie-poster-image" />
            <p class="movie-tagline mt-3 text-center">{{movie.tagline}}</p>

            <p class="font-weight-bold">Genres</p>
            <span
              class="badge badge-light mr-3 mb-4"
              v-for="genre in movie.genres"
              :key="genre.id"
            >{{genre}}</span>
            <p class="font-weight-bold">Top Billed Cast</p>
            <div
              class="cast-profile-links badge badge-light mr-3 mb-4"
              v-for="(cast,index) in movie.casts"
              :key="index"
              data-dismiss="modal"
            >
              <router-link
                :to="{
                name: 'Cast',
                params: {
                  item: cast
                }
              }"
                class="text-decoration-none cast-profile-area"
              >
                <p class="text-dark mb-0">{{cast.name}}</p>
              </router-link>
            </div>
            <p class="font-weight-bold">Overview</p>
            <div class="mb-3">{{movie.content}}</div>
          </div>
          <div class="modal-footer">
            <button @click="toggleHidden" class="btn">
              <img class="play-btn" alt="queen" src="@/assets/video.png" />
              <span class="ml-2">Play Trailer</span>
            </button>
            <button @click="showReviews" data-dismiss="modal" class="btn mr-auto">Reviews</button>
            <button
              @click="writeReview"
              data-dismiss="modal"
              class="btn btn-warning review-creation-btn"
            >Write a review</button>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>

        <div v-if="!showTrailer" class="modal-content">
          <div class="modal-header">
            <button
              @click="toggleHidden"
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >Back to detail</button>
          </div>
          <Trailer :video="video" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

import axios from "axios";
import Trailer from "@/components/Trailer.vue";

export default {
  name: "MovieDetail",
  data() {
    return {
      showContent: false,
      showTrailer: true,
      inputValue: "",
      video: null
    };
  },
  methods: {
    toggleHidden() {
      this.showContent = !this.showContent;
      this.showTrailer = !this.showTrailer;
      this.getTrailer(this.movie.title);
    },
    getTrailer(movieTitle) {
      this.inputValue = movieTitle + "trailer";
      axios
        .get(API_URL, {
          params: {
            key: API_KEY,
            part: "snippet",
            type: "video",
            q: this.inputValue
          }
        })
        .then(res => {
          res.data.items.forEach(item => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(item.snippet.title, "text/html");
            item.snippet.title = doc.body.innerText;
          });
          this.video = res.data.items[0];
        })
        .catch(err => console.error(err));
    },
    writeReview() {
      this.$router.push(`/reviews/${this.movie.id}/create`);
    },
    showReviews() {
      this.$router.push(`/reviews/${this.movie.id}`);
    }
  },
  components: {
    Trailer
  },
  props: {
    movie: Object
  },
  computed: {
    backdropURL() {
      return "https://image.tmdb.org/t/p/w780//" + this.movie.background;
    },
    profileURL(cast) {
      return "https://image.tmdb.org/t/p/w500/" + cast.profile;
    }
  }
};
</script>

<style class="scoped">
.movieListItemModal {
  z-index: 2;
}
.modal-trigger-button {
  background-color: #3fb883;
  color: white;
  font-size: 0.9rem;
}

.rating-area {
  background-color: #3fb883;
  font-weight: bold;
}

.movie-tagline {
  color: #343a40;
  font-style: italic;
}

.play-btn,
.review-btn {
  width: 30px;
}

.review-creation-btn {
  opacity: 0.8;
}

.cast-profile-links:hover {
  transform: scale(
    1.5
  ); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
  z-index: 1;
}
</style>