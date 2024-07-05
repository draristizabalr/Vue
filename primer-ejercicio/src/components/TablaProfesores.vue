<template>
  <table class="tabla-profesores">
    <thead>
      <th v-for="(titulo, index) in titulos" :key="index">{{ titulo }}</th>
    </thead>
    <tbody>
      <tr v-for="(profesor, index) in props.listaProfesores" :key="index">
        <td v-for="(informacion, key, index) in profesor" :key="index">{{ informacion }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts" setup>
const props = defineProps(["listaProfesores"])

const titulos:Array<string> = ['Nombre', 'Apellido', 'Asignaturas']
</script>

<style scoped>
.tabla-profesores {
  width: 100%;
  height: fit-content;
  border-collapse: collapse;
  margin-top: 5em;
}
.tabla-profesores td,th {
  text-align: center;
  border: 1px solid #333;
  padding: 2px;
}
.tabla-profesores th {
  background-color: lightblue;
}
</style>