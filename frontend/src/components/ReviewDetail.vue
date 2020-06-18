<template>  
<div>
    <h4>Review For {{reviews.movie_title}}</h4>
    <hr>
    <div id="review-detail">
        <div id="title-content">
            <div id="empty">
                <i class="far fa-thumbs-up fa-md" aria-hidden="true" id="likeCount"> {{likeCount}} </i>
                <i class="far fa-thumbs-down fa-md" aria-hidden="true"> {{dislikeCount}} </i>
            </div>
            <div>
                <h5>{{reviews.title}}</h5>
                
                <b-form-rating id="rating-inline" v-model="divideRating" inline no-border variant="warning" readonly></b-form-rating>
                <label for="rating-inline"><p>{{reviews.rating}}</p></label>
            </div>
            <div>
                <p>by {{reviews.username}}</p>
                <p id="date">{{reviews.updated_at}}</p>
            </div>
           
        </div>
        <hr>
        <div id="review-content" style="white-space: pre-line;">
            {{reviews.content}}
        </div>
        <hr>
    </div>
</div>
</template>

<script>


export default {
    name: 'ReviewDetailView',
    props: ['reviews', 'likeCount', 'dislikeCount'],
    data() {
        return {
            id: this.$route.params.id,
        }
    },
    computed: {
         divideRating() {
            return this.reviews.rating/2
        },
    },
    
    
}
</script>

<style scoped>
h4 {
    margin-top: 30px;
}
#empty {
    width: 85px;
}
#title-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}
#review-content {
    min-height: 400px;
}
label {
    color: red;
}
p {
    margin-bottom: 0;
}
#rating-inline {
    padding: 0;
    margin: 0;
}
#date {
    margin-bottom: 5px;
}
i {
    margin: 5px;
}
</style>