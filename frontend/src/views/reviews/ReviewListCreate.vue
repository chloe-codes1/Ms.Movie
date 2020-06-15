<template>
    <div>
        <ReviewCreate @create="createReview"/>
        <ReviewList :reviews="reviews"/>
    </div>
</template>

<script>
import { mapState, mapActions } from vuex
import ReviewCreate from '@/components/ReviewCreate.vue'
import ReviewList from '@/components/ReviewList.vue'
export default {
    name: 'ReviewListCreate',
    components: {
        ReviewCreate,
        ReviewList
    },
    computed: {

    },
    methods: {

    },
    created() {
        this.getReviews()

    }

}
</script>

<style>

</style>