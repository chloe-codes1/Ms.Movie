<template>
    <div>
        <p>{{review}}</p>
    </div>
</template>

<script>
import axios from 'axios'
const SERVER = 'http://localhost:8000'
export default {
    name: 'ReviewDetailView',
    data() {
        return {
            id: this.$route.params.id,
            review : null
        }
    },
    methods: {
        getReview() {
            axios.get(`${SERVER}/reviews/${this.id}/`)
            .then(res => {
                console.log(res.data)
                this.review = res.data
            })  
        }
    },
    created() {
        this.getReview()
    }
}
</script>

<style>

</style>