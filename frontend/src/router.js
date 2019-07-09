import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Landing from './views/Landing.vue';
import Register from './views/Register.vue';
import About from './views/About.vue';
import Login from './views/Login.vue';
import Player from './views/Player.vue';
import Event from './views/Event.vue';
import NotFound from './views/NotFound.vue';
import store from './store';
// check if user is logged in before every request.


function loggedInRedirectHome(to, from, next) {
  if (localStorage.token) {
    next('/home')
  } else {
    next()
  }
}

function notLoggedInRedirectLogin(to, from, next) {
  if (localStorage.token) {
    next()
  } else {
    next('/login')
  }
}
Vue.use(Router);
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
      meta: {
        public: true, // Allow access to even if not logged in
        onlyWhenLoggedOut: true,
      },
      beforeEnter: loggedInRedirectHome,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        public: true, // Allow access to even if not logged in
        onlyWhenLoggedOut: true,
      },
      beforeEnter: loggedInRedirectHome,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        public: true, // Allow access to even if not logged in
        onlyWhenLoggedOut: true,
      },
      beforeEnter: loggedInRedirectHome,
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      beforeEnter: notLoggedInRedirectLogin,
    },
    {
      path: '/player/:id',
      name: 'player',
      component: Player,
    },
    {
      path: '/event/:id',
      name: 'event',
      component: Event,
    },
    {
      path: '/about',
      name: 'about',
      component: About,
    },
    {
      path: '*',
      name: 'notfound',
      component: NotFound,
    },
  ],
});

router.beforeEach((to, from, next) => {
  // checking isLoggedIn status to not emit too much events
  if (!store.state.isLoggedIn && localStorage.token) {
    store.dispatch('getUserLoggedIn')
    next()
  }
  next()
})

export default router
