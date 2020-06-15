<template>
    <div id="create">
        <h3>Create Review</h3>
        <!-- title -->
        <b-form-group class="mb-2" label="Title" label-for="title" description="Write your review for the movie">
            <b-form-input type="text" id="title" v-model="reviewData.title"> </b-form-input>
        </b-form-group>
        <!-- rating -->
        <label for="rating">Rating:</label>
        <b-form-rating id="rating" inline v-model="reviewData.rating" variant="warning" class="mb-2" stars="10"></b-form-rating>
        value: {{reviewData.rating}}
        <!-- content -->
        <b-form-group class="mb-2" label="Content" label-for="content">
            <b-form-textarea
            id="content"
            v-model="reviewData.content"
            placeholder="Write your review content"
            rows="3"
            max-rows="6"
            ></b-form-textarea>
        </b-form-group>
        <b-button @click="createReview({'reviewData': reviewData, 'id': id})">Submit</b-button>  
    </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'ReviewCreate',
    data() {
        return {
            reviewData: {
                title: null,
                content: null,
                rating: null
            },
            id: this.$route.params.id
        }
    },
    methods: {
        ...mapActions(['createReview'])
    }
    
}
</script>

<style>
#create {
    width: 50%;
}

</style>