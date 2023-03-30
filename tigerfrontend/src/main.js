import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap'
import 'vue3-toastify/dist/index.css'

const debug = false

if (debug) {
    axios.defaults.baseURL = 'http://127.0.0.1:8000'
}
else {
    axios.defaults.baseURL = 'https://api.tigerslusthoehle.de'
}

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
