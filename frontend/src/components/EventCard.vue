<template>
<div class="card text-left" style="height:192px">
    <div class="container card-title"><h3> {{event.name}}</h3></div>
    <div class="card-body">
        <div class="container">
            <div class="row">
                <div class="col-sm-8">
                    <p class="card-text date">Date: {{ event.date }} </p>
                    <p class="card-text date">Time: {{ event.time }} </p>
                    <p class="card-text">Location: {{ event.location }}</p>
                </div>
                <div class="col-sm-4 people">
                    <p class="center">Number of people </p>
                    <h5 class="card-title center">{{ numberOfAttendees }}</h5>
                    <button class="btn-primary">Attend</button>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'event-card',
    props: {
        event: Object
    },
    computed: {
        numberOfAttendees: function() {
            return this.event.attendees.length
        },
        // alreadyAttended: function() {
        //     if (this.$state.player)
        // } 
    }
}
</script>

<style>
.center {
    text-align: center;
    margin: auto;
}
.event {
    font-size: 0.8rem;
    text-align: left
}
.event-button {
    position: relative;
    left: 20px;
}
.people {
    border-left: solid 1px;
}
.card-body {
    padding: 5px;
    font-size: 0.8rem
}
.date {
    margin-bottom: 1px;
}

</style>