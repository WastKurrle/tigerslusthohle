<script setup>
import { ref, reactive, onMounted } from 'vue'
import axios from "axios";

// compoents
import Image from '../components/Image.vue'
import Video from '../components/Video.vue'

const images = ref({})
const videos = ref({})

const getImages = async () => {
  await axios.get('/api/upload/image/')
        .then(response => {
          images.value = response.data
        })
        .catch(error => {
          console.log(error)
        })
}

const getVideos = async () => {
  await axios.get('/api/upload/video/')
            .then(response => {
              videos.value = response.data
            })
            .catch(error => {
              console.log(error)
            })
}

onMounted(() => {
  getImages()
  getVideos()
})
</script>

<template>
  <main>
    <h1 class="text-center">Tigers Lusthöhle</h1>

    <div class="flex justify-center">
      <div class="row mb-3 gap-3">
        <Image v-for="img in images" :key="img.id" :image="img" class="col-md-4"/>
        <Video v-for="video in videos" :key="video.id" :video="video"/>
      </div>
    </div>
  </main>
</template>
