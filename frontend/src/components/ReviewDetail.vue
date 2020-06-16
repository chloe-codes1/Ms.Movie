<template>  
<div>
    <h3>Review For {{reviews.movie_title}}</h3>
    <div id="review-detail">
        <div id="title-content">
            <div id="empty"></div>
            <div>
                <h5>{{reviews.title}}</h5>
                <div>
                    <b-form-rating id="rating-inline" v-model="divideRating" inline no-border variant="warning" readonly></b-form-rating>
                    <label for="rating-inline"><h5>{{reviews.rating}}</h5></label>
                </div>
            </div>
            <div>
                <p>{{reviews.updated_at}}</p>
            </div>
           
        </div>
        <hr>
        <div>
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

label {
    color: red;
}
</style>