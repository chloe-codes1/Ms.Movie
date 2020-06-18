<template>
    <div id="update" class="row">
        <div class="col-2">
            <ReviewSidebar :movieId="this.$route.params.movieId"/>
        </div>
        <div class="col-10">
            <!-- title -->
            <div id="form" >
            <b-form-group class="mb-2" label="Title" label-for="title" description="Write your review for the movie">
                <b-form-input type="text" id="title" v-model="reviews.title"> </b-form-input>
            </b-form-group>
            <!-- rating -->
            <b-input-group class="mb-2">
                <b-input-group-prepend><b-button id="ratingButton">Rating</b-button>   
                </b-input-group-prepend>
                <b-form-rating v-model="reviews.rating" stars="10" variant="warning"></b-form-rating>
                <b-input-group-append>
                    <b-input-group-text class="justify-content-center" style="min-width: 3em;">
                    {{ reviews.rating }}
                    </b-input-group-text>
                </b-input-group-append>
            </b-input-group>
            
            <!-- content -->
            <b-form-group class="mb-2" label="Content" label-for="content">
                <b-form-textarea
                id="content"
                v-model="reviews.content"
                placeholder="Write your review content"
                ></b-form-textarea>
            </b-form-group>
            
            <b-button id="submitButton" @click="updateReview({movie: reviews.movie, id: reviews.id, reviewData: {title: reviews.title, content: reviews.content, rating: reviews.rating}})">Update</b-button> 
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ReviewSidebar from '@/components/ReviewSidebar.vue'
export default {
    name: 'ReviewUpdate',
    components: {
        ReviewSidebar,
    },
    computed: {
        ...mapState(['reviews'])
    },
    methods: {
        ...mapActions(['getReview', 'updateReview']),
    },
    created() {
        this.getReview({movie_id:this.$route.params.movieId, review_id:this.$route.params.id})
    }

}
</script>

<style scoped>
#form {
    width: 80%;
    text-align: left;
    margin: 30px auto;
    
}

b-form-group {
    text-align: left;
}
#content {
    height: 300px;
}
#rating {
    width: 75%;
}
#submitButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#submitButton:hover {
    background-color: #3baa7a;
}
#ratingButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#ratingButton:hover {
    background-color: #3baa7a;
}

</style>