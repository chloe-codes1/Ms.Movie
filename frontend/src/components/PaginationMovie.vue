<template>
 <div class="app">
   <ul>
   <div v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="limit">
     <li v-for="movie in movies" :key="movie.id">    
        {{movie}}
     </li>
     </div>
   </ul>
   </div>
 
</template>
<script>
import axios from "axios"
const SERVER = "http://localhost:8000"

export default {
 name: "PaginationMovie",
 data() {
   return {
     movies: [],
     busy: false,
     start: 1,
     limit: 10,
   };
 },
 methods: {
  
   loadMore() {
      this.busy = true
      const end = this.start+this.limit
      while (this.start < end) {
          axios.get(SERVER + `/movies/${this.start}`)
            .then(res => {
                console.log(res.data)
                this.movies.push(res.data)
            })
            this.start ++
      }
        this.busy = false
     }
 },
 created() {
 this.loadMore() 
 }
}
</script>


<style>

</style>