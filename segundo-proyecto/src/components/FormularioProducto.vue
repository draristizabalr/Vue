<template>
  <form class="formulario-productos" @submit="handleSubmit($event)">
    <h3>Formulario de productos</h3>
    <label for="name">Nombre del producto</label>
    <input type="text" name="name" id="name" placeholder="Manzana, Mesa, Televisor, ..." v-model="values.name" />
    <label for="price">Precio del producto</label>
    <input type="number" name="price" id="price" placeholder="3000, 200000, 1500000" v-model="values.price" />
    <div class="submit-button">
      <button type="submit">Agregar producto</button>
    </div>
  </form>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'
const emit = defineEmits(["enviarProducto"])
interface ValuesType {
  name: string,
  price: number,
}
let values:Ref<ValuesType> = ref({
  name: '',
  price: 0
})

const handleSubmit: Function = (event: Event) => {
  event.preventDefault()

  emit('enviarProducto', values)
}

</script>

<style scoped>
.formulario-productos {
  height: fit-content;
  padding: 3em 1em;
  display: grid;
  grid-auto-flow: row;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr;
  row-gap: 2em;
  align-self: center;
  border: 1px solid #333;
  border-radius: 1em;
}

.formulario-productos h3 {
  grid-column: 1 / 3;
  text-align: center;
  margin: 0;
  padding: 0;
  color: blue;
  background-color: aqua;
}
.formulario-productos input{
  max-height: 1.5em;
}

.submit-button {
  height: 100%;
  width: 100%;
  grid-column: 1 / 3;
  display: flex;
  justify-content: center;
  align-items: center;
}

.submit-button button {
  height: 100%;
  width: fit-content;
}
</style>