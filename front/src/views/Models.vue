<template>
    <div>
        <h1> Models </h1>
        <div v-for='model in models' v-bind:key="model.id">
            <router-link v-bind:to="{name: 'Specs', params: {id: model.id}}">
                <h3> {{ model }} </h3>
            </router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    // props: ['id'],
    data(){
        return {
            models: []
        }
    },
    mounted(){
        axios.get('http://localhost:8000/models/')
        .then(response => {this.models = response.data})
    }
}
</script>
