<template>
  <ul>
    <li v-for="country in countries" :key="country.code">{{ country.name }}</li>
  </ul>
</template>

<script setup lang="ts">
  import { Ref, ref } from 'vue'
  interface ICountry {
    code: string,
    name: string
  }
  let countries:Ref<Array<ICountry>> = ref([
    {code: 'es', name:'Spain'},
    {code: 'fr', name:'France'},
    {code: 'uk', name:'UK'},
    {code: 'it', name:'Italy'},
    {code: 'pr', name:'Portugal'},
    {code: 'co', name:'Colombia'}
  ])
</script>