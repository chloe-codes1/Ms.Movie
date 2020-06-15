<template>
<div id="review_list">
    <h1>Review List</h1>
    <ReviewCreate/>
    <b-table hover :items="reviews"></b-table>
</div>
</template>

<script>
import ReviewCreate from '@/components/ReviewCreate.vue'
export default {
    name: 'ReviewList',
    props: ['reviews'],
    components: {
        ReviewCreate,
    },
    methods: {
        createVue() {
            
        }

    }
}
</script>

<style>

</style>