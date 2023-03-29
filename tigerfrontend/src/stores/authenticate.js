import { defineStore } from "pinia";
import { ref } from "vue";
import { toast } from "vue3-toastify";
import axios from "axios";
import Cookies from 'js-cookie'

export const useAuthenticateStore = defineStore('authenticate', () => {
    const authenticated = ref(false)

    const authentciate = (password) => {
        const data = {
            password: password
        }

        axios
            .post('/api/auth/', data, {
                withCredentials: true,
            })
            .then(response => {
                Cookies.set('auth', true, { expires: 1/24/6 })
                authenticated.value = true
                toast.success('Eingeloggt', { autoClose: 3000 })
            })
            .catch(error => {
                toast.error('Falsches Passwort!', { autoClose: 3000 })
            })
    }

    return { authenticated, authentciate }
})
