<template>
  <div>
    <h1>Hello world</h1>
  </div>
</template>

<script lang="ts">
export default {
  name: 'CycleOption',
  created () {
    console.log('Created')
  },
  mounted () {
    console.log('Mounted')
  },
  updated () {
    console.log('Updated')
  },
  unmounted () {
    console.log('Unmounted')
  }
}
</script>

<style scoped>

</style>