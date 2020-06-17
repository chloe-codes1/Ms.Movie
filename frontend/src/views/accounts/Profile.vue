<template>
  <div>
    <h1> 여긴 프로파일 페이지~~~ 하하하~~</h1>
    <b-avatar></b-avatar>
    <div v-if="account">
      <p> 아이디: {{account.username}}</p>
      <p> 장르: {{account.favorites}}</p>
    </div>
    <div v-if="othersAccount">
       <p> 아이디: {{othersAccount.username}}</p>
      <p> 장르: {{othersAccount.favorite}}</p>
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
    this.getAccount()
    this.getOthersAccount(this.id)
  }
}
</script>

<style>

</style>