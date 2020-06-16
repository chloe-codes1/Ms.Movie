<template>
    <div id="login">
        <h1>로그인</h1>
        <b-form-group class="mb-2" label="아이디" label-for="username" >
            <b-form-input type="text" id="username" v-model="loginData.username" placeholder="아이디를 작성해주세요"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="비밀번호" label-for="password" >
            <b-form-input type="password" id="password" v-model="loginData.password" placeholder="비밀번호를 작성해주세요"> </b-form-input>
        </b-form-group>
        <b-button @click="login(loginData)" class="btn ">로그인</b-button>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: "LoginView",
    data() {
        return {
            loginData: {
                username: null,
                password: null
            }
        }
    },
    methods: {
        ...mapActions(['login'])
    }
}

</script>

<style scoped>
#login {
    text-align: left;
    width: 50%;
    margin: auto;
}
h1 {
    text-align: center;
}
</style>