<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue';
import { useAuthenticateStore } from './stores/authenticate';
import Cookies from 'js-cookie'

// components
import Navbar from './components/Navbar.vue'

// stores = 
const authenticateStore = useAuthenticateStore()

onMounted(() => {
  if (Cookies.get('auth')) {
    authenticateStore.authenticated = true
  }
})
</script>

<template>
  <header>
    <Navbar />
  </header>
  
  <main class="container mt-3">
    <RouterView />
  </main>
</template>

<style scoped>
</style>
