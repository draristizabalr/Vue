<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/about">About</RouterLink> |
        <RouterLink to="/services">Services</RouterLink> |
        <RouterLink to="/contact">Contact</RouterLink> |
        <RouterLink to="/blog">Blog</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
nav {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 1em;
}
.router-link-active, .router-link-exact-active {
  color: red;
}
</style>
