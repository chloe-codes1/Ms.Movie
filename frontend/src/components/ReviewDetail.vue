<template>  
<div>
    <h3>Review For {{reviews.movie_title}}</h3>
    <div id="review-detail">
        <div id="title-content">
            <div id="empty"></div>
            <div>
                <h5>{{reviews.title}}</h5>
                <p>by {{reviews.username}}</p>
                <b-form-rating id="rating-inline" v-model="divideRating" inline no-border variant="warning" readonly></b-form-rating>
                <label for="rating-inline"><p>{{reviews.rating}}</p></label>
            </div>
            <div>
                <p id="date">{{reviews.updated_at}}</p>
            </div>
           
        </div>
        <hr>
        <div id="review-content">
            {{reviews.content}}
        </div>
        <hr>
    </div>
</div>
</template>

<script>


export default {
    name: 'ReviewDetailView',
    props: ['reviews'],
    data() {
        return {
            id: this.$route.params.id,   
        }
    },
    computed: {
         divideRating() {
            return this.reviews.rating/2
        }
    }
    
}
</script>

<style scoped>
#empty {
    width: 80px;
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
</style>