<template>
    <div>
        <p>{{reviews}}</p>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: 'ReviewDetailView',
    data() {
        return {
            id: this.$route.params.id,
            
        }
    },
    computed: {
        ...mapState(['reviews'])

    },
    methods: {
        ...mapActions(['getReview'])

    },
        
    created() {
        this.getReview(this.id)
    }
}
</script>

<style>

</style>