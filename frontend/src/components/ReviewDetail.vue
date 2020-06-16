<template>  
<div>
     <p>{{reviews}}</p>
     <h3>Review For {{reviews.movie_title}}</h3>
     <h4>{{reviews.title}}</h4>
      <div>
        <b-form-rating id="rating-inline" v-model="divideRating" inline no-border variant="warning" readonly></b-form-rating>
        <label for="rating-inline">{{reviews.rating}}</label>
    </div>
     <hr>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: 'ReviewDetailView',
    data() {
        return {
            id: this.$route.params.id,
            
        }
    },
    computed: {
        ...mapState(['reviews']),
        divideRating() {
            return this.reviews.rating/2
        }

    },
    methods: {
        ...mapActions(['getReview'])

    },
        
    created() {
        this.getReview(this.id)
    }
}
</script>

<style>
label {
    color: red;
}
</style>