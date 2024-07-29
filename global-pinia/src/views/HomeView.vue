<template>
  <h3>Counter: {{ store.count }}</h3>
  <h3>{{ store.count }} x 2 = {{ store.times2 }}</h3>
  <button @click="store.incremente(1)">Increment</button>
  <button @click="store.reset">Reset</button>
</template>

<script lang="ts" setup>
  import { useCounterStore } from '@/store/counter'
  const store = useCounterStore()
</script>

<style scoped>

</style>