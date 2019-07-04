<template>

</template>
<style>
h5 {
    font-size: 1.0rem;
}
</style>

<script>
import router from '@/router.js'
export default {
    name: 'playerEventCard',
    props: ['data'],
    methods: {
        // captainSelectPlayer: function() {
        //     this.$emit('handleSelect', this.data._id)
        // },
        goToPlayer: function(_id) {
            router.push({
                name: 'player',
                params: { id: _id }
            })
        },
    }
}
</script>
