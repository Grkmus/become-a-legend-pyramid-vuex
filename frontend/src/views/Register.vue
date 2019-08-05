<template>
<div class="main container">
  <div class="row">
    <div class="col-md-6 col-md-offset-3">
      <form @submit.prevent="signup" method="POST" action="/register" id="forms">
        <fieldset>
          <legend>Register</legend>
          <div v-if="errorMessage.general" class="alert alert-warning" role="alert" >
            {{errorMessage.general}}
          </div>

          <div class="form-group has-danger">
            <label class="form-control-label" for="name">Name</label>
            <input v-model="player.name" id="name" v-bind:class="{ 'is-invalid': errorMessage.name }" class="form-control" type="text" placeholder="Name" name="name">
            <div class="invalid-feedback" v-if="errorMessage.name">{{ errorMessage.name }}</div>
          </div>

          <div class="form-group has-danger">
            <label class="form-control-label" for="surname">Surname</label>
            <input v-model="player.surname" id="surname" v-bind:class="{ 'is-invalid': errorMessage.surname }" class="form-control" type="text" placeholder="Surname" name="surname">
            <div class="invalid-feedback" v-if="errorMessage.surname"> {{ errorMessage.surname }} </div>
          </div>

          <div class="form-group has-danger">
            <label class="form-control-label" for="email">Email address</label>
            <input v-model="player.email" id="email" v-bind:class="{ 'is-invalid': errorMessage.email }" class="form-control" type="email" placeholder="Enter email" name="email" aria-describedby="emailHelp" >
            <!-- <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small> -->
            <div class="invalid-feedback" v-if="errorMessage.email">{{ errorMessage.email }}</div>
          </div>

          <div class="form-group has-danger">
            <label class="form-control-label" for="username">Username</label>
            <input v-model="player.username" id="usernameId" v-bind:class="{ 'is-invalid': errorMessage.username }" class="form-control" type="text" placeholder="name"  name="username" aria-describedby="usernameHelp">
            <div class="invalid-feedback" v-if="errorMessage.username">{{ errorMessage.username }}</div>
          </div>

          <div class="form-group">
            <label class="form-control-label" for="pw">Password</label>
            <input v-model="player.password"  id="pw" v-bind:class="{ 'is-invalid': errorMessage.password }" class="form-control" type="password" placeholder="Password" name="password">
            <div class="invalid-feedback" v-if="errorMessage.password">{{ errorMessage.password }}</div>
          </div>

          <div class="form-group">
            <label class="form-control-label" for="cpw">Confirm Password</label>
            <input v-model="player.confirmPassword" id="cpw" v-bind:class="{ 'is-invalid': errorMessage.confirmPassword }" class="form-control" type="password" placeholder="Confirm password" name="confirmPassword">
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </fieldset>
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
        name: Joi.string().regex(/^[a-zA-ZİğüöÖÜ]/).min(2).max(30).required(),
        surname: Joi.string().regex(/^[a-zA-ZİğüöÖÜ]/).min(2).max(30).required(),
        username: Joi.string().alphanum().min(3).max(30).required(),
        email: Joi.string().email({ minDomainSegments: 2 }),
        password: Joi.string().regex(/^[a-zA-Z0-9]{6,30}$/),
        confirmPassword: Joi.string().regex(/^[a-zA-Z0-9]{6,30}$/)
      })

export default {
  name: 'register',
  data: () => ({
    errorMessage: {
      name: '',
      surname: '',
      username: '',
      email: '',
      password: '',
      general: '',
    },
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
            this.errorMessage.username = "Sorry, this username's already taken."
          else
            this.errorMessage.general = err.message
        })
      }
      console.log('user is not valid')
    },
    validPlayer: function () {
      this.errorMessage = { //reset the errorMessage object
        name: '',
        surname: '',
        username: '',
        email: '',
        password: '',
        general: '',
      }

      if (this.player.password !== this.player.confirmPassword) {
        this.errorMessage.password = "Passwords are not matching."
        return false
      } else {
        const result = Joi.validate(this.player, schema, {abortEarly: false})
        if (result.error === null) {
          return true
        }
        result.error.details.forEach(error => {
          if (error.path[0] === 'name' && this.errorMessage.name === '') {
            this.errorMessage.name = error.message
          } else if (error.path[0] === 'surname' && this.errorMessage.surname === '') {
            this.errorMessage.surname = error.message
          } else if (error.path[0] === 'username' && this.errorMessage.username === '') {
            this.errorMessage.username = error.message
          } else if (error.path[0] === 'email' && this.errorMessage.email === '') {
            this.errorMessage.email = error.message
          } else if (error.path[0] === 'password' && this.errorMessage.password === '') {
            this.errorMessage.password = error.message
          }
        });
        return false
      }
      return true
    },
  }
}
</script>
