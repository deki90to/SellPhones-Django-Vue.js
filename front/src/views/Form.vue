<template>
<div>
	<h1> Create New Model </h1> <hr> <br>

	<form @submit.prevent="createPost()">
		<input type="text" placeholder="Brand Name" v-model="data.brand">
		<br><br>
		<button> Create </button> <br><br>

		<div v-if="success"> 
			{{ success }} 	
		</div> 
		<div v-if="failed">
			{{ failed }}
		</div> 
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
				},
					success: '',
					failed: '',
			}
		},
		methods: {
			createPost() {
				axios.post('http://localhost:8000/', this.data)
				.then(response => 
					this.brand = response.data)
					this.success = 'Brand Added Successfuly'
					setTimeout(() => {
						this.$router.push({ name: 'Brands' })
					}, 1000)

				.catch(error => 
					console.log(error.message))
					this.failed = 'Brand Adding Failed'
				}
				// this.$router.push({ name: 'Brands' })
			}
		}
</script>