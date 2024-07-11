<template>
  <h1>Blog page</h1>
  <ul>
    <li><RouterLink :to="{ name: 'post' , params: { id: 1 } }">Primer post</RouterLink></li>
    <li><RouterLink :to="{ name: 'post' , params: { id: 2 } }">Segundo post</RouterLink></li>
    <li><RouterLink :to="{ name: 'post' , params: { id: 3 } }">Tercer post</RouterLink></li>
    <li><RouterLink :to="{ name: 'post' , params: { id: 4 } }">Cuarto post</RouterLink></li>
    <li><RouterLink :to="{ name: 'post' , params: { id: 5 } }">Quinto post</RouterLink></li>
  </ul>

</template>

<script lang="ts" setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>