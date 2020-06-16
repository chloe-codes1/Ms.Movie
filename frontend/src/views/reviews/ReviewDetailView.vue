<template>
    <div id="review-detail">
       <ReviewDetail :reviews="reviews"/>
       <CommentCreate/>
       <CommentList :comments="reviews.comment_set"/>
    </div>
</template>

<script>
import ReviewDetail from '@/components/ReviewDetail.vue'
import CommentCreate from '@/components/CommentCreate.vue'
import CommentList from '@/components/CommentList.vue'
import { mapState, mapActions } from 'vuex'
export default {
    name: 'ReviewDetailView',
    
    components: {
        ReviewDetail,
        CommentCreate,
        CommentList
    },
    computed: {
        ...mapState(['reviews']),
       

    },
    methods: {
        ...mapActions(['getReview'])

    },
        
    created() {
        this.getReview(this.$route.params.id)
    }

}
</script>

<style scoped>
#review-detail {
    width: 75%;
    margin: 0 auto;
}
</style>