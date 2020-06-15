<template>
<div class="Trailer col-md-12 col-lg-8">
  <h1>Trailer!!</h1>
  <div v-if="video">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe id="player" type="text/html" class="video-iframe embed-responsive-item" 
              :src="videoURL" frameborder="0" allowfullscreen></iframe>
    </div>
    <p class="video-detail-title"> {{video.snippet.title}}</p>
    <p class="published-at">{{video.snippet.publishedAt | dateParse('MM.DD.YY', { epoch: 1900 }) }}</p>
  </div>
</div>

</template>

<script>

export default {
  name: 'Trailer',
  props: {
    videos: Array,
    video: Object,
  },
  computed: {
    videoURL(){
      return 'https://www.youtube.com/embed/'+ this.video.id.videoId
    }
  }
}
</script>

<style>
.Trailer{
  z-index: 3;
}


.video-iframe{
  width : 100%;
  height : 500px
}

.video-detail-title{
  font-size: 1.2rem;
  margin-top: 10px;
}

.published-at {
  font-size: 0.8rem;
}

</style>