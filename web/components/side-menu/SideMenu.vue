<script setup lang="ts">
import MenuLink from "~/components/side-menu/MenuLink.vue"
import { useSideMenuStore } from "~/store/sidemenu"

const rsslinks = [
  { title: "title", slug: "slug" },
  { title: "title1", slug: "slug1" },
]
const sideMenuStore = useSideMenuStore()
</script>

<template>
  <div
    v-if="!sideMenuStore.isHidden"
    id="sidemenu"
    class="flex flex-col w-1/3 bg-primary fixed h-screen"
  >
    <MenuLink v-for="link in rsslinks" :link="link" :key="link.slug" />
  </div>
</template>
