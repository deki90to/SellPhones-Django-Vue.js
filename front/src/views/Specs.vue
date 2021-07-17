<template>
    <div>
        <div v-if='specs' class='specs'>
            <div v-for='spec in specs' v-bind:key='spec.id'>
                {{ spec }}
            </div>
            <!-- <ul>
                <li> <b> Model </b>         {{ specs.model }} </li> <br>
                <li> <b>Dimensions:</b>     {{ specs.dimensions }} </li> <br>
                <li> <b>Weight:</b>         {{ specs.weight }} </li> <br>
                <li> <b>Screen:</b>         {{ specs.screen }} </li> <br>
                <li> <b>Cpu:</b>            {{ specs.cpu }} </li> <br>
                <li> <b>Gpu:</b>            {{ specs.gpu }} </li> <br>
                <li> <b>Main Camera:</b>    {{ specs.mainCam }} </li> <br>
                <li> <b>Front Camera:</b>   {{ specs.selfieCam }} </li> <br>
                <li> <b>Video:</b>          {{ specs.video }} </li> <br>
                <li> <b>Battery:</b>        {{ specs.battery }} </li> <br>
                <li> <b>Fast Charging:</b>  {{ specs.fastCharging }} </li> <br>
            </ul> -->
        </div>
    </div>
</template>

<script>
    export default {
        props: ['id'],
        data(){
            return {
                specs: []
            }
        },
        mounted(){
            fetch('http://localhost:8000/specs/' + this.id)
            .then(response => response.json())
            .then(data => this.specs = data)
            .catch(error => console.log(error))
        }
    }
</script>

<style scoped>
    .specs ul li{
        list-style-type: none;
        float: left;
    }
</style>