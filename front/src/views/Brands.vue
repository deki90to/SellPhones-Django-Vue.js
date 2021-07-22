<template>
    <div>
        <h1> Brands </h1> <hr>
        <div v-for="brand in brands" v-bind:key="brand.id">
            <router-link v-bind:to="{name: 'Models'}">
                <h3> {{ brand }} </h3>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            brands: []
        }
    },
    mounted(){
        axios.get('http://localhost:8000/')
        .then(response => {this.brands = response.data})
    }
}
</script>
