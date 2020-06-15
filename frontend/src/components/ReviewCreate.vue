<template>
    <div>
        <h3>Create Review</h3>
        <!-- title -->
        <b-form-group class="mb-2" label="Title" label-for="title" description="Write your review for the movie">
            <b-form-input type="text" id="title" v-model="review.title"> </b-form-input>
        </b-form-group>
        <!-- rating -->
        <b-form-rating v-model="review.rating" variant="warning" class="mb-2" stars="10"></b-form-rating>
        <p class="mt-2">Rating: {{ review.rating }}</p>
        <!-- content -->
        <b-form-group class="mb-2" label="Content" label-for="content">
            <b-form-textarea
            id="content"
            v-model="review.content"
            placeholder="Write your review content"
            rows="3"
            max-rows="6"
            ></b-form-textarea>
        </b-form-group>
        
        <b-button @click="create">Submit</b-button>  
    </div>
</template>

<script>
export default {
    name: 'ReviewCreate',
    data() {
        return {
            reviewData: {
                title: null,
                content: null,
                rating: null
            },
        }
    },
    methods: {
        create() {this.$emit('createReview', this.reviewData)} 
    }
    
}
</script>

<style>

</style>