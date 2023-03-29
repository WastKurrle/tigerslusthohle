<script setup>
    import { ref } from 'vue'
    import { toast } from 'vue3-toastify';
    import axios from 'axios'

    const title = ref('')
    const image = ref({})
    const description = ref('')

    const changeImage = (event) => {
        image.value = event.target.files[0]
    }

    const uploadImage = () => {
        const data = {
            title: title.value,
            image: image.value,
            description: description.value
        }

        axios
            .post('/api/upload/image/', data, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            })
            .then(response => {
                toast.success('Bild wurde hochgeladen', { autoClose: 3000 })
            })
        
        title.value = ''
        image.value = ''
        description.value = ''
    }
</script>

<template>
    <div>
        <h3 class="text-center">Upload</h3>

        <div>
            <form @submit.prevent="uploadImage">
                <label for="title" class="form-label">Titel</label>
                <input type="text" id="title" class="form-control mb-3" required v-model="title">

                <label for="image" class="form-label">Bild</label>
                <input type="file" id="image" class="form-control mb-3" required @change="changeImage" accept="image/png, image/gif, image/jpeg">

                <label for="desc" class="form-label">Beschreibung</label>
                <textarea id="desc" cols="30" rows="10" class="form-control mb-3" required v-model="description"></textarea>

                <button class="btn btn-success">Upload</button>
            </form>
        </div>
    </div>
</template>

<style scoped>

</style>