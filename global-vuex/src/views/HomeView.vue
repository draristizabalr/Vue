<template>
  <h3>Counter: {{ counter }}</h3>
  <h3>{{ counter }} x2 = {{ times2 }}</h3>
  <button @click="increment">Incrementar</button>
  <button @click="reset()">Reset counter</button>
</template>

<script lang="ts" setup>
import { useStore } from 'vuex'
import { computed } from 'vue'
import { key } from '@/store/store'

const store = useStore(key)

const counter = computed(() => store.state.count)
const times2 = computed(() => store.getters.times2)

const increment = () => store.commit('increment')
const reset = () => store.commit('reset')
</script>

<style scoped>
.counter {
  color: red;
  font-size: 2em;
}
</style>
