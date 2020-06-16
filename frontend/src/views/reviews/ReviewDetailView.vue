<template>
    <div id="review-detail">
        userID!!!!!! <p>{{ userId }}</p> 
        {{id }}
        로그인 되어있냐!! {{ isLoggedIn }}
       <ReviewDetail :reviews="reviews"/>
       <CommentCreate/>
       <CommentList :comments="reviews.comment_set"/>
    </div>
</template>

<script>
import ReviewDetail from '@/components/ReviewDetail.vue'
import CommentCreate from '@/components/CommentCreate.vue'
import CommentList from '@/components/CommentList.vue'
import { mapState, mapGetters, mapActions } from 'vuex'
export default {
    name: 'ReviewDetailView',
    data() {
        return {
            id: null
        }
    },
    components: {
        ReviewDetail,
        CommentCreate,
        CommentList
    },
    computed: {
        ...mapState(['reviews', 'userId']),
        ...mapGetters(['isLoggedIn']),
        
    },
    methods: {
        ...mapActions(['getReview', 'getUserState']),
    },
        
    created() {
        this.getReview(this.$route.params.id),
        
        this.getUserState(this.id)
        
    }

}
</script>

<style scoped>
#review-detail {
    width: 75%;
    margin: 0 auto;
}
</style>