<template>
	<div>
        <router-link v-bind:to="{name: 'BrandForm'}"> Add New Brand </router-link>
		
		<h1> Brands </h1> <br> <hr>
		<div v-for="brand in brands" v-bind:key="brand.id" class="brands">
			<router-link :to="{ name: 'BrandModels', params: {id: brand.id, brand: brand} }"> 
				<h3> {{ brand.brand }} </h3>
			</router-link>

			<!-- <button v-on:click="deleteBrand(brand.id)"> Delete </button>  -->
			<br> <hr>
		</div>
		
		<div v-if='deleted'>
			<h4> Deleting... </h4>
		</div>
</div>
</template>

<script>
	import axios from 'axios'
	import BrandForm from './BrandForm.vue'

	export default {
		components: { BrandForm },
		data(){
			return {
				brands: [],
				deleted: '',
			}
		},
		mounted() {
			axios.get('http://localhost:8000/')
			.then(response => {
				this.brands = response.data
			})
			.catch(error => {
				console.log(error.message)
			})
		},
		methods: {
			deleteBrand(id) {
				axios.delete('http://localhost:8000/brandDelete/' + id + '/')
				.then(response => {
					console.log(response)
					this.deleted = response.statusText
					setTimeout(() => {
						this.$router.go(0)
					}, 500)
				})
				.catch(error => 
					console.log(error.message))
			}
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