<template>
    <div id="review-detail">
        <ReviewDetail :reviews="reviews"/>
        <div id="buttons-like">
            <div id="likes">
                <b-icon icon="hand-thumbs-up" font-scale="1.5" class="rounded-circle bg-primary" variant="light"></b-icon>
                <b-icon icon="hand-thumbs-down" font-scale="1.5" variant="light"></b-icon>
            </div>
            <div v-if="userId==reviews.user">
                <router-link :to="'/reviews/detail/'+reviews.id+'/update'"><b-button variant="warning" size="sm">Update</b-button></router-link>
                <b-button size="sm" variant="danger" @click="deleteReview({id: reviews.id, movie: reviews.movie})">Delete</b-button>
            </div>
        </div>
        
        <CommentCreate/>
        <CommentList :comments="reviews.comment_set" :userId="userId"/>
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
        ...mapState(['reviews', 'userId']),    
    },
    methods: {
        ...mapActions(['getReview', 'deleteReview']),
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
button {
    margin: 3px;
}
#buttons-like {
    display: flex;
    justify-content: space-between;
    
}

#likes {
    height: 50px;
    width: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
svg {
    border: 1px solid blue;
}
svg:hover{
    width: 2rem;
    height: 2rem;
}
</style>