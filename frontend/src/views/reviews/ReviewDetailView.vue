<template>
    <div id="review-detail">
        
        <ReviewDetail :reviews="reviews" :likes="likes" :dislikes="dislikes"/>
        <div id="buttons-like">
            <div id="likes">
                <b-button size="sm" id="likeButton" @click="likeReview(reviews.id)"><i id="likeThumb" class="far fa-thumbs-up fa-md" aria-hidden="true">Like</i></b-button>
                <b-button size="sm" variant="danger" @click="dislikeReview(reviews.id)"><i class="far fa-thumbs-down fa-md" aria-hidden="true"> DisLike</i></b-button>
            </div>
            <div v-if="userId==reviews.user">
                <b-button size="sm" @click="goBack">Back</b-button>
                <router-link :to="'/reviews/detail/'+reviews.id+'/update'"><b-button variant="warning" size="sm">Update</b-button></router-link>
                <b-button size="sm" variant="danger" @click="deleteReview({id: reviews.id, movie: reviews.movie})">Delete</b-button>
            </div>
            <div v-else>
                <b-button size="sm" @click="goBack">Back</b-button>
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
    data() {
        return {
            likes: 0,
            dislikes: 0,
            change: 0,
        }
    },
    components: {
        ReviewDetail,
        CommentCreate,
        CommentList
    },
    computed: {
        ...mapState(['reviews', 'userId']),
    },
    methods: {
        ...mapActions(['getReview', 'deleteReview', 'likeReview', 'dislikeReview']),
        goBack() {
            this.router.push(`/reviews/${this.reviews.movie}/`)
        },
    },
    watch: {
        change: function() {
            this.likes = this.reviews.liked_users.length
            this.dislikes = this.reviews.disliked_users.length
            console.log("shffh")
        },
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
#likeButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#likeButton:hover {
    background-color: #3baa7a;
}
</style>