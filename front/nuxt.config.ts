// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  ssr: true,
  devtools: {
    enabled: true,
  },
  modules: [
    '@pinia/nuxt',
    '@nuxt/eslint',
  ],
  imports: {
    autoImport: true,
    dirs: ['./utils/', './utils/api', './store/'],
  },
  eslint: {
    config: {
      standalone: false,
    },
  },
  css: ['~/assets/scss/global.scss'],
})
