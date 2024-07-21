import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AuthView from '@/views/AuthView.vue'
import SocialView from '@/views/SocialView.vue'
import ExampleView from '@/views/ExampleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: AuthView
    },
    {
      path: '/social',
      name: 'social',
      component: SocialView
    },
    {
      path: '/example',
      name: 'example',
      component: ExampleView
    }
  ]
})

export default router
