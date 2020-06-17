<template>
    <div id="update">
        
        <h3>Update Review</h3>
            <div id="form">
            <!-- title -->
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
            <b-button id="submitButton" @click="onWrite">Update</b-button> 
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: 'ReviewUpdate',
    computed: {
        ...mapState(['reviews'])
    },
    methods: {
        ...mapActions(['getReview', 'updateReview']),
        onWrite() {
            this.updateReview({reviewData: {title:this.reviews.title, content: this.reviews.content, rating: this.reviews.rating}, id: this.$route.params.id})
        }
    },
    created() {
        this.getReview(this.$route.params.id)
    }

}
</script>

<style scoped>
#update {
    width: 75%;
    margin: 0 auto;
}
#form {
    text-align: left;
    margin-top: 30px;
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