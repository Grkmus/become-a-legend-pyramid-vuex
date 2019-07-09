import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import jwt from 'jsonwebtoken';

const request = axios.create({
  baseURL: 'http://localhost:6543',
});

const AUTH_TOKEN = `Bearer ${localStorage.token}`
// Alter defaults after instance has been created
request.defaults.headers.common['Authorization'] = AUTH_TOKEN;

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: null,
    player: {},
    players: [],
    events: [],
    isLoggedIn: false,
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
    setUserId(state, payload) {
      state.userId = payload
    },
    setUserLoggedIn(state) {
      state.isLoggedIn = true
    },
    setUserLoggedOut(state) {
      state.isLoggedIn = false
      state.userId = null
    },
  },
  actions: {
    async fetchPlayer({ commit }, id) {
      commit('setPlayer', (await request.get(`/player/${id}`)).data)
    },
    async fetchPlayers({ commit }) {
      commit('setPlayers', (await request.get('/player/all')).data)
    },
    async fetchEvents({ commit }) {
      commit('setEvents', (await request.get('/event/all')).data)
    },
    getUserId({ commit }) {
      const result = jwt.verify(localStorage.token, 'secret', (err, decoded) => {
        if (err) {
          return err
        }
        return decoded
      })
      commit('setUserId', result)
    },
    getUserLoggedIn({ commit }) {
      commit('setUserLoggedIn')
    },
    getUserLoggedOut({ commit }) {
      commit('setUserLoggedOut')
    },
  },
});
