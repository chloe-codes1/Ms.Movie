<template>
    <div id="comment-body">
        <h5>Comments</h5>
        
        <hr>
        <b-input-group>
            <b-form-input v-model="commentData.content" @keyup.enter="onWrite" placeholder="Enter your comment for the review"></b-form-input>
            <b-input-group-append>
                <b-button @click="onWrite">Submit</b-button> 
            </b-input-group-append>
        </b-input-group>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: 'CommentCreate',
    data() {
        return {
            commentData: {
                content: null
            }
        }
    },
    methods: { 
        ...mapActions(['createComment']), 
        onWrite() { 
            this.createComment({commentData: this.commentData, id: this.$route.params.id})
        }
    },
}
</script>

<style>

</style>