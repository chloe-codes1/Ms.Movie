<template>
  <div>
    <b-avatar></b-avatar>
    <div v-if="account">
      <p> Username: {{account.username}}</p>
      <p> Genre: {{account.favorites}}</p>
    </div>
    <div v-if="othersAccount">
      <p> Username: {{othersAccount.username}}</p>
      <p> Genre: {{othersAccount.favorite}}</p>
    </div>                                                                                                                                                                                                                                                                                                                                                                                                                                         
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  name: 'Profile',
  computed: {
    ...mapState(['account', 'othersAccount'])
  },
  data() {
    return{
      // variable routing 으로 가져오깅
      id: this.$route.params.id
    }
  },
  methods: {
    ...mapActions(['getAccount', 'getOthersAccount'])
  },
  created() {
    // this.getAccount()
    this.getOthersAccount(this.id)
  }
}
</script>

<style>

</style>