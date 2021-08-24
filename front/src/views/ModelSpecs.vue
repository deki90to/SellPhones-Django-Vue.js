<template>
    <div>
        <h1> Specifications </h1> <br>
        <div v-for="data in modelSpecs" v-bind:key="data.id">
        <table class="th">
            <tr>
                <th> <b> Dimensions </b> </th>
                <th> <b> Weight </b> </th>
                <th> <b> Screen </b> </th>
                <th> <b> Cpu </b> </th>
                <th> <b> Gpu </b> </th>
                <th> <b> Main Camera </b> </th>
                <th> <b> Front Camera </b> </th>
                <th> <b> Video </b> </th>
                <th> <b> Battery </b> </th>
                <th> <b> Fast Charging </b> </th>
            </tr>
            <tr class="td">
                <td> {{ data[0].dimensions }} </td> 
                <td> {{ data[0].weight }} </td> 
                <td> {{ data[0].screen }} </td> 
                <td> {{ data[0].cpu }} </td> 
                <td> {{ data[0].gpu }} </td> 
                <td> {{ data[0].mainCam }} </td> 
                <td> {{ data[0].selfieCam }} </td> 
                <td> {{ data[0].video }} </td> 
                <td> {{ data[0].battery }} </td> 
                <td> {{ data[0].fastCharging }} </td> 
            </tr>
        </table>
        </div>
    </div>
    <!--             <b> Dimensions: </b>    {{ data[0].dimensions }} <br>
            <b> Weight: </b>        {{ data[0].weight }} <br>
            <b> Screen: </b>        {{ data[0].screen }} <br>
            <b> Cpu: </b>           {{ data[0].cpu }} <br>
            <b> Gpu: </b>           {{ data[0].gpu }} <br>
            <b> Back Camera: </b>   {{ data[0].mainCam }} <br>
            <b> Front Camera: </b>  {{ data[0].selfieCam }} <br>
            <b> Video Quality: </b> {{ data[0].video }} <br>
            <b> Battery: </b>       {{ data[0].battery }} <br>
            <b> Fast Charging: </b> {{ data[0].fastCharging }} <br> -->
</template>


<script>
import axios from 'axios'

    export default {
        props: ['id'],
        data(){
            return {
                modelSpecs: []
            }
        },
        mounted(){
            axios.get('http://localhost:8000/modelSpecs/' + this.id)
            .then(response => {
                this.modelSpecs = response.data
            })
        }
    }
</script>

<style scoped>
    .th {
        border-bottom: 3px solid;
        margin: auto;
        padding: 0.5rem;
        box-shadow: 5px 5px 20px 100px cyan;
    }
    .td {
        background-color: lightblue;
        color: black;
    }
</style>