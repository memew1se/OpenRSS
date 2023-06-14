<script setup lang="ts">
const { data: rssfeed } = await useFetch<RssFeed>(`/main-feed/${useRoute().params.slug}`, {
    baseURL: useRuntimeConfig().public.apiBase,
})
</script>

<template>
  <h1 class="text-center font-bold text-5xl m-5">{{ useRoute().params.slug }}</h1>
  <div
    class="flex flex-col md:mx-[10rem] my-10 p-5"
  >
    <ul>
      <TheRSSEntry v-for="entry in rssfeed.entries" :rssentry="entry" />
    </ul>
  </div>
</template>
