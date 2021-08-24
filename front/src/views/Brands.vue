<template>
	<div>
        <router-link v-bind:to="{name: 'Form'}"> Add New Brand </router-link>
		
		<h1> Brands </h1> <br> <hr>
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
		width: 50%;
		color: cyan;
	}
/*	.brand-form {
	    width: 30%;
	    height: 40px;
	    border: 1px solid lightblue;
	}*/
</style>