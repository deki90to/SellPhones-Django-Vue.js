<template>
	<div>
		<h1> Brands </h1>
		<div v-for="brand in brands" v-bind:key="brand.id">
			<!-- <router-link :to="{ name: 'Models', params: {id: brand.id} }">  -->
			<router-link :to="{ name: 'BrandModels', params: {id: brand.id} }"> 
				{{ brand }} 
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
			.then(response => {
				this.brands = response.data
			})
		},
	}
</script>