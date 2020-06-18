<template>
<div>
    <div id="review-list">
        <div>
            <router-link :to="'/reviews/' + id + '/create'"><b-button>New</b-button></router-link>
        </div>
        <table class="table table-hover table-md">
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
                    
                    <b-link :href="`http://localhost:8080/reviews/${id}/detail/${review.id}`"><td>{{review.title}}</td></b-link>
                    <td>{{review.user}}</td>    
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>
<script>
export default {
    name: 'ReviewList',
    props: ['reviews',],
    data() {
        return {
            id: this.$route.params.id
        }
    },
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
    width: 80%;
    margin: 30px auto;
}
button {
    background-color: white;
    color: #3fb883;
    border: 1px solid #3fb883;
    float: left;
    margin-bottom: 10px;
}
button:hover {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
</style>