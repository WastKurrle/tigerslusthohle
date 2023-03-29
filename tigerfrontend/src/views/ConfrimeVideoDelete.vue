<script setup>
import { useRoute, useRouter } from 'vue-router'
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'
import { toast } from 'vue3-toastify'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const id = ref(route.params.id)

const deleteImg = () => {
    axios.delete(`/api/upload/video/${id.value}/`)
        .then(response => {
            toast.error('Video wurde gelöscht', { autoClose: 3000 })
            router.push('/')
        })
        .catch(error => {
            console.log(error)
        })
}
</script>

<template>
    <div>
        <h4 class="text-center">Video Löschen</h4>

        <div>
            <div>
                <p>Möchtest du das Video Löschen?</p>
                <RouterLink class="btn btn-primary w-25 m-1" to="/">Abbrechen</RouterLink>
                <button class="btn btn-danger w-25" @click="deleteImg">Ja</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>