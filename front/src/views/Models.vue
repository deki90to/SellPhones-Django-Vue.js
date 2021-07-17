<template>
    <div>
        <div v-if='models'>
            <h1> Models </h1>
            <div v-for='model in models' :key='model.id'>
                <router-link v-bind:to="{name: 'Specs', params: {id: model.id}}">
                    <h3> {{ model.modelName }} </h3>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // props: ['id'],
    data(){
        return {
            models: []
        }
    },
    mounted(){
        fetch('http://localhost:8000/models/')
        .then(response => response.json())
        .then(data => this.models = data)
        .catch(error => console.log(error))
    }
}
</script>
