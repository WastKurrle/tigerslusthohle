<script setup>
    import { useFilterStore } from '../stores/filter';
    import Image from '../components/Image.vue';
    import Video from '../components/Video.vue';

    // stores
    const filterStore = useFilterStore()
</script>

<template>
    <div>
        <h4 class="text-center">Filter Ergebnisse</h4>

        <div class="flex justify-center">
            <div class="row mb-3 gap-3">
              <Image v-for="img in filterStore.filterRes.img" :key="img.id" :image="img" class="col-md-4"/>
              <Video v-for="video in filterStore.filterRes.video" :key="video.id" :video="video"/>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>