<template>
<div id="review_list">
    <h1>영화 리뷰</h1>
    <router-link to="/reviews/create"><b-button>리뷰 작성</b-button></router-link>
    <b-table hover :items="reviews"></b-table>
</div>
</template>

<script>
import axios from 'axios'
const SERVER = 'http://localhost:8000'
export default {
    name: 'ReviewListView',
    data() {
        return {
            reviews: null
        }
    },
    methods: {
        getReviews() {
            axios.get(`${SERVER}/reviews/`)
            .then(res => {
                console.log(res)
                this.reviews = res.data
            })    
        },
    },
    created() {
            this.getReviews()
        }

}
</script>

<style>

</style>