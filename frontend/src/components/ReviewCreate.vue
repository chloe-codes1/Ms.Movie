<template>
    <div>
        <h3>Create Review</h3>
        <!-- title -->
        <b-form-group class="mb-2" label="Title" label-for="title" description="Write your review for the movie">
            <b-form-input type="text" id="title" v-model="review.title"> </b-form-input>
        </b-form-group>
        <!-- rating -->
        <label for="rating">Rating</label>
        <b-form-input id="rating" v-model="review.rating" type="range" min="0" max="10"></b-form-input>
        <div class="mt-2">Value: {{ review.rating }}</div>
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
        
        <b-button @click="createReview">Submit</b-button>  
    </div>
</template>

<script>
export default {
    name: 'ReviewCreate',
    props: ['review'],
    
}
</script>

<style>

</style>