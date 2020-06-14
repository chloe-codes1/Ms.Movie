<template>
  <div>
      <b-card
        :title="movie.title"
        :img-src="movie.image"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
      >
        <b-button href="#" variant="primary">상세 보기</b-button>
      </b-card>
  </div>
</template>

<script>
export default {
  name: 'MovieItem'
}
</script>

<style>

</style>