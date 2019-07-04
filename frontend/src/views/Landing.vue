<template>
<div class="jumbotron">
    <h1 class="display-4">Welcome to the "Become a Legend!" </h1>
    <p class="lead">Platform for doing sports with people while keeping track of your performance. It is designed for amateur sportsman who always having difficulties to find people to do sports with. You can get in a team according to your performance points. Organize
        sport events, between teams or other sport lovers. Compete in a league in any sport with your team or solo.</p>
    <hr class="my-4" />
    <p>You can be a legend! </p>
    <router-link class="btn btn-primary btn-lg" to="/about" role="button">Learn more</router-link>
    <router-link class="btn btn-secondary btn-lg" to="/register" role="button">Join Now!</router-link>
</div>
</template>

<script>

export default {
  name: 'landing',
}


</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
