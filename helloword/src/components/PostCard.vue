<template>
  <div class="post-card">
    <h3>Titulo</h3>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consectetur veritatis, nesciunt deserunt rerum quos et, rem maxime voluptatum exercitationem dignissimos sed commodi quia quis, aspernatur labore. Suscipit architecto tempora recusandae!</p>
    <PostButton />
  </div>
</template>
<script lang="ts" setup>
import PostButton from './PostButton.vue';

</script>
<style>
  .post-card {
    border-radius: 15px;
    padding: 10px;
    margin: 5px;
    border: 1px solid #ccc;
  }
</style>