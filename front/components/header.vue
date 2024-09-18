<script setup lang="ts">
const links = [
  {
    name: 'Home',
    url: '/',
  },
  {
    name: 'About',
    url: '/about',
  },
  {
    name: 'Command',
    url: '/command',
  },
  {
    name: 'Profile',
    url: '/profile',
  },
]
</script>

<template>
  <div class="header">
    <div class="loog">
      <h3>Pipao</h3>
    </div>
    <div class="links">
      <router-link v-for="link in links" :key="link.name" class="h5" :to="link.url">
        {{ link.name }}
      </router-link>
    </div>
  </div>
</template>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;

  .links {
    display: flex;
    gap: 30px;
  }
}
</style>
