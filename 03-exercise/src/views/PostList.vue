<template>
  <h1>Listado de posts</h1>
  <ul class="post-list">
    <RouterLink v-for="post in posts" :key="post.id" 
      class="route"
      :to="{ name: 'post', params: { id: post.id } }"
    >
      {{ post.title }}
    </RouterLink>
  </ul>
</template>

<script lang="ts" setup>
import PostService from '@/services/PostService';  
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';

const service = new PostService()
const posts = service.getPosts()

onMounted(async (): Promise<void> => {
  await service.fetchAll()
})

</script>

<style scoped lang="scss">
$red: #ff0000;
* {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
h1, .post-list {
  text-align: center;
}
ul {
  display: flex;
  flex-direction: column;
}
.route {
  border: 1px solid #999;
  padding: 0.5em 0;
  list-style-type: none;
  color: $red;
}

.route:hover {
  background-color: darken(#fff, 20%);
  cursor: pointer;
}

</style>