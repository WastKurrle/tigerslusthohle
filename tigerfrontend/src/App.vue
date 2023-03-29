<script setup>
import { RouterView } from 'vue-router'
import NavbarVue from './components/Navbar.vue'

// components
import Navbar from './components/Navbar.vue'
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
