<script setup lang="ts">
import MenuLink from "~/components/side-menu/MenuLink.vue"
import { useSideMenuStore } from "~/store/sidemenu"

const { data: rsslinks } = await useFetch<RssLink[]>("/main-feed/", {
    baseURL: useRuntimeConfig().public.apiBase,
})
const sideMenuStore = useSideMenuStore()
</script>

<template>
  <div
    v-if="!sideMenuStore.isHidden"
    id="sidemenu"
    class="flex flex-col w-1/3 bg-primary fixed h-screen"
  >
    <MenuLink v-for="link in rsslinks" :link="link" />
  </div>
</template>
