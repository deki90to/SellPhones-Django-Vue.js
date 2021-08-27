<template>
    <div> 
        <router-link v-bind:to="{ name: 'ModelForm'}"> Add New Model </router-link>

        <h1> Brand Models </h1> <br>
        <div v-if="brandModels">
            <div v-for="data in brandModels" v-bind:key="data.id"> 
                <div v-for="model in data" v-bind:key="model.id">
                    <table class="th">
                        <tr>
                            <th><b> Model </b></th>
                            <!-- <th><b> Created </b></th>
                            <th><b> Warranty </b></th>
                            <th><b> Damaged </b></th>
                            <th><b> Repaired </b></th>
                            <th><b> First Owner </b></th>
                            <th><b> Price </b></th> -->
                        </tr>
                        <tr>
                            <td>{{ model.model }}</td>
                            <!-- <td>{{ model.createdOn }}</td> 
                            <td>{{ model.warranty }}</td> 
                            <td>{{ model.damaged }}</td> 
                            <td>{{ model.repaired }}</td> 
                            <td>{{ model.firstOwner }}</td> 
                            <td>{{ model.price }}e </td> 
                            <td> <router-link :to="{ name: 'ModelSpecs', params: {id: model.id} }"> <i> Specs here</i> </router-link> </td> -->
                        </tr>
                    </table>
                    <hr>
                </div>
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
