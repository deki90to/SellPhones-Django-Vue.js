<template>
    <div>
        <h1> Models </h1>
            <div v-for="model in models" v-bind:key="model.id" class="models">
                <hr>
                <table>
                    <tr>
                        <th> Model </th>
                        <th> Created </th>
                        <th> Warranty </th>
                        <th> Damaged </th>
                        <th> Repaired </th>
                        <th> First Owner </th>
                        <th> Price </th>
                        <th> More Specs </th>
                    </tr>
                    <tr>
                        <td> {{ model.modelName }} </td>
                        <td> {{ model.createdOn }} </td>
                        <td> {{ model.warranty }} </td>
                        <td> {{ model.damaged }} </td>
                        <td> {{ model.repaired }} </td>
                        <td> {{ model.firstOwner }} </td>
                        <td> {{ model.price }}e </td>
                        <th> 
                            <router-link :to="{ name: 'Specs', params: {id: model.id} }"> 
                                HERE 
                            </router-link> 
                        </th>
                    </tr>
                </table>
            </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['id'],
    // template: ['id'],
    data(){
        return {
            models: []
        }
    },
    mounted(){
        axios.get('http://localhost:8000/model/')
        .then(response => {this.models = response.data})
    }
}
</script>

<style scoped>
    .models{
        background-color: lightcyan;
        border: 10px;
    }

</style>