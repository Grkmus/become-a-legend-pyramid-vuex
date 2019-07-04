import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Landing from './views/Landing.vue';
import Register from './views/Register.vue';
import Login from './views/Login.vue';
import Player from './views/Player.vue';
import NotFound from './views/NotFound.vue';

Vue.use(Router);
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
      meta: {
        public: true,  // Allow access to even if not logged in
        onlyWhenLoggedOut: true
      },
      beforeEnter: loggedInRedirectHome
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        public: true,  // Allow access to even if not logged in
        onlyWhenLoggedOut: true
      },
      beforeEnter: loggedInRedirectHome
      
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        public: true,  // Allow access to even if not logged in
        onlyWhenLoggedOut: true
      },
      beforeEnter: loggedInRedirectHome
    }, 
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
    },
    {
      path: '/player/:id',
      name: 'player',
      component: Player,
    },
    {
      path: '/about',
      name: 'about',
      
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    {
      path: '*',
      name: 'notfound',
      component: NotFound,
    }
  ],
});

function loggedInRedirectHome (to, from, next) {
  if(localStorage.token){
    next('/home')
  } else {
    next()
  }
}


// router.beforeEach((to, from, next) => {
//   const isPublic = to.matched.some(record => record.meta.public)
//   const onlyWhenLoggedOut = to.matched.some(record => record.meta.onlyWhenLoggedOut)
//   const loggedIn = !!TokenService.getToken();

//   if (!isPublic && !loggedIn) {
//     return next({
//       path:'/login',
//       query: {redirect: to.fullPath}  // Store the full path to redirect the user to after login
//     });
//   }

//   // Do not allow user to visit login page or register page if they are logged in
//   if (loggedIn && onlyWhenLoggedOut) {
//     return next('/')
//   }

//   next();
// })
// router.beforeEach((to, from, next) => {
//   const isPublic = to.matched.some(record => record.meta.public)
//   if (isPublic) {
//     console.log('Public Page!')
//     next()
//   }
//   else {
//     console.log('Private Page!')
//     return next({
//       path: '/login',
//       query: {redirect: to.fullPath }
//     });
//   }
// })
 
export default router