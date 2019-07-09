<template>
<div id="app">
    <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
        <router-link class="navbar-brand" to="/">Become A Legend</router-link>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto pull-right">
                <li class="nav-item">
                    <router-link 
                    v-if="!isLoggedIn" 
                    class="btn btn-danger" 
                    to="/register">
                    Sign Up</router-link>
                </li>
                <li class="nav-item pull-right">
                    <router-link v-if="!isLoggedIn" class="nav-link" to="/login">Login</router-link>
                </li>
                <li class="nav-item pull-right">
                    <router-link class="nav-link" to="/about">About</router-link>
                </li>
                <li class="nav-item pull-right">
                    <a href="#" v-if="isLoggedIn" @click="logout" class="nav-link">logout</a>
                </li>
            </ul>
        </div>
    </nav>
    <router-view></router-view>
</div>

</template>

<script>
import { mapState } from 'vuex'
import router from './router'


export default {
  name: 'navbar',
  computed: {
    ...mapState(['isLoggedIn']),
  },
  methods: {
    logout: function() {
      localStorage.clear()
      this.$store.dispatch('getUserLoggedOut')
      router.push('/')
    },
  },
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>