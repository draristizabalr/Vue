<template>
  <div class="container">
    <PostDetail v-for="post in info" :key="post.title"
      :title="post.title"
      :content="post.content"
      @show-msg="showAlert($event)"
    />
  </div>
</template>

<script lang="ts" setup>
import PostDetail from './PostDetail.vue'

interface Info  {
  title: string;
  content: string;
}

let info:Array<Info> = [
  {title: "Este es el post 1", content: "Texto de ejemplo 1"},
  {title: "Este es el post 2", content: "Texto de ejemplo 2"},
  {title: "Este es el post 3", content: "Texto de ejemplo 3"},
  {title: "Este es el post 4", content: "Texto de ejemplo 4"},
]

const showAlert:Function = (msg:string) => {
  alert(msg)
}
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-top: 1em;
}
</style>