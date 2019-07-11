<template>
<div class="container">
    <div class="card">
      <div class="row no-gutters">
        <div class="col-md-4">
          <img src="https://www.mercurynews.com/wp-content/uploads/2018/09/BNG-L-WARRIORS-0925-131.jpg?w=525" class="card-img" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h2 class="card-title">{{ player.name }} {{ player.surname }}</h2>
            <p class="card-text">@{{ player.username }}</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            <a class="btn-lg btn-danger" :href="'/player/' + player.id + '/quiz'">Fill out the quick form to play basketball!</a>
          </div>
        </div>
      </div>
    </div>
    <br>
    <div class="row">
        <div class="col-md-4">
          <div class="card">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">Age: </li>
                <li class="list-group-item">Weight:</li>
                <li class="list-group-item">Height:</li>
                <li class="list-group-item">Location:</li>
                <li class="list-group-item">Role Preference:</li>
                <li class="list-group-item">Overall Rating:</li>
              </ul>
          </div>
        </div>
        <div class="col-md-8">
            <!-- <div class="card" style="height:150px">
              <p>events</p>
            </div>
            <hr>
            <div class="card" style="height:150px">
              <p>events</p>
            </div>
            <hr>
            <div class="card" style="height:150px">
              <p>events</p>
            </div> -->
            <div class="list-group" :key="event.id" v-for="event in player.events">
                <event-card :event="event" :key="event._id"></event-card>
                <hr/>
            </div>

        </div>
    </div>
  </div>
</template>

<script>
import router from '../router.js'
import EventCard from '@/components/EventCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'player',
  async created(){
    await this.$store.dispatch('fetchPlayer', this.$route.params.id)
  },
  computed: {
    ...mapState(['player'])
  },
  components: {
    EventCard,
  },
}
</script>

<style>

</style>
