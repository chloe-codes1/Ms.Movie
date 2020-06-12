<template>
    <div id="signup">
        <h1>회원가입</h1>
        <b-form-group class="mb-2" label="아이디" label-for="username" description="아이디를 작성해주세요">
            <b-form-input type="text" id="username" v-model="signupData.username"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="비밀번호" label-for="password1" description="비밀번호를 작성해주세요">
            <b-form-input type="password" id="password1" v-model="signupData.password1"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="비밀번호 확인" label-for="password2" description="비밀번호를 다시 한번 작성해주세요">
            <b-form-input type="password" id="password2" v-model="signupData.password2"> </b-form-input>
        </b-form-group>
        <b-button @click="signup" class="btn ">회원가입</b-button>
    </div>
</template>

<script>
export default {
    name: 'SignupView',
    data() {
        return{
            signupData : {
                username: null,
                password1: null,
                password2: null
            }
        }
    },
    methods: {
        signup() {
            this.$emit('submit-signup-data', this.signupData)
        }
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