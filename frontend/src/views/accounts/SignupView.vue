<template>
  <div id="signup">
    <h4>Sign Up</h4>
    <b-form-group class="mb-2" label="Username" label-for="username" description="Type username">
      <b-form-input type="text" id="username" v-model="signupData.username"></b-form-input>
    </b-form-group>
    <b-form-group class="mb-2" label="Password" label-for="password1" description="Type password">
      <b-form-input type="password" id="password1" v-model="signupData.password1"></b-form-input>
    </b-form-group>
    <b-form-group
      class="mb-2"
      label="Confirm password"
      label-for="password2"
      description="Retype password"
    >
      <b-form-input type="password" id="password2" v-model="signupData.password2"></b-form-input>
    </b-form-group>
    <b-button @click="signup(signupData)" id="submitButton">Sign Up</b-button>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "SignupView",
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    };
  },
  methods: {
    ...mapActions(["signup"])
  }
};
</script>

<style scoped>
#signup {
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