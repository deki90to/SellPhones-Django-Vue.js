import { createRouter, createWebHistory } from 'vue-router'
import About from '../views/About.vue'
import Specs from '../views/Specs.vue'
import Brands from '../views/Brands.vue'
import BrandModels from '../views/BrandModels.vue'
import ModelSpecs from '../views/ModelSpecs.vue'
import Form from '../views/Form.vue'
import ModelForm from '../views/ModelForm.vue'

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
    path: '/modelSpecs/:id',
    name: 'ModelSpecs',
    component: ModelSpecs,
    props: true
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/form',
    name: 'Form',
    component: Form
  },
  {
    path: '/modelForm/:id',
    name: 'ModelForm',
    component: ModelForm,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
