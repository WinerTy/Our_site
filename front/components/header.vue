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

const router = useRoute()
</script>

<template>
  <div class="header">
    <div class="loog">
      <h4>Pipao.com</h4>
    </div>
    <div class="links">
      <template v-for="(link, i) in links" :key="i">
        <router-link
          :to="link.url"
          class="h5"
          :class="{ active: router.path === links[i].url }"
        >
          {{ link.name }}
        </router-link>
      </template>
    </div>
  </div>
</template>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;

  .links {
    display: flex;
    gap: 30px;

    a {
      transition: color 0.3s ease-in-out;

      &:hover {
        color: $color-primary;
      }
    }
  }
}

.active {
  color: $color-acnet;
}
</style>
