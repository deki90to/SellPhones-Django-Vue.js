<template>
	<div>
		<h1> Brands </h1> <br>
		<div v-for="brand in brands" v-bind:key="brand.id" class="brands">
			<router-link :to="{ name: 'BrandModels', params: {id: brand.id} }"> 
				<h3> {{ brand.brand }} </h3> <hr>
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

<style scoped>
	hr {
		width: 20%;
		color: cyan;
	}
</style>