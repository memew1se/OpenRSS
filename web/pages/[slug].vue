<script setup lang="ts">
const rssentries = [
  {
    title: "Very long title this is",
    link: "https://google.com",
    date: "2002.02.01",
  },
  { title: "Short title", link: "https://google.com", date: "2002.02.02" },
]
</script>

<template>
  <h1 class="text-center font-bold text-5xl m-5">{{ $route.params.slug }}</h1>
  <div
    class="flex flex-col border border-2 border-dashed border-indigo-600 mx-[10rem] my-10 p-5"
  >
    <ul>
      <TheRSSEntry v-for="entry in rssentries" :rssentry="entry" />
    </ul>
  </div>
</template>
