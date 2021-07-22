import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Models from '../views/Models.vue'
import Specs from '../views/Specs.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/models/',
    name: 'Models',
    component: Models,
  },
  {
    path: '/specs/:id',
    name: 'Specs',
    component: Specs,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
