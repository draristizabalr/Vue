<template>
  <form class="formulario" @submit="chequed ? enviarFormulario($event) : reiniciarFormulario($event)">
    <label for="nombres">Nombres</label>
    <input type="text" name="nombres" id="nombres" v-model="nombres">
    <label for="apellidos">Apellidos</label>
    <input type="text" name="apellidos" id="apellidos" v-model="apellidos">
    <label for="DNI">DNI</label>
    <input type="text" name="DNI" id="DNI" v-model="DNI">
    <label for="asignaturas">Asignaturas</label>
    <select name="asignaturas" id="asignaturas" multiple="true" v-model="asignaturas">
      <option v-for="asignatura in listAsignaturas" :key="asignatura" :value="asignatura">
        {{ asignatura }}
      </option>
    </select>
    <label for="chequeado">
      <input type="checkbox" name="chequeado" id="chequeado" v-model="chequed">
      Documentos
    </label>
    <button type="submit" hidden></button>
  </form>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'
const emit = defineEmits(['enviarProfesor'])

const listAsignaturas:Array<string> = [
  'Literatura',
  'Matemáticas',
  'Inglés',
  'Ciencias Sociales',
  'Física',
  'Química',
  'Estadística',
  'Música',
  'Historia del Arte'
]

let nombres:Ref<string> = ref('')
let apellidos:Ref<string> = ref('')
let DNI:Ref<string> = ref('')
let asignaturas:Ref<Array<string>> = ref([])
let chequed: Ref<boolean> = ref(false)

const enviarFormulario:Function = (event: Event) => {
  event.preventDefault()

  emit('enviarProfesor', {
    nombres: nombres.value,
    apellidos: apellidos.value,
    DNI: DNI.value,
    asignaturas: asignaturas.value })

  reiniciarFormulario(event)
}

const reiniciarFormulario:Function = (event: Event) => {
  event.preventDefault()

  nombres.value = '' 
  apellidos.value = ''
  DNI.value = ''
  asignaturas.value = []
  chequed.value = false
}

</script>

<style scoped>
.formulario {
  height: fit-content;
  display: grid;
  grid-template-columns: 40% 1fr;
  grid-template-rows: repeat(3, 2em) 10em 1em;
  grid-auto-flow: row;
  gap: 1em 0;
  padding: 2em;
  margin-top: 5em;
  border: 1px solid #333;
  border-radius: 2em;
}
.formulario #nombres, #apellidos, #DNI {
  height: 1.5em;
}
</style>