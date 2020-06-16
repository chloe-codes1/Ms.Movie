<template>
<div>
    <hr>
    <div v-for="comment in comments" :key="comment.id">
        <div id="comment">
            <div id="user-avatar"><b-avatar variant="warning"></b-avatar></div>
            <div id="comment-content">
                <p id="comment-text">{{comment.user}}  <span id="date">{{comment.updated_at}}</span></p>
                <p>{{comment.content}}</p>
            </div>
            <div>
                <p>수정</p>

            </div>
        </div>
        <hr>
    </div>
    
    
    
</div>
</template>

<script>
export default {
    name: 'CommentList',
    props: ['comments'],
    data() {
        return {
            isUser: false
        }
    },
    computed: {
    }

}
</script>

<style scoped>
#comment {
    display: flex;
    justify-content: left;
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

</style>