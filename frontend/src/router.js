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

// function checkLoggedInRedirectHome(to, from, next) {
//   if (localStorage.token) {
//     next('/home')
//   } else {
//     next()
//   }
// }

// function checkLoggedInRedirectLogin(to, from, next) {
//   if (localStorage.token) {
//     store.dispatch('getUser')
//     next()
//   } else {
//     next('/login')
//   }
// }
Vue.use(Router);
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
      meta: {
        relatedToAuth: true,
      },
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        relatedToAuth: true,
      },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        relatedToAuth: true,
      },
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      meta: {
        requiresAuth: true,
      },
      // beforeEnter: checkLoggedInRedirectLogin,
    },
    {
      path: '/player/:id',
      name: 'player',
      component: Player,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/event/:id',
      name: 'event',
      component: Event,
      meta: {
        requiresAuth: true,
      },
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
  // console.log('beforeEachStart')
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // console.log('this route requires auth')
    if (localStorage.token) {
      if (!store.getters.isLoggedIn) {
        // console.log('the user has token but not logged in')
        store.dispatch('getUser')
        // console.log('the user has been set')
        next()
      }
      // console.log('the user has token and is logged in')
      next()
    } else {
      // console.log('the user is NOT logged in')
      next('/login')
    }
  } else if (to.matched.some(record => record.meta.relatedToAuth)) {
    // console.log('this route is related to auth')
    if (localStorage.token) {
      // console.log('the user is logged in so needs to go to home page!')
      next('/home')
    } else {
      // console.log('the user is NOT logged in can go to a route related to auth')
      next()
    }
  } else {
    if (localStorage.token) {
      if (!store.getters.isLoggedIn) {
        store.dispatch('getUser')
        next()
      }
      next()
    }
    // console.log('do whatever you like!')
    next()
  }
})


export default router
