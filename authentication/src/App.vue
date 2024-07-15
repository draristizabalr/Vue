<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
      <RouterLink :to="{ name: 'auth' }">Access</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script lang="ts" setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped></style>
