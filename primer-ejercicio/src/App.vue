<template>
  <div class="container">
    <FormularioInscripcion
      @enviar-profesor="parseInfo($event)"
    />
    <TablaProfesores 
      :listaProfesores="listaProfesores"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, type Ref } from 'vue'
import FormularioInscripcion from './components/FormularioInscripcion.vue'
import TablaProfesores from './components/TablaProfesores.vue'

const listaProfesores:Ref<Array<{ nombres: string, apellidos: string, asignaturas: string }>> = ref([])

const parseInfo:Function = (informacion:{ nombres: string, apellidos: string, asignaturas: Array<string> }) => {
  const { nombres, apellidos, asignaturas } = informacion

  const asignaturasParsed:string = asignaturas.reduce((a: string, b: string) => a + ' - ' + b)

  listaProfesores.value.push({
    nombres,
    apellidos,
    asignaturas: asignaturasParsed
  })
}
</script>

<style scoped>
.container {
  height: 100%;
  width: 100%;
  padding: 1em;
  display: grid;
  grid-template-columns: 25% 1fr;
  grid-template-rows: 1fr;
  gap: 0 2em;
}
</style>
