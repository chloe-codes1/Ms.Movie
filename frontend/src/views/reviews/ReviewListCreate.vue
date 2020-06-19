<template>
    <div class="row">
        <div class="col-md-12 col-lg-2">
            <ReviewSidebar :movieId="id"/>
        </div>
        <div class="col-md-12 col-lg-10">
            <ReviewList :reviews="reviews" />
        </div>       
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import ReviewCreate from '@/views/ReviewCreate.vue'
import ReviewList from '@/components/ReviewList.vue'
import ReviewSidebar from '@/components/ReviewSidebar.vue'
export default {
    name: 'ReviewListCreate',
    data() {
        return {
            id: this.$route.params.id,
        }
    },
    components: {
        ReviewList,
        ReviewSidebar,
    },
    computed: {
        ...mapState(['reviews'])

    },
    methods: {
        ...mapActions(['getReviews']),
    },
    created() {
        this.getReviews(this.id)
    }

}
</script>

<style>

</style>