import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

const app = createApp(App)

app.use(router)
  .use(VueCookies, {expires: '1d'})
  .mount('#app')

// $cookies.set('auth', 1000)
// $cookies.get('auth')
// $cookies.remove('auth')
// $cookies.isKey('auth')
// $cookies.isKey('auth')
// $cookies.keys()

// $session.start()
// $session.set('auth', 1000)
// $session.get('auth')
// $session.id()
// $session.renew()
// $session.destroy()
