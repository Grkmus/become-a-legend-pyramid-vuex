<template>
<div id="app">
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link class="navbar-brand" to="/">Become A Legend</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor02">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link 
            v-if="!isLoggedIn" 
            class="btn btn-danger" 
            to="/register">
            Sign Up
          </router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="!isLoggedIn" class="nav-link" to="/login">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/about">About</router-link>
        </li>
        <li class="nav-item">
          <a href="#" v-if="isLoggedIn" @click="logout" class="nav-link">logout</a>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search">
        <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
  <router-view></router-view> 
</div>

</template>

<script>
import { mapState, mapGetters } from 'vuex'
import router from './router'


export default {
  name: 'navbar',
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  methods: {
    logout: function() {
      localStorage.clear()
      this.$store.dispatch('getUserLoggedOut').then(() => {
        router.push('/')
      })
    },
  },
}

</script>

<style>

</style>