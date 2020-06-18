<template>
<div id="wrapper">
    <nav id="sidebar">
        <div class="sidebar-header" v-if="starredMovie">
            <h4>Review For</h4>
            <h4>{{starredMovie.title}}</h4>
        </div>
        <hr>
        <div class="sidebar-item-active" v-if="!path.includes('create') & !path.includes('detail')">
            <h5 style="font-weight:bold;">Review List</h5>
        </div>
        <div class="sidebar-item" v-else>
        <router-link :to="'/reviews/'+ id"><h5>Review List</h5></router-link>
        </div>
        
        <div class="sidebar-item-active" v-if="path.includes('create')">
        <h5 style="font-weight:bold;">Review Create</h5>
        </div>
        <div class="sidebar-item" v-else>
        <router-link :to="'/reviews/'+ id + '/create'"><h5>Review Create</h5></router-link>
        </div>
    </nav>
      
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
    name: 'ReviewSidebar',
    data() {
        return {
            id: this.$route.params.id,
            path: this.$route.path,
        }
    },
    computed: {
        ...mapState(['starredMovie'])
    },
    methods: {
        ...mapActions(['fetchMovie'])

    },
    created() {
        this.fetchMovie(this.id)
    }
}
</script>

<style scoped>
/* background-color: #3baa7a; */
#wrapper {
    padding: 0;
    
}
h5 {
    margin: 0;
    text-decoration: none;
    color: white;
}
h5:hover {
    font-weight: bold;
}
a:hover {
    text-decoration: none;
}
.sidebar-item-active {
    padding: 13px 0;
    width: 100%;
    height: 50px;
    background-color: #3baa7a;
    font-weight: bold;
}
.sidebar-item {
    padding: 13px 0;
    width: 100%;
    height: 50px;
    
}
#sidebar {
    position: fixed;
    height: 100vh;
    width: 200px;
    padding: 0;
    background-color: #3fb883;
    color: white;
}

.sidebar-header {
    margin: 10px;
}
</style>