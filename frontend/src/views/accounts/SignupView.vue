<template>
    <div id="signup">
        <h1>Sign Up</h1>
        <b-form-group class="mb-2" label="아이디" label-for="username" description="아이디를 작성해주세요">
            <b-form-input type="text" id="username" v-model="signupData.username"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="비밀번호" label-for="password1" description="비밀번호를 작성해주세요">
            <b-form-input type="password" id="password1" v-model="signupData.password1"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="비밀번호 확인" label-for="password2" description="비밀번호를 다시 한번 작성해주세요">
            <b-form-input type="password" id="password2" v-model="signupData.password2"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="좋아하는 장르" label-for="favorite" description="좋아하는 영화 장르를 알려주세요">
            <b-form-select :options="options" id="favorite" v-model="signupData.favorite"></b-form-select>
        </b-form-group>
        <b-button @click="signup(signupData)" class="btn ">Sign Up</b-button>

        {{ signupData.favorites}}
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: "SignupView",
    data() {
        return {
        signupData: {
            username: null,
            password1: null,
            password2: null,
            favorite: null,
        },
        options: [
          { value: 'Adventure', text: 'Adventure' },
          { value: 'Fantasy', text: 'Fantasy' },
          { value: 'Animation', text: 'Animation' },
          { value: 'Drama', text: 'Drama' },
          { value: 'Horror', text: 'Horror' },
          { value: 'Action', text: 'Action' },
          { value: 'Comedy', text: 'Comedy' },
          { value: 'History', text: 'History' },
          { value: 'Western', text: 'Western' },
          { value: 'Thriller', text: 'Thriller' },
          { value: 'Crime', text: 'Crime' },
          { value: 'Documentary', text: 'Documentary' },
          { value: 'Science Fiction', text: 'Science Fiction' },
          { value: 'Mystery', text: 'Mystery' },
          { value: 'Music', text: 'Music' },
          { value: 'Romance', text: 'Romance' },
          { value: 'Family', text: 'Family' },
          { value: 'War', text: 'War' },
          { value: 'TV Movie', text: 'TV Movie' },
        ]
        }
    },
    methods: {
        ...mapActions(["signup"])
    }
}

</script>

<style>
#signup {
    text-align: left;
    width: 50%;
    margin: auto;
}
h1 {
    text-align: center;
}
</style>