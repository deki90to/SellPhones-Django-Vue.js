<template>
<div>
	<h1> Create New Model </h1> <hr> <br>

	<form @submit.prevent="createPost()">
		<input type="text" placeholder="Brand Name" v-model="data.brand">
		<br><br>
		<button> Create </button> <br><br>

		<div v-if="message.success"> 
			{{ message.success }} 	
		</div> 
		<div v-if="message.failed">
			{{ message.failed }}
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
				message: {
					success: '',
					failed: '',
				}
			}
		},
		methods: {
			createPost() {
				axios.post('http://localhost:8000/', this.data)
				.then(response => 
					this.brand = response.data)
					this.message.success = 'Brand Added Successfuly'
					setTimeout(() => {
						this.$router.push({ name: 'Brands' })
					}, 2000)

				.catch(error => 
					console.log(error.message))
					this.message.failed = 'Brand Adding Failed'
				}
				// this.$router.push({ name: 'Brands' })
			}
		}
</script>