<template>
	<div>
		<form>
			<input type="text" placeholder="brand" v-model="data.brand"><br><br>
			<input type="text" placeholder="Model" v-model="data.model"><br><br>
			<input type="text" placeholder="Date Created" v-model="data.createdOn"><br><br>
			<input type="text" placeholder="Warranty" v-model="data.warranty"><br><br>
			<input type="text" placeholder="Damaged" v-model="data.damaged"><br><br>
			<input type="text" placeholder="Repaired" v-model="data.repaired"><br><br>
			<input type="text" placeholder="First Owner" v-model="data.firstOwner"><br><br>
			<input type="text" placeholder="Price" v-model="data.price"><br><br>
			<br>
			<button v-on:click.prevent="createForm()"> Create </button>
			<br><br>	
			<p v-if="error">
				<b> {{ error }} </b>
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
					brand: '',
					model: '',
					createdOn: '',
					warranty: '',
					damaged: '',
					repaired: '',
					firstOwner: '',
					price: '',
				},
				error: ''
			}
		},
		methods: {
			createForm() {
				axios.post('http://localhost:8000/brandModels/' + this.id + '/', this.data)
				.then(response => 
					this.data = response.data)
				.catch(error => 
					this.error = error.message)
			}
		}
	}
</script>