<template>
  <div class="movieListItemModal">
   
    <!-- Modal -->
    <div class="modal fade" :id="'movieDetail-'+movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-xl" role="document">
        <div class="modal-content">
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
            
            <p>장르: <span class="ml-2 text-secondary" v-for="(genre, index) in movie.genres" :key="index">{{genre}}</span></p>
            
            <p>출연진: <span class="badge badge-success mx-2" v-for="(cast,index) in movie.casts" :key="index"> {{cast.name}}</span> </p>
            <p>개봉일: <span class="mx-2">{{movie.release_date}}</span>  | <span class="mx-2"> {{movie.runtime}} 분 </span> | <span class="mx-2" v-for="(country,index) in movie.countries" :key="index"> {{country}}</span> </p>
            <div>{{movie.content}}</div>

          </div>
          <div class="modal-footer">
               <router-link to="/" >
                <button class="btn mr-auto">
                    <img class="play-btn" alt="queen" src="@/assets/video.png"> <span>예고편 보기</span>
                </button>
                </router-link>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "MovieDetail",
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