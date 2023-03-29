<script setup>
    import { ref } from "vue"
    import { RouterLink } from 'vue-router'

    const props = defineProps(['video'])

    const video = ref(props.video)
</script>

<template>
   <div class="card" style="width: 18rem;">
        <video controls class="h-75">
            <source :src="video.get_video">
        </video>
        <div class="card-body">
            <h5 class="card-title">{{ video.title }}</h5>
            <p class="card-text">{{ video.description }}</p>
            <RouterLink :to="`/upload/video/${video.id}`" class="btn btn-danger">Löschen</RouterLink>
        </div>
    </div>
</template>

<style scoped>
</style>
