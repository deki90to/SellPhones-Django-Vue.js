<template>
    <div>
        <h1> Brands </h1> <hr>
        <div v-for="brand in brands" v-bind:key="brand.id">
            <router-link v-bind:to="{name: 'Models'}">
                <h3> {{ brand.brand }} </h3>
            </router-link>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return {
            brands: []
        }
    },
    mounted(){
        fetch('http://localhost:8000/')
        .then(response => response.json())
        .then(data => this.brands = data)
        .catch(error => console.log(error))
    }
}
</script>
