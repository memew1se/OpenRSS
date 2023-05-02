import {defineStore} from "pinia";

export const useSideMenuStore = defineStore("sidemenu", () => {
    const isHidden = ref(false)

    function hide() {
        isHidden.value = !isHidden.value
    }

    return {
        isHidden,
        hide,
    }
})
