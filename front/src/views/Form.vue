<template>
<div>
	<h1> Create New Model </h1> <hr> <br>

</div>
</template>

<script>
	import axios from 'axios'
	export default {
		name: 'Create Post',
		data() {
			return {
				
			}
		},
		methods: {
			createPost(){
				axios.post()
				.then(response => 
					console.log(response))
				.catch(error => 
					console.log(error.message))
			}
		}
	}
</script>