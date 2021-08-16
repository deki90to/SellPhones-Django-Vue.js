<template>
	<h1> Form </h1> <hr> <br>
	<form @submit.prevent>
		<div>
			<label for="model"> Model </label>
			<input type="text" id="model" v-model="formData.model" />
		</div>
		<div>
			<label for="created"> Created </label>
			<input type="text" id="created" v-model="formData.created" />
		</div>
		<div>
			<label for="warranty"> Warranty </label>
			<input type="text" id="warranty" v-model="formData.warranty" />
		</div>
		<div>
			<label for="damaged"> Damaged </label>
			<input type="text" id="damaged" v-model="formData.damaged" />
		</div>
		<div>
			<label for="repaired"> Repaired </label>
			<input type="text" id="repaired" v-model="formData.repaired" />
		</div>
		<div>
			<label for="firstOwner"> First Owner </label>
			<input type="text" id="firstOwner" v-model="formData.firstOwner" />
		</div>
		<div>
			<label for="price"> Price </label>
			<input type="text" id="price" v-model="formData.price" />
		</div>
			<button v-on:click="createPost()"> Create </button>

	</form>
</template>


<script>
	import axios from 'axios'
	export default {
		name: 'Create Post',
		data() {
			return {
				formData: {
					model: '',
					created: '',
					warranty: '',
					damaged: '',
					repaired: '',
					firstOwner: '',
					price: ''
				}
			}
		},
		methods: {
			createPost(){
				axios.post('http://localhost:8000/brandModels/', this.formData)
				.then(response => console.log(response))
				.catch(error => console.log(error))
			}
		}
	}
</script>