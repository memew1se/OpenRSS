// https://nuxt.com/docs/api/configuration/nuxt-config
import svgLoader from "vite-svg-loader"
export default defineNuxtConfig({
  css: ["~/assets/css/main.css"],
  modules: ["@nuxtjs/tailwindcss", "@pinia/nuxt", "@kevinmarrec/nuxt-pwa"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  pwa: {
    workbox: {
      enabled: true,
    },
  },
  vite: {
    plugins: [svgLoader()],
  },
  runtimeConfig: {
    public: {
      apiBase: "http://127.0.0.1:8000/api",
    },
  },
})
