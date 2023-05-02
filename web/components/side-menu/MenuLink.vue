<script setup lang="ts">
defineProps<{
  link: RssLink
}>()
</script>

<template>
  <NuxtLink
    class="flex flex-col bg-secondary rounded-2xl items-center p-3 m-3 lg:mx-10 lg:text-2xl sm:text-xl"
    :to="link.slug"
    ><span class="">{{ link.title }}</span></NuxtLink
  >
</template>
