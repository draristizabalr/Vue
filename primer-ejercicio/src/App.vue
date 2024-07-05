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

interface ProfesorType {
  nombres: string;
  apellidos: string;
  DNI: string;
  asignaturas: string;
}

interface InformacionType {
  nombres: string;
  apellidos: string;
  DNI: string;
  asignaturas: Array<string>;
}

const listaProfesores:Ref<Array<ProfesorType>> = ref([])

const parseInfo:Function = (informacion:InformacionType) => {
  const { nombres, apellidos, DNI, asignaturas } = informacion

  const asignaturasParsed:string = asignaturas.reduce((a: string, b: string) => a + ' - ' + b)

  listaProfesores.value.push({
    nombres,
    apellidos,
    DNI,
    asignaturas: asignaturasParsed
  })
}
</script>

<style scoped>
.container {
  max-height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 25% 1fr;
  grid-template-rows: 1fr;
  gap: 0 2em;
}
</style>
