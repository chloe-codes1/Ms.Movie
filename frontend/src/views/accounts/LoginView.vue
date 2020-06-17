<template>
    <div id="login">
        <h4>Login</h4>
        <b-form-group class="mb-2" label="ID" label-for="username" description="Type username">
            <b-form-input type="text" id="username" v-model="loginData.username"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="Password" label-for="password" description="Type password">
            <b-form-input type="password" id="password" v-model="loginData.password" @keyup.enter="login(loginData)"> </b-form-input>
        </b-form-group>
        <b-button @click="login(loginData)" id="submitButton">Login</b-button>
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
    margin: 30px auto;
}
h3 {
    text-align: center;
}
#submitButton {
    background-color: #3fb883;
    color: white;
    border: 1px solid #3fb883;
}
#submitButton:hover {
    background-color: #3baa7a;
}
</style>