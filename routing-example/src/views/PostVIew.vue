<template>
  <h1>Post View del elemento: {{ postId }}</h1>
</template>

<script lang="ts" setup>
import { onMounted, ref, type Ref } from 'vue';
import { useRoute } from 'vue-router';

let postId: Ref<string> = ref('')

onMounted(() => {
  const route = useRoute()
  postId.value = route.params.id
})
</script>

<style scoped>

</style>