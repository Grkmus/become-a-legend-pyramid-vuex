<template>
<div class="container">
    <div class="card">
      <div class="row no-gutters">
        <div class="col-md-4">
          <img src="https://www.mercurynews.com/wp-content/uploads/2018/09/BNG-L-WARRIORS-0925-131.jpg?w=525" class="card-img" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h2 class="card-title">{{player.name}} {{player.surname}}</h2>
            <p class="card-text">@{{player.username}}</p>
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
                <li class="list-group-item">Age:</li>
                <li class="list-group-item">Weight:</li>
                <li class="list-group-item">Height:</li>
                <li class="list-group-item">Location:</li>
                <li class="list-group-item">Role Preference:</li>
                <li class="list-group-item">Overall Rating:</li>
              </ul>
          </div>
        </div>
        <div class="col-md-8">
            <div class="card" style="height:150px">
              <p>events</p>
            </div>
            <hr>
            <div class="card" style="height:150px">
              <p>events</p>
            </div>
            <hr>
            <div class="card" style="height:150px">
              <p>events</p>
            </div>
              <!-- <div class="list-group" v-for="event in events">
                  <dailyEvent :data="event" :key="event._id" v-if="event._id"></dailyEvent>
                  <hr/>
              </div> -->

        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router.js'

export default {
  name: 'profile',
  async created(){
    await this.fetchPlayer(this.$route.params.id)
  },
  data(){
    return {
      player: {}
    }
  },
  methods: {
    fetchPlayer: async function(id) {
      const res = await axios.get(`http://localhost:6543/player/${id}`).catch(err => {
        router.push({
          name: 'notfound',
          params: { message: err.message }
        })
      })
      console.log(res)
      this.player = res.data
    } 
  }

}
</script>

<style>


</style>
