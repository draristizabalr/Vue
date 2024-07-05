<template>
  <div>
    
  </div>
</template>

<script lang="ts" setup>
import { onMounted, onUpdated } from 'vue'

onMounted (() => {
  alert("Mounted")
}) 

onUpdated (() => {
  alert("Updated")
})
</script>

<style scoped>

</style>