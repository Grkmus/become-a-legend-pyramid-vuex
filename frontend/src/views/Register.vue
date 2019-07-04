<template>
<div class="main container">
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
          <div class="alert alert-warning" role="alert" v-if="errorMessage">
            {{errorMessage}}
          </div>
            <h1 class="display-4 m-b-2">Register to play</h1>
            <!-- register form-->
          <form @submit.prevent="signup" method="POST" action="/register" id="forms">
              <div class="form-group"><label for="name">Name:</label><input v-model="player.name" class="form-control" type="text" placeholder="name" name="name" /></div>
              <div class="form-group"><label for="surname">Surname:</label><input v-model="player.surname" class="form-control" type="text" placeholder="name" name="surname" /></div>
              <div class="form-group"><label for="username">Username:</label><input v-model="player.username" class="form-control" type="text" placeholder="name" name="username" /></div>
              <div class="form-group"><label for="email">Email:</label><input v-model="player.email" class="form-control" type="email" placeholder="name@email.com" name="email" /></div>
              <div class="form-group"><label for="pw">Password:</label><input v-model="player.password" class="form-control" type="password"  /></div>
              <div class="form-group"><label for="pw">Password:</label><input v-model="player.confirmPassword" class="form-control" type="password" /></div>
              <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        </div>
    </div>
</div>
</template>
<script>

import router from '../router.js'
import axios from 'axios'
import Joi from '@hapi/joi'

const schema = Joi.object().keys({
        name: Joi.string().alphanum().min(2).max(30).required(),
        surname: Joi.string().alphanum().min(2).max(30).required(),
        username: Joi.string().alphanum().min(3).max(30).required(),
        email: Joi.string().email({ minDomainSegments: 2 }),
        password: Joi.string().regex(/^[a-zA-Z0-9]{6,30}$/),
        confirmPassword: Joi.string().regex(/^[a-zA-Z0-9]{6,30}$/)
      })

export default {
  name: 'register',
  data: () => ({
    errorMessage: '',
    player: {
      name: '',
      surname: '',
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
    }
  }),
  methods: {
    signup: async function () {
      if (this.validPlayer()) {
        await axios.post('http://localhost:6543/register', this.player)
        .then(async res => {
          console.log(res)
          localStorage.token = res.data.token
          router.push('home')
        })
        .catch(err => {
          if (err.response.status == 406)
            alert('this username already taken')
          else
            alert(err.message)
        })
      }
    },
    validPlayer: function () {
      if (this.player.password !== this.player.confirmPassword) {
        this.errorMessage = 'Passwords are not matching..'
        return false
      }

      const result = Joi.validate(this.player, schema)
      if (result.error === null) 
        return true;
      this.errorMessage = result.error.details[0].message
      console.dir(result.error)
      return false;
    },
  }
}
</script>

<style>
.about {
  text-align: left
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
