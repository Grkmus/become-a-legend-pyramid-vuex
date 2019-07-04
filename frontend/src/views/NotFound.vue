<template>
<div class="container">
    <h1>Bad Request!</h1>
    <h4>{{message}}</h4>
</div>
</template>

<script>
// import Player from '@/components/PlayerCard.vue'
// import dailyEvent from '@/components/EventCard.vue'
// import axios from 'axios'

export default {
  name: 'notfound',
  data(){
    return {
      message: this.$route.params.message
    }
  }, 
}
</script>

<style>
h4 {
  border-bottom: solid 0.1rem lightgrey
}
.vertical-line {
  border-left: solid 0.1rem lightgrey;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
