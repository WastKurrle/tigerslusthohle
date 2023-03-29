<script setup>
    import { ref } from "vue"
    import { RouterLink } from 'vue-router'

    const props = defineProps(['image'])

    const image = ref(props.image)
</script>

<template>
    <div class="card" style="width: 18rem;">
            <div class="h-75">
                <img :src="image.get_image" class="card-img-top"/>
            </div>
            <div class="card-body">
                <h5 class="card-title">{{ image.title }}</h5>
                <p class="card-text">{{ image.description }}</p>
                <RouterLink class="btn btn-danger" :to="`/upload/${image.id}`">Löschen</RouterLink>
            </div>
        </div>
</template>

<style scoped>
</style>
