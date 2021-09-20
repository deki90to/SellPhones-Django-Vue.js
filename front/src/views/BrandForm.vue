<template>
<div>
	<h1> Add New Brand </h1> <hr> <br>

	<form @submit.prevent="createPost()">
		<input type="text" placeholder="Brand Name" v-model="data.brand">
		<br><br>
		<button> Create </button> <br><br>
		
		<h3 v-if="adding"> 
			<b> {{ adding }} </b>
		</h3>

		<!-- <div v-if="success"> 
			{{ success }} 	
		</div> 
		<div v-if="failed">
			{{ failed }}
		</div>  -->
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
				adding: '',
					// success: '',
					// failed: '',
			}
		},
		methods: {
			createPost() {
				axios.post('http://localhost:8000/', this.data)
				.then(response => {
					this.brand = response.data
					// this.success = 'Brand Added Successfuly'
					this.adding = 'Creating Brand...'
					setTimeout(() => {
						this.$router.push({ name: 'Brands' })
					}, 1000)
				})
				.catch(error => {
					console.log(error.message)
					// this.failed = error.message
					})
				},
			}
		}
</script>