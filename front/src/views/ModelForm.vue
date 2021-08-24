<template>
	<div>
		<form @submit.prevent="createForm()">
			<input type="text" placeholder="Model" v-model="info.model"><br><br>
			<input type="text" placeholder="CreatedOn" v-model="info.createdOn"><br><br>
			<input type="text" placeholder="Warranty" v-model="info.warranty"><br><br>
			<input type="text" placeholder="Damaged" v-model="info.damaged"><br><br>
			<input type="text" placeholder="Repaired" v-model="info.repaired"><br><br>
			<input type="text" placeholder="First Owner" v-model="info.firstOwner"><br><br>
			<input type="text" placeholder="Price" v-model="info.price"><br><br>
			<br>
			<button> Create </button>
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
				info: {
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
			async createForm() {
				await axios.post('http://localhost:8000/brandModels/' + this.id + '/', this.info)
				.then(response => {
					this.info = response.data
				})
				.catch(error => 
					this.error = error.message
				)
			}
		}
	}
</script>