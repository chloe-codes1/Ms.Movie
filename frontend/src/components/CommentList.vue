<template>
<div>
    <hr>
    <div v-for="comment in comments" :key="comment.id">
        <div id="comment">
            <div id="comment-body">
                <div id="user-avatar"><b-avatar variant="warning"></b-avatar></div>
                <div id="comment-content">
                    <p id="comment-text">{{comment.username}}  <span id="date">{{comment.updated_at}}</span></p>
                    <p>{{comment.content}}</p>
                </div>
            </div>

            <div v-if="userId==comment.user">
                <a id="deleteLink" @click="deleteComment({review: reviewId, comment: comment.id})">Delete</a>
            </div>
        </div>
        <hr>
    </div>   
</div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    name: 'CommentList',
    props: ['comments', 'userId'],
    data() {
        return {
            reviewId: this.$route.params.id
        }
    },
    methods: {
        ...mapActions(['deleteComment']),
    },

}
</script>

<style scoped>
#comment {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
#comment-body {
    display: flex;
    align-items: center;
}
#comment-content {
    text-align: left;
}
p {
    margin-bottom: 0;
}
#user-avatar {
    margin: 0 10px;
}
#comment-text {
    font-weight: bold;
}
#date {
    font-weight: normal;
}
#deleteLink {
    color: gray;
}
#deleteLink:hover {
    text-decoration: underline;
    cursor: pointer;
}

</style>