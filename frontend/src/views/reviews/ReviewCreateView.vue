<template>
    <div>
        <h1>Community</h1>
        <p class="text-left">Title</p>
        <b-form-input v-model="reviewData.title" type="text" id="title" placeholder="영화와 관련된 자유로운 의견을 남겨주세요."></b-form-input>
        <p class="text-left mt-3">Content</p>
        <b-form-textarea v-model="reviewData.content" id="content" cols="30" rows="10" placeholder=""></b-form-textarea>
        <b-button @click="createReview">작성하기</b-button>  
    </div>
</template>

<script>
import axios from 'axios'
const SERVER = 'http://localhost:8000'

export default {
    name: 'ReviewCreateView',
    data() {
        return {
            reviewData : {
                title: null,
                content: null,
                image: null
            }
        }
    },
    method: {
        createReview() {
           const config = {
                headers: {
                Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.post(`${SERVER}/reviews/`, this.reviewData, config)
                .then(res => {
                console.log(res.data)
                this.$router.push('/reviews')
            })
            .catch(err => console.log(err.res.data))
        }
    },
}
</script>

<style>

</style>