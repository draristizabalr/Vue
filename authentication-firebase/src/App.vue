<template>
  <nav class="navigation">
    <RouterLink v-for="route, index in routes" :key="index" :to="{ name: route.name}">{{ route.label }}</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

interface routesType {
  name: string,
  label: string
}
const routes: routesType[] = [
  { name: 'home', label: 'Home'},
  { name: 'login', label: 'Login'},
  { name: 'social', label: 'Social Login'},
  { name: 'example', label: 'Example View'},
]
</script>

<style scoped>
.navigation {
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 1em;
}
</style>
