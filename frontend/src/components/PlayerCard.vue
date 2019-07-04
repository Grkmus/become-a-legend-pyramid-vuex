<template>
    <div class="card" style="height:80px">
        <div class="container">
            <h5>{{player.name}} {{player.surname}}</h5>
        </div>
    </div>
</template>
<style>
h5 {
    font-size: 1.0rem;
}
</style>

<script>
export default {
    name: 'player-card',
    props: {
        player: Object
    },
}
</script>
