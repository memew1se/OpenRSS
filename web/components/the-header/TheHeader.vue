<script setup lang="ts">
import TheLogo from "~/components/TheLogo.vue"
import TheButton from "~/components/TheButton.vue"
</script>

<template>
  <header class="sticky top-0 w-full h-32">
    <div class="bg-accent flex h-32 items-center justify-between p-10">
      <TheButton />
      <TheLogo />
    </div>
  </header>
</template>
