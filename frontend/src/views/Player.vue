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

.emp-profile{
    padding: 3%;
    margin-top: 3%;
    margin-bottom: 3%;
    border-radius: 0.5rem;
    background: #fff;
}
.profile-img{
    text-align: center;
}
.profile-img img{
    width: 70%;
    height: 100%;
}
.profile-img .file {
    position: relative;
    overflow: hidden;
    margin-top: -20%;
    width: 70%;
    border: none;
    border-radius: 0;
    font-size: 15px;
    background: #212529b8;
}
.profile-img .file input {
    position: absolute;
    opacity: 0;
    right: 0;
    top: 0;
}
.profile-head h5{
    color: #333;
}
.profile-head h6{
    color: #0062cc;
}
.profile-edit-btn{
    border: none;
    border-radius: 1.5rem;
    width: 70%;
    padding: 2%;
    font-weight: 600;
    color: #6c757d;
    cursor: pointer;
}
.proile-rating{
    font-size: 12px;
    color: #818182;
    margin-top: 5%;
}
.proile-rating span{
    color: #495057;
    font-size: 15px;
    font-weight: 600;
}
.profile-head .nav-tabs{
    margin-bottom:5%;
}
.profile-head .nav-tabs .nav-link{
    font-weight:600;
    border: none;
}
.profile-head .nav-tabs .nav-link.active{
    border: none;
    border-bottom:2px solid #0062cc;
}
.profile-work{
    padding: 14%;
    margin-top: -15%;
}
.profile-work p{
    font-size: 12px;
    color: #818182;
    font-weight: 600;
    margin-top: 10%;
}
.profile-work a{
    text-decoration: none;
    color: #495057;
    font-weight: 600;
    font-size: 14px;
}
.profile-work ul{
    list-style: none;
}
.profile-tab label{
    font-weight: 600;
}
.profile-tab p{
    font-weight: 600;
    color: #0062cc;
}
</style>
