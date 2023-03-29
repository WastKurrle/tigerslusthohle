<script setup>
    import { ref } from 'vue'
    import { useAuthenticateStore } from '../stores/authenticate';

    // stores
    const authenticateStore = useAuthenticateStore()

    const password = ref('')

    const login = () => {
        authenticateStore.authentciate(password.value)
        password.value = ''
    }
</script>

<template>
    <div>
        <h4 class="text-center">Authentifizieren um Bilder und Videos sehen zu können</h4>

        <form @submit.prevent="login">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" class="form-control" v-model="password">
        </form>
    </div>
</template>

<style scoped>
</style>