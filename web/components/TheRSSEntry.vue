<script setup lang="ts">
defineProps<{
  rssentry: RssEntry
}>()
</script>

<template>
  <li class="m-10">
    <a
      :href="rssentry.link"
      target="_blank"
      class="underline text-blue-600 hover:text-blue-800 visited:text-purple-600"
      ><span class="text-3xl">{{ rssentry.title }}</span></a
    >
    <p>{{ rssentry.published }}</p>
  </li>
</template>
