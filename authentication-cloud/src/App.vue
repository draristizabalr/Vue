<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink> | 
      <RouterLink :to="{ name: 'auth' }">Auth</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>
