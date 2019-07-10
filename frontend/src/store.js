import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jwt from 'jsonwebtoken';

// const request = axios.create({
//   baseURL: 'http://localhost:6543',
// });
// const AUTH_TOKEN = `Bearer ${localStorage.token}`
// Alter defaults after instance has been created
const authHeaderSet = {
  headers: {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  },
}

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    player: {},
    players: [],
    events: [],
  },
  getters: {
    isLoggedIn: (state) => {
      if (state.user === {} || state.user === null) {
        return false
      }
      return true
    },
  },
  mutations: {
    setPlayer(state, payload) {
      state.player = payload
    },
    setPlayers(state, payload) {
      state.players = payload
    },
    setEvents(state, payload) {
      state.events = payload
    },
    setUser(state, payload) {
      state.user = payload
    },
    setUserLoggedOut(state) {
      state.user = null
    },
  },
  actions: {
    async fetchPlayer({ commit }, id) {
      commit('setPlayer', (await axios.get(`http://localhost:6543/player/${id}`, authHeaderSet)).data)
    },
    async fetchPlayers({ commit }) {
      commit('setPlayers', (await axios.get('http://localhost:6543/player/all', authHeaderSet)).data)
    },
    async fetchEvents({ commit }) {
      console.log('fetchEvents')
      commit('setEvents', (await axios.get('http://localhost:6543/event/all', authHeaderSet)).data)
    },
    async getUser({ commit }) {
      const result = await jwt.verify(localStorage.token, 'secret', (err, decoded) => {
        if (err) {
          console.log(err)
          return err
        }
        return decoded
      })
      commit('setUser', result)
    },
    getUserLoggedOut({ commit }) {
      commit('setUserLoggedOut')
    },
    // async attendToEvent({ commit }, ids) {
    //   console.log(ids.eventId, ids.userId)
    //   commit('attendToEvent', (await axios.get(`http://localhost:6543/player/${id}/event/${eventId}`, authHeaderSet)).data)
    //   // commit('attendToEvent')
    // },
  },
});
