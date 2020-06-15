<template>
    <div>
        
        <ReviewCreate @create="createReview"/>
        
        <ReviewList :reviews="reviews"/>
        
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ReviewCreate from '@/components/ReviewCreate.vue'
import ReviewList from '@/components/ReviewList.vue'
export default {
    name: 'ReviewListCreate',
    data() {
        return {
            id: this.$route.params.id,
        }
    },
    components: {
        ReviewCreate,
        ReviewList
    },
    computed: {
        ...mapState(['reviews'])

    },
    methods: {
        ...mapActions(['getReviews']),
        ...mapActions(['createReview'])
    },
    created() {
        this.getReviews(this.id)
    }

}
</script>

<style>

</style>