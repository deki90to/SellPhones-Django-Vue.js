<template>
	<div>
		<form>
			<input type="text" hidden placeholder="brand" v-model="data.brand">
			<input type="text" placeholder="Model" v-model="data.model"><br><br>
			<input type="text" hidden placeholder="Date Created" v-model="data.createdOn">
			<input type="text" placeholder="Warranty" v-model="data.warranty"><br><br>
			<input type="text" placeholder="Damaged" v-model="data.damaged"><br><br>
			<input type="text" placeholder="Repaired" v-model="data.repaired"><br><br>
			<input type="text" placeholder="First Owner" v-model="data.firstOwner"><br><br>
			<input type="text" placeholder="Price" v-model="data.price"><br><br><br>

			<button v-on:click.prevent="createForm()"> Create </button>
			<br><br>	
				<p>
					{{ message.success }}
				</p>
				<p v-if="message.error">
					{{ message.error }}
				</p>
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
				message: {
					success: '',
					error: ''
				},
			}
		},
		methods: {
			createForm() {
				axios.post('http://localhost:8000/brandModels/' + this.id + '/', this.data)
				.then(response => 
					this.data = response.data)
					this.message.success = 'Model Successfuly Added'
					setTimeout(() => {
						this.$router.push({ name: Brands })
					})
				.catch(error => 
					this.message.error = error.message)
					this.message.error = 'Adding Model Failed'
			}
		}
	}
</script>