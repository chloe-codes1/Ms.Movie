<template>
  <div class="movieListItemModal">
   
    <!-- Modal -->
    <div class="modal fade" :id="'movieDetail-'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-xl" role="document">


        <div v-if="!showContent" class="modal-content">
          <div class="modal-header">
            <div class="d-flex w-100 align-items-center">
              <h5 class="modal-title" id="exampleModalLabel">{{movie.title}}</h5>
              <span class="badge badge-warning text-white ml-2">★ {{movie.vote_average}}</span>
            </div>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body text-left">
            <img class="card-img-top" :src="backdropURL" alt="movie-poster-image">
            <p class="movie-tagline mt-3 text-center">{{movie.tagline}}</p>
            <p><span class="mx-2">{{movie.release_date}}</span>  | <span class="mx-2"> {{movie.runtime}} mins </span> | <span class="mx-2" v-for="(country,index) in movie.countries" :key="index"> {{country}}</span> </p>
            <p>Genres: <span class="ml-2 text-secondary" v-for="(genre, index) in movie.genres" :key="index">{{genre}}</span></p>
            
            <p>Starring: <span class="badge badge-success mx-2" v-for="(cast,index) in movie.casts" :key="index"> {{cast.name}}</span> </p>
            <div>{{movie.content}}</div>

          </div>
          <div class="modal-footer">
            <button v-on:click="toggleHidden" class="btn mr-auto">
                <img class="play-btn" alt="queen" src="@/assets/video.png"> <span>Play Trailer</span>
            </button>
            <button  type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>

        <div v-if="!showTrailer" class="modal-content">



           <Trailer />
        
        </div>
      
      </div>
    </div>

  </div>
</template>

<script>
import Trailer from '@/components/Trailer.vue'

export default {
  name: "MovieDetail",
  data(){
    return {
    showContent: false,
    showTrailer: true,
    }
  
  },
  methods: {
    toggleHidden(){
      this.showContent = !this.showContent
      this.showTrailer = !this.showTrailer
    }
  },
  components:{
    Trailer
  },
  props: {
    movie: Object
  },
  computed: {
    backdropURL() {
      return 'https://image.tmdb.org/t/p/w780//' + this.movie.background
    },
  }
}
</script>

<style class="scoped">
.movieListItemModal{
  z-index: 2;
}
.modal-trigger-button{
  background-color:  #3fb883;
  color:white;
  font-size: 0.9rem;
}

.rating-area{
  background-color: #3fb883;
  font-weight: bold;
}

.movie-tagline{
  color: #343a40;
  font-style: italic;
}

.play-btn{
    width: 30px;
}
</style>