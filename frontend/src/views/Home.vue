<template>
<div class="container">
    <div class="row">
        <div class="col-sm-8">
            <div class="container">
                <h4>events</h4>
                <template v-for="event in this.$store.state.events">
                  <event-card :key="event.id" :event="event" ></event-card>
                  <hr>
                </template>
            </div>
        </div>
        <div class="col-sm-4" >
          <div class="container">
            <h4>players</h4>
          <template v-for="player in this.$store.state.players">
            <player-card :key="player.id" :player="player"></player-card>
            <hr>
          </template>
          </div>

        </div>
    </div>
</div>
</template>

<script>
import PlayerCard from '@/components/PlayerCard.vue'
import EventCard from '@/components/EventCard.vue'
import { mapState, mapActions } from 'vuex'
// import axios from 'axios'

export default {
  name: 'home',
  created(){
    this.$store.dispatch('fetchPlayers')
    this.$store.dispatch('fetchEvents')
    // this.fetchEvents()
  },
  data() {
    return {
      // events: [],
      // players: []
    }
  },
  computed: {
    ...mapState(['players','events']),
  },
  components: {
     EventCard,
     PlayerCard
  },
  methods:{
    // fetchPlayers: async function(){
    //   await axios.get('http://localhost:6543/player/all')
    //     .then(res => { 
    //       this.players = res.data
    //       this.$store.dispatch('fetchPlayers', res.data) 
    //     })
    // },
    // fetchEvents: async function(){
    //   const res = await axios.get('http://localhost:6543/event/all')
    //   this.events = res.data
    // },
  }
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
