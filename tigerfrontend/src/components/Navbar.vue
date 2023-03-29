<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useFilterStore } from '../stores/filter'
import axios from 'axios'

const router = useRouter()

// stores
const filterStore = useFilterStore()

const query = ref('')

const filter = () => {
    const data = {
        filterData: query.value
    }

    axios
        .post('/api/upload/filter/', data)
        .then(response => {
            filterStore.filterRes = response.data
            query.value = ''
            router.push('/filter')
        })
        .catch(error => {
            console.log(error)
        })
}
</script>

<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <RouterLink class="navbar-brand" :to="{ name: 'home' }">Tigers Lusthöhle</RouterLink>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <RouterLink class="nav-link active" aria-current="page" :to="{ name: 'home' }">Home</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" :to="{ name: 'upload' }">Upload</RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" :to="{ name: 'upload-video' }">Upload Video</RouterLink>
                    </li>
                </ul>
                <form class="d-flex" @submit.prevent="filter">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="query">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
                </div>
            </div>
        </nav>
    </div>
</template>

<style scoped>
</style>
