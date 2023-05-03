<script setup lang="ts">
import Logo from "@/assets/icons/button.svg"
import { useSideMenuStore } from "~/store/sidemenu"
const sideMenuStore = useSideMenuStore()
</script>

<template>
  <button v-on:click="sideMenuStore.hide"><Logo class="top-1/2" /></button>
</template>
