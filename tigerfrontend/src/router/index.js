import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import UploadView from '../views/UploadView.vue'
import UploadVideo from '../views/UploadVideo.vue'
import ConfrimeImgDeleteView from '../views/ConfrimeImgDelete.vue'
import ConfrimeVideoDeleteView from '../views/ConfrimeVideoDelete.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/upload',
      name: 'upload',
      component: UploadView
    },
    {
      path: '/upload/video',
      name: 'upload-video',
      component: UploadVideo
    },
    {
      path: '/upload/:id',
      name: 'upload-delete',
      component: ConfrimeImgDeleteView
    },
    {
      path: '/upload/video/:id',
      name: 'upload-video-delete',
      component: ConfrimeVideoDeleteView
    },
  ]
})

export default router
