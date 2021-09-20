<template>
	<div>
		<h1> Add New Model </h1>
		<form>
			<input type="text" hidden placeholder="brand" v-model="data.brand">
			<input type="text" placeholder="Model" v-model="data.model"><br><br>
			<input type="text" hidden placeholder="Date Created" v-model="data.createdOn">
			<input type="text" placeholder="Warranty" v-model="data.warranty"><br><br>
			<input type="text" placeholder="Damaged" v-model="data.damaged"><br><br>
			<input type="text" placeholder="Repaired" v-model="data.repaired"><br><br>
			<input type="text" placeholder="First Owner" v-model="data.firstOwner"><br><br>
			<input type="text" placeholder="Price" v-model="data.price"><br><br><br>

			<button v-on:click.prevent="createForm"> Create </button>
			<br><br>
			<router-link :to="{ name: 'Brands' }"> Back To HOME </router-link>
				<!-- <p v-if="success">
					{{ success }}
				</p> -->
		</form>
	</div>
</template>

<script>
	import axios from 'axios'

	export default {
		props: ['id'],
		data() {
			return {
				data: {
					brand: this.id,
					model: '',
					createdOn: new Date().toISOString().slice(0,10),
					warranty: '',
					damaged: '',
					repaired: '',
					firstOwner: '',
					price: '',
				},
				// success: '',
			}
		},
		methods: {
			createForm() {
				axios.post('http://localhost:8000/brandModels/' + this.id + '/', this.data)
				.then(response => {
					this.data = response.data
					// this.success = 'Model Successfuly Added'
					setTimeout(() => {
						this.$router.push({ name: 'BrandModels' })
					}, 1000)
				})
				.catch(error => 
					this.error = error.message)
			}
		}
	}
</script>