<template>
    <div v-if="specs" class="specs">
        <ul>
            <li> <b>Model:</b>          {{ specs.model }} </li> <br>
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
        </ul>
        <!-- <table class="th">
            <tr>
                <th><b> Model </b></th>
                <th><b> Dimensions </b></th>
                <th><b> Weight </b></th>
                <th><b> Screen </b></th>
                <th><b> Cpu </b></th>
                <th><b> Gpu </b></th>
                <th><b> Main Camera </b></th>
                <th><b> Front Camera </b></th>
                <th><b> Video </b></th>
                <th><b> Battery </b></th>
                <th><b> Fast Charging </b></th>
            </tr>
            <tr>
                <td>{{ specs.model }}</td>
                <td>{{ specs.dimensions }}</td> 
                <td>{{ specs.weight }}</td> 
                <td>{{ specs.screen }}</td> 
                <td>{{ specs.cpu }}</td> 
                <td>{{ specs.gpu }}</td> 
                <td>{{ specs.mainCam }}</td> 
                <td>{{ specs.selfieCam }}</td> 
                <td>{{ specs.video }}</td> 
                <td>{{ specs.battery }}</td> 
                <td>{{ specs.fastCharging }}</td> 
            </tr>
        </table> -->
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        props:['id'],
        data(){
            return {
                specs: [],
            }
        },
        mounted(){
            axios.get('http://localhost:8000/model/specs/' + this.id)
            .then(response => {this.specs = response.data})
        }
    }
</script>

<style scoped>
    .specs ul li {
        list-style-type: none;
        float: left;
    }
    /* .th {
        border: 1px solid;
        border-radius: 10px;
        padding: 20px;
        margin: 10% auto;
        box-shadow: 5px 5px 10px 5px ;
        background-color: aliceblue;
    } */
    .specs {
        background-color: lightcyan;
        border: 10px;
        padding: 10px;
    }

</style>