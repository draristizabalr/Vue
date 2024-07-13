<template>
  <header>
    <div class="back-link">
      <RouterLink to="/">Back</RouterLink>
    </div>
  </header>
  <div class="container">
    <div class="post-body">
      <h1 class="post-title">{{ post.title }}</h1>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted } from 'vue'
import PostService from '@/services/PostService';
import { useRoute } from 'vue-router';

const router = useRoute()
const service = new PostService()
const post = service.getPost()

onMounted(async (): Promise<void> => {
  const id: string | string[] = router.params.id
  await service.fetchPost(id)
}) 
</script>

<style scoped lang="scss">
* {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif
}
.container {
  width: 100%;
  height: 100%;
  padding: 1em;
  display: flex;
  justify-content: center;
  align-items: center;
}
.post-title {
  text-align: center;
  font-weight: bold;
  color: #5555ff;
}
.post-body {
  width: 50%;
  padding: 1em 2em;
  display: flex;
  flex-direction: column;
  gap: 1em;
  border: 1px solid #999;
  border-radius: 2em;
  background-color: #00ff0020;
}
.post-body p {
  text-align: center;
  color: #333;
}
header {
  margin-top: 1em;
}
.back-link {
  width: fit-content;
  margin-left: 2em;
  padding: 0.5em 1em;
  font-size: 20px;
  text-decoration: none;
  border: 1px solid #0000ff50;
  border-radius: 2em;
}
</style>