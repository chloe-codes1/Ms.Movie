<template>
    <div>
        <b-button><router-link :to="'/reviews/' + id + '/create'">New</router-link></b-button>
        <ReviewList :reviews="reviews"/>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import ReviewCreate from '@/components/ReviewCreate.vue'
import ReviewList from '@/components/ReviewList.vue'
export default {
    name: 'ReviewListCreate',
    data() {
        return {
            id: this.$route.params.id,
        }
    },
    components: {
        ReviewList
    },
    computed: {
        ...mapState(['reviews'])

    },
    methods: {
        ...mapActions(['getReviews']),
    },
    created() {
        this.getReviews(this.id)
    }

}
</script>

<style>

</style>