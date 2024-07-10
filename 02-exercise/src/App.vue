<template>
  <div class="container">
    <FormularioProducto @enviar-producto="takeProduct($event)" />
    <TablaProductos :product-list="productsList" />
  </div>
</template>

<script lang="ts" setup>
import { type Ref, ref } from 'vue'
import FormularioProducto from './components/FormularioProducto.vue'
import TablaProductos from './components/TablaProductos.vue'

let productsList: Ref<Array<{ name: string; price: number }>> = ref([])

const takeProduct: Function = (values: Ref<{ name: string; price: number }>) => {
  const { name, price } = values.value
  productsList.value.push({ name, price })
}
</script>

<style scoped>
.container {
  height: 100vh;
  width: 100%;
  display: grid;
  grid-template-columns: 20% 1fr;
  grid-template-rows: 1fr;
  gap: 2em 0;
}
</style>
