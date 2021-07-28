<template>
    <div> 
        <h1> Brand Models </h1>
        <hr>
        <div v-if="brandModels">
            <div v-for="bm in brandModels" :key="bm.id"> 
                {{ bm }}
            </div>
        </div>
    </div>
</template>


<script>
    import axios from 'axios'

    export default {
        props: ['id'],
        data(){
            return {
                brandModels: []
            }
        },
        mounted(){
            axios.get('http://localhost:8000/brandModels/' + this.id)
            .then(response => {
                this.brandModels = response.data
            })
        }
    }
</script>
