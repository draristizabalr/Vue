import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import NoteCreateView from '@/views/NoteCreateView.vue'
import NoteListView from '@/views/NoteListView.vue'
import useAuth from '@/stores/auth'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'login',
            component: LoginView,
            meta: {
                requireAuth: false
            }
        },
        {
            path: '/register',
            name: 'register',
            component: RegisterView,
            meta: {
                requireAuth: false
            }
        },
        {
            path: '/note-list',
            name: 'note-list',
            component: NoteListView,
            meta: {
                requireAuth: true
            }
        },
        {
            path: '/note-create',
            name: 'note-create',
            component: NoteCreateView,
            meta: {
                requireAuth: true
            }
        }
    ]
})

router.beforeEach((to, from, next) => {
    const auth = useAuth()
    const isAuth = auth.token

    if (isAuth == null && to.meta.requireAuth) {
        next({ name: 'login' })
    } else {
        next()
    }
})

export default router
