<template>
<div class="event">
    <div class="container">
        <div class="container">
            <nav aria-label="...">
                <ul class="pagination pagination-lg">
                    <li class="page-item" v-bind:class="{ active: event.phase == 'phase1', disabled: event.phase != 'phase1' }"><a class="page-link" href="#" tabindex="-1">Phase 1</a></li>
                    <li class="page-item" v-bind:class="{ active: event.phase == 'phase2', disabled: event.phase == 'phase3' }"><a class="page-link" href="#" @click.once="fetchEventPhase2">Phase 2</a></li>
                    <li class="page-item" v-bind:class="{ active: event.phase == 'phase3', disabled: event.phase != 'phase3' }"><a class="page-link" href="#">Phase 3</a></li>
                </ul>
            </nav>
        </div>
        <div class="container">
            <div class="card" id="eventTitle">
                <div class="card-body">
                    <h1 class="card-title">{{event.name}} Daily Event</h1>
                    <h6 class="card-subtitle mb-2 text-muted">Date: {{realDate}} </h6>
                    <h6 class="card-subtitle mb-2 text-muted">Time: {{time}}</h6>
                    <h6 class="card-subtitle mb-2 text-muted">Location: {{event.location}}</h6>
                </div>
            </div>
        </div>
        <!-- <h2 v-if="event.phase == 'phase1'">{{attendeesCount}} people has joined</h2><img src="@/assets/giphy.gif" v-if="loading" /> -->
        <div class="row" v-if="!loading">
            <div :key="player" v-for="player in event.attendees" v-if="event.phase == 'phase1'"><img class="player" :src="player.imageURL" @click="goToPlayer(player._id)" />
                <p style="text-align: center;">{{player.name}} {{player.ratingEvaluation}}</p>
            </div>
            <div class="col-sm-4" v-if="event.phase == 'phase2'">
                <div class="card" id="players">
                    <div class="card-body">
                        <h2>{{attendeesToBeSelectedCount}} people to be picked</h2>
                        <div class="row"><template v-for="player in event.attendeesToBeSelected"><playerEventCard :data="player" :key="player._id" @selectPlayer="handleSelection"> </playerEventCard></template></div>
                    </div>
                </div>
            </div>
            <div class="col-sm-8 teams" v-if="event.phase == 'phase2'">
                <div class="card" id="teams">
                    <div class="card-body">
                        <h2>{{teamCount}} teams gonna play</h2>
                        <div class="row">
                            <div class="col-sm-6" v-for="team in event.teams">
                                <team :data="team" ref="teams" @skipTheTurn="handleSkipTurn"></team>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="row">
                    <div class="col-sm-6 teams" v-if="event.phase == 'phase3'">
                        <div class="card" id="teams">
                            <div class="card-body">
                                <h2>Teams</h2>
                                <div class="row">
                                    <div class="col-sm-6" :key="team._id" v-for="team in event.teams">
                                        <TeamPhase3 :data="team"  ref="teams">vs</TeamPhase3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6" v-if="event.phase == 'phase3'">
                        <div class="card" id="teams">
                            <div class="card-body">
                                <h2>Schedule</h2>
                                <div class="row">
                                    <div :key="team.id" class="col-sm-12" v-for="team in event.teams">
                                        <h4>{{team.name}} vs {{team.name}}</h4>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

</template>

<script>
import axios from 'axios'
import Player from '@/components/PlayerCard.vue'
import PlayerEventCard from '@/components/PlayerEventCard.vue'
import Team from '@/components/TeamCard.vue'
import TeamPhase3 from '@/components/TeamCardPhase3.vue'
import router from '@/router.js'

export default {
  name: 'event',
  created(){
    this.fetchEvent(this.$route.params.id)
    var unwatch = this.$watch('event.turn', (newVal, oldVal) => {
      newVal = newVal % this.event.teams.length
      oldVal = oldVal % this.event.teams.length
      this.$refs.teams[oldVal].isActive = false
      this.$refs.teams[newVal].isActive = true
      if(this.isTeamFull(newVal) && this.teamQuota != 0) this.event.turn++
    })
    this.unwatch = unwatch
  },
  data(){
    return {
      event: {
        teams: [
          {players: Array}
        ],
        attendeesToBeSelected: [{
          ratingEvaluation: Number
        }],
        attendees: Array,
        turn: 0,
        phase: String
      },
      loading: false,
      unwatch: null
    }
  },
  mounted(){
    this.$watch('event', (newVal, oldVal) => {
      if (newVal.phase == 'phase2') this.startPlayerSelection()
    })

  },
  components: {
    Player,
    Team,
    TeamPhase3,
    PlayerEventCard,
  },
  methods: {
    fetchEvent: async function(id) {
      this.loading = true
      const res = await axios.get(`https://backend.something.gt/daily-event/${id}`)
      this.event = res.data
      this.loading = false
    },
    fetchEventPhase2: async function(id) {
      this.loading = true
      const res = await axios.post(`https://backend.something.gt/daily-event/phase2/`, {_id: this.event._id})
      this.event = res.data
      this.teams = res.data.teams
      this.loading = false
    },
    startPlayerSelection: function() {
      const counter = this.event.turn % this.event.teams.length
      this.$refs.teams[counter].$data.isActive = true
    },
    goToPlayer: function(_id) {
      router.push({
          name: 'player',
          params: { id: _id }
      })
    },
    isAbleToPick: function(turn) {
      this.event.attendeesToBeSelected.forEach(player => {
        if(this.event.teams[turn].credits < player.ratingEvaluation) {
          alert('There is no player that you can pick.. sorry..')
          return false
        } else return true
      });
    },
    isTeamFull: function(turn){
      if(this.event.teams[turn].players.length == 3) {
        console.log('hobaa')
        return true
      } else return false
    },
    handleSkipTurn: async function() {
      this.event.turn++
      await axios.put(`https://backend.something.gt/daily-event/${this.event._id}`, this.event )
    },
    handleSelection: async function(id){
      const counter = this.event.turn % this.event.teams.length
      const indexPlayer = this.event.attendeesToBeSelected.findIndex(attendee => {
        return attendee._id.toString() == id.toString() 
      })
      const selectedPlayer = this.event.attendeesToBeSelected[indexPlayer]
      const selectedTeam = this.event.teams[counter]
      // if(selectedTeam.credits < selectedPlayer.ratingEvaluation) {
      //   alert('Your credit is not enough')
      //     throw new Error('Your credit is not enough')
      // }
      this.event.attendeesToBeSelected.splice(indexPlayer, 1)
      selectedTeam.credits = (selectedTeam.credits - selectedPlayer.ratingEvaluation).toFixed(2)
      selectedTeam.players.push(selectedPlayer)
      await axios.put(`https://backend.something.gt/team/${selectedTeam._id}`, selectedTeam)
      this.teamQuota--
      if(this.teamQuota == 0) {
        this.event.phase = 'phase3'
        this.unwatch()
        await axios.put(`https://backend.something.gt/daily-event/${this.event._id}`, this.event )
      }
      this.event.turn++
      await axios.put(`https://backend.something.gt/daily-event/${this.event._id}`, this.event )
    }
    // playerValidation: function(selectedPlayer, selectedTeam, indexPlayer) {
    //   return new Promise((resolve, reject) => {

    //     if(selectedTeam.credits < selectedPlayer.ratingEvaluation) {
    //       reject('Your credit is not enough')
    //       alert('Your credit is not enough')
    //       throw new Error('Your credit is not enough')
    //     }
    //     this.event.attendeesToBeSelected.splice(indexPlayer, 1)
    //     selectedTeam.credits = (selectedTeam.credits - selectedPlayer.ratingEvaluation).toFixed(2)
    //     selectedTeam.players.push(selectedPlayer)
    //     resolve(selectedTeam)
    //   })
    // }
  },
  computed: {
        realDate: function(){
            const eventTime =new Date(this.event.date)
            return eventTime.toLocaleDateString()
        },
        time: function(){
            const eventTime =new Date(this.event.date)
            return eventTime.toLocaleTimeString()
        },
        teamCount: function(){
            return this.event.teams.length
        },
        attendeesCount: function(){
          return this.event.attendees.length
        },
        attendeesToBeSelectedCount: function(){
          return this.event.attendeesToBeSelected.length
        },
        teamQuota: function(){
          let totalSelectedPlayers = 0
          this.event.teams.forEach((team) => {
            totalSelectedPlayers += team.players.length
          })
          return (this.event.teams.length * 3 - totalSelectedPlayers)
        }
        // get: function () {
        //   return result
        // },
        // // setter
        // set: function (newValue) {
        //   var names = newValue.split(' ')
        //   this.firstName = names[0]
        //   this.lastName = names[names.length - 1]
        // }
    },
  
}
</script>

<style>
#eventTitle {
  margin-bottom:15px;
}
#teams .card {
  margin: 10px;
}
/* .teams {
  padding-right: 15px;
} */
.card {
  text-align: center;
}
/* .card-body {
  padding: 10px;
} */

/* #players, #teams {
  border: 1px solid rgba(0,0,0,.125);
  border-radius: 0.25rem;
  margin: 10px;
  padding: 10px;
} */
/* .players {
  border-top: solid 1px lightgrey;
  padding: 10px;
} */
 .player {
  border-radius: 70px;
}

/*
.pagination {
  margin-left: 20px;
  margin-top: 10px;
}
.card {
  text-align: center;
  width: auto;
  margin: 20px;
} */
</style>
