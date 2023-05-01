// https://nuxt.com/docs/api/configuration/nuxt-config
import svgLoader from "vite-svg-loader"
export default defineNuxtConfig({
  css: ['~/assets/css/main.css'],
  modules: ['@nuxtjs/tailwindcss'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  vite: {
    plugins: [svgLoader()],
  },
})
