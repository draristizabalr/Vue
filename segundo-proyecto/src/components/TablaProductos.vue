<template>
  <table class="tabla-productos">
    <thead>
      <th v-for="titulo in titulos" :key="titulo">{{ titulo }}</th>
    </thead>
    <tbody>
      <tr v-for="(product, index) in productListComplited" :key="product.name">
        <td>{{ index }}</td>
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.taxes }}</td>
        <td>{{ product.totalValue }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
import { type ComputedRef, type PropType, computed } from 'vue'

const props = defineProps({
  productList: Array as PropType<Product[]>
})

interface Product {
  name: string
  price: number
}

interface ProductComplite {
  name?: string
  price?: number
  taxes?: number
  totalValue?: number
}

const valorImpuestos: number = 10

const titulos: Array<string> = ['ID Product', 'Nombre', 'Precio', 'Valor impuestos', 'Valor total']

const productListComplited: ComputedRef = computed((): ProductComplite[] => {
  const productListComplited = props.productList!.map((product: Product): ProductComplite => {
    let { name, price } = product
    return {
      name: name,
      price: price,
      taxes: Math.fround(price * valorImpuestos / 100),
      totalValue: Math.fround(price * (valorImpuestos / 100 + 1))
    }
  })
  return productListComplited
})
</script>

<style scoped>
.tabla-productos {
  align-self: flex-start;
  border-collapse: collapse;
  margin-top: 6em;
}

.tabla-productos * {
  border: 1px solid #666;
  text-align: center;
}
</style>
