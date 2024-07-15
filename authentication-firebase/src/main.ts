import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'

const firebaseConfig = {
  apiKey: 'AIzaSyAsSWpbxaY6WYuqa-WOJ5yBGHXIQMxSbK8',
  authDomain: 'curso-vue-30b6f.firebaseapp.com',
  projectId: 'curso-vue-30b6f',
  storageBucket: 'curso-vue-30b6f.appspot.com',
  messagingSenderId: '261056079854',
  appId: '1:261056079854:web:6ace525f36e7c99de650ff',
  measurementId: 'G-VN70KPCXPQ'
}

initializeApp(firebaseConfig)

const app = createApp(App)

app.use(router)

app.mount('#app')
