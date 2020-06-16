<template>
<div id="review-list">
    <h1>Review List</h1>
    <b-button><router-link :to="'/reviews/' + id + '/create'">New</router-link></b-button>
    <table class="table table-hover table-sm">
        <thead>
            <tr>
                <th scope="col" width="10%">ID</th>
                <th cope="col" width="75%;">Title</th>
                <th scope="col">User</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="review in reviews" :key="review.id" :review='review'>
                <th scope="row">{{review.id}}</th>
                <b-link :href="`http://localhost:8080/reviews/detail/${review.id}`"><td>{{review.title}}</td></b-link>
                <td>{{review.user}}</td>    
            </tr>
        </tbody>
    </table>
</div>
</template>

<script>

export default {
    name: 'ReviewList',
    props: ['reviews'],

    components: {
        
    },
    methods: {

    }
}
</script>

<style scoped>
a:link, a:hover, a:active, a:visited{
    color: black;
    text-decoration: none;
}
thead {
    background-color: #3fb883;
    color: white;
}
#review-list {
    width: 75%;
    margin: 0 auto;
}
</style>