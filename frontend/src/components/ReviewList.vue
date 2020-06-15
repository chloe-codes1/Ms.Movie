<template>
<div id="review_list">
    <h1>Review For {{  }}</h1>
    <router-link to="/reviews/:id"><b-button>리뷰 작성</b-button></router-link>
    <b-table hover :items="reviews"></b-table>
</div>
</template>

<script>
export default {
    name: 'ReviewList',
    props: ['reviews'],
    methods: {
        
    },
}
</script>

<style>

</style>