<template>
  <h1>Listado de posts</h1>
  <ul class="post-list">
    <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
  </ul>
</template>

<script lang="ts" setup>
import PostService from '@/services/PostService';  
import { onMounted } from 'vue';

const service = new PostService()
const posts = service.getPosts()

onMounted(async (): Promise<void> => {
  await service.fetchAll()
})

</script>

<style scoped>
* {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif
}
h1, .post-list {
  text-align: center;
}
li {
  border: 1px solid #999;
  padding: 0.5em 0;
  list-style-type: none;
}
</style>