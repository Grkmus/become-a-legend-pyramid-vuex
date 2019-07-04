<template>

</template>
<style>
.center {
    margin-top: 12.8px;
    display: flex;  
}
#captain {
    padding-left: 0px;
    padding-right: 0px;
    margin: 10px;

}
.players {
    height: 126px;  
}  
#player1 {
    height: 126px;
    margin-top: 10px;
    padding-left: 5px;
    padding-right: 5px;
    height: 100%;
}
#player2 {
    height: 126px;
    margin-top: 10px;
    padding-left: 5px;
    padding-right: 5px;
}

</style>

<script>
export default {
    name: 'Team',
    props: ['data'],
    created(){
    },
    data(){
        return {
            team: {
                name: String,
                players: [{
                    name: String,
                    ratingEvaluation: Number
                }],
                credits: Number
            },
            isLoaded: false,
            isActive: false
        }
    },
    mounted(){
        this.team = this.data
        // this.captain = this.data.players[0]
        this.isLoaded = true
        this.isActive = false
    },
    methods: {
        skipTheTurn: function(){
            this.$eventBus.$emit('skipTheTurn')
        }
    },
    computed: {
        // captain() {
        //     return this.team.players[0]
        // },
        // player1() {
        //     return this.team.players[1]
        // },
        // player2() {
        //     return this.team.players[2]
        // }
        
    }
}
</script>
