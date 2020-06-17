<template>
    <div id="signup">
        <h4>Sign Up</h4>
        <b-form-group class="mb-2" label="Username" label-for="username" description="Type username">
            <b-form-input type="text" id="username" v-model="signupData.username"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="Password" label-for="password1" description="Type password">
            <b-form-input type="password" id="password1" v-model="signupData.password1"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="Confrim password" label-for="password2" description="Retype password">
            <b-form-input type="password" id="password2" v-model="signupData.password2"> </b-form-input>
        </b-form-group>
        <b-form-group class="mb-2" label="Favorite genre" label-for="favorite" description="Choose your favorite genre. We'll recommend movies based on your choice.">
            <b-form-select :options="options" id="favorite" v-model="signupData.favorite"></b-form-select>
        </b-form-group>
        <b-button @click="signup(signupData)" id="submitButton">Sign Up</b-button>

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