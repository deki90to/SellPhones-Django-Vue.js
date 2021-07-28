import { createRouter, createWebHistory } from 'vue-router'
import About from '../views/About.vue'
import Specs from '../views/Specs.vue'
import Brands from '../views/Brands.vue'
import BrandModels from '../views/BrandModels.vue'



const routes = [
  {
    path: '/',
    name: 'Brands',
    component: Brands
  },
  {
    path: '/brandModels/:id',
    name: 'BrandModels',
    component: BrandModels,
    props: true
  },
  {
    path: '/specs/:id',
    name: 'Specs',
    component: Specs,
    props: true
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
