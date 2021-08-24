<template>
<div>
	<h1> Create New Model </h1> <hr> <br>

	<form @submit.prevent="createPost()">
		<input type="text" placeholder="Brand Name" v-model="data.brand">
		<br><br>
		<button> Create </button>
	</form>

	<br><hr><br>
	<router-link to="/"> Back to HOME </router-link>
</div>
</template>

<script>
	import axios from 'axios'
	export default {
		name: 'Create Post',
		data() {
			return {
				data: {
					brand: '',
				}
			}
		},
		methods: {
			createPost() {
				axios.post('http://localhost:8000/', this.data)
				.then(response => 
					console.log(response.data))
				.catch(error => 
					console.log(error.message))
					
				this.$router.push({ name: 'Brands' })
			}
		}
	}
	
</script>

<!-- 		methods: {
			createPost(){
				axios.post('http://localhost:8000/', this.data)
				.then(response => 
					console.log(response))
				.catch(error => 
					console.log(error.message))
			}
		}
	} -->