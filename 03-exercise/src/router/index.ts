import { createRouter, createWebHistory } from 'vue-router'

import PostList from '@/views/PostList.vue'
import PostDetail from '@/views/PostDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: () => {
        return { name: 'postList' }
      }
    },
    {
      path: '/post',
      name: 'postList',
      component: PostList
    },
    {
      path: '/post/:id',
      name: 'post',
      component: PostDetail
    }
  ]
})

export default router
