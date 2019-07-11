<template>
<div class="container">
    <div class="row">
        <div class="col-sm-12">
            <div class="container">
                <h4>events</h4>
                <template v-for="event in events">
                  <!-- <button  :key="event.id">Go to Event</button> -->
                  <event-card @click.native="goToEvent(event.id)" :key="event.id" :event="event" ></event-card>
                  <hr>
                </template>
            </div>
        </div>
        <!-- <div class="col-sm-4" >
          <div class="container">
            <h4>players</h4>
          <template v-for="player in this.$store.state.players">
            <player-card :key="player.id" :player="player"></player-card>
            <hr :key="player">
          </template>
          </div> -->
    </div>
</div>
</template>

<script>
import PlayerCard from '@/components/PlayerCard.vue'
import EventCard from '@/components/EventCard.vue'
import { mapState } from 'vuex'
// import axios from 'axios'

export default {
  name: 'home',
  created() {
    // this.$store.dispatch('fetchPlayers')
    this.$store.dispatch('fetchEvents')
  },
  computed: {
    ...mapState(['events',]),
  },
  components: {
     EventCard,
  },
  methods: {
    goToEvent: function(event_id) {
      this.$router.push({
        name: 'event',
        params: { id: event_id }
      })
      // console.log('event clicked!', event_id)
    }
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

</style>
