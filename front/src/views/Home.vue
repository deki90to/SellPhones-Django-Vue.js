<template>
  <div class="home">
    <Nav />
    <Body />
  </div>
</template>

<script>
import Nav from '../components/Nav.vue'
import Body from '../components/Body.vue'

export default {
  name: 'Home',
  components: {
    Nav,
    Body
  }
}
</script>
