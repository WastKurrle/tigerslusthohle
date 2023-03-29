<script setup>
    import { ref } from 'vue'
    import { toast } from 'vue3-toastify';
    import axios from 'axios'

    const title = ref('')
    const video = ref({})
    const description = ref('')

    const changeVideo = (event) => {
        video.value = event.target.files[0]
    }

    const uploadVideo = () => {
        const data = {
            title: title.value,
            video: video.value,
            description: description.value
        }

        axios
            .post('/api/upload/video/', data, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            })
            .then(response => {
                toast.success('Video wurde hochgeladen', { autoClose: 3000 })
            })
        
        title.value = ''
        video.value = ''
        description.value = ''
    }
</script>

<template>
    <div>
        <h3 class="text-center">Upload</h3>

        <div>
            <form @submit.prevent="uploadVideo">
                <label for="title" class="form-label">Titel</label>
                <input type="text" id="title" class="form-control mb-3" required v-model="title">

                <label for="video" class="form-label">Video</label>
                <input type="file" id="video" class="form-control mb-3" required @change="changeVideo" accept="video/*">

                <label for="desc" class="form-label">Beschreibung</label>
                <textarea id="desc" cols="30" rows="10" class="form-control mb-3" required v-model="description"></textarea>

                <button class="btn btn-success">Upload</button>
            </form>
        </div>
    </div>
</template>

<style scoped>

</style>