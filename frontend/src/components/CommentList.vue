<template>
<div>
    
    <b-list-group>
        <b-list-group-item v-for="comment in comments" :key="comment.id">
            <div>
                {{comment.content}}
                {{comment.user}}
            </div>
        </b-list-group-item>
    </b-list-group>
</div>
</template>

<script>
export default {
    name: 'CommentList',
    props: ['comments'],

}
</script>

<style>

</style>