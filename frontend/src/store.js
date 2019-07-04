import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    players: [],
    events: [],
    isLoggedIn: false
  },
  mutations: {
    setPlayers (state, payload) {
      state.players = payload
    },
    setEvents (state, payload) {
      state.events = payload
    }
  },
  actions: {
    async fetchPlayers ({ commit }) {
      commit('setPlayers', (await axios.get('http://localhost:6543/player/all')).data)
    },
    async fetchEvents ({ commit }) {
      commit('setEvents', (await axios.get('http://localhost:6543/event/all')).data)
    }
  },
});
