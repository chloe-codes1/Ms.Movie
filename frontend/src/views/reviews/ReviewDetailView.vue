<template>
    <div id="review-detail" class="row">
        <div class="col-2">
            <ReviewSidebar :movieId="this.$route.params.movieId"/>
        </div>
        <div class="col-10">
            <ReviewDetail :reviews="reviews" :likeCount="likeCount" :dislikeCount="dislikeCount" />
            <div id="buttons-like">
                <div id="likeButtons">
                    <!-- <b-button size="sm" id="likeButton" @click="likeReview(reviews.id)"><i id="likeThumb" class="far fa-thumbs-up fa-md" aria-hidden="true">Like</i></b-button> -->
                    <b-button size="sm" id="likeButton" @click="likeReview(reviews.id)"><i id="likeThumb" class="fa-thumbs-up fa-md" aria-hidden="true">Like</i></b-button>
                    <b-button size="sm" variant="danger" @click="dislikeReview(reviews.id)"><i id="dislikeThumb" class="fa-thumbs-down fa-md" aria-hidden="true"> DisLike</i></b-button>
                </div>
                <div v-if="userId==reviews.user">
                    <b-button size="sm" @click="goBack">Back</b-button>
                    <router-link :to="'/reviews/'+reviews.movie+'/detail/'+reviews.id+'/update'"><b-button variant="warning" size="sm">Update</b-button></router-link>
                    <b-button size="sm" variant="danger" @click="deleteReview({id: reviews.id, movie: reviews.movie})">Delete</b-button>
                </div>
                <div v-else>
                    <b-button size="sm" @click="goBack">Back</b-button>
                </div>
            </div>
            <CommentCreate/>
            <CommentList :comments="reviews.comment_set" :userId="userId"/>             
        </div>
    </div>
</template>

<script>
import ReviewSidebar from '@/components/ReviewSidebar.vue'
import ReviewDetail from '@/components/ReviewDetail.vue'
import CommentCreate from '@/components/CommentCreate.vue'
import CommentList from '@/components/CommentList.vue'
import { mapState, mapActions } from 'vuex'

export default {
    name: 'ReviewDetailView',

    components: {
        ReviewDetail,
        CommentCreate,
        CommentList,
        ReviewSidebar
    },
    computed: {
        ...mapState(['reviews', 'userId', 'likeCount', 'dislikeCount']),
        isLike() {
            const likeThumb = document.querySelector('#likeThumb')
            if (this.reviews.liked_users.includes(Number(this.userId))) { 
                likeThumb.classList.add('fas')
            }
            else {
                likeThumb.classList.add('far')
            }
            return likeThumb.classList
        },
        isDisLike() {
            const dislikeThumb = document.querySelector('#dislikeThumb')
            if (this.reviews.disliked_users.includes(Number(this.userId))) { 
                dislikeThumb.classList.add('fas')
            }
            else {
                dislikeThumb.classList.add('far')
            }
            return dislikeThumb.classList
        },
    },
    methods: {
        ...mapActions(['getReview', 'deleteReview', 'likeReview', 'dislikeReview']),
        goBack() {
            this.$router.push(`/reviews/${this.reviews.movie}/`)
        },     
    }, 
    created() {
        this.getReview({id: this.$route.params.id, movie: this.$route.params.movieId})
    }

}
</script>

<style scoped>
#review-detail {
   
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