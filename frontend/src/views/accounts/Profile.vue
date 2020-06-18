<template>
  <div class="container mt-4">
    <div class="row">
      <div class="col-xl-6">
        <b-avatar class="mr-3" size="4rem"></b-avatar>
        <span v-if="othersAccount">Username: {{othersAccount.username}}</span>
      </div>
      <div class="col-xl-6">
        <p v-if="othersAccount">Genre: {{othersAccount.favorite}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Profile",
  computed: {
    ...mapState(["othersAccount"])
  },
  data() {
    return {
      id: this.$route.params.id
    };
  },
  methods: {
    ...mapActions(["getOthersAccount"])
  },
  created() {
    this.getOthersAccount(this.id);
  }
};
</script>

<style>
</style>