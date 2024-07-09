<template>
  <div>
    <input type="text" v-model="message" />
    <h3 v-custom-size:lg>{{ message }}</h3>
    <h3 v-font-size>{{ reverse }}</h3>
    <h3 v-custom-fount.lg.blue>{{ reverse }}</h3>

  </div>
</template>

<script lang="ts" setup>
import { computed, ref, type ComputedRef, type Ref } from 'vue'

let message: Ref<string> = ref('')
const reverse: ComputedRef = computed(() => message.value.split('').reverse().join(''))
</script>

<style scoped></style>
