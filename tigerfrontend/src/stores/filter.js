import { defineStore } from "pinia";
import { ref } from "vue";

export const useFilterStore = defineStore('filter', () => {
    const filterRes = ref({})

    return { filterRes }
})
