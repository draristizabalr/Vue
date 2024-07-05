<template>
  <form class="form">
    <label for="name">Escribe tu nombre</label>
    <input type="text" name="name" id="name" v-model="inputText">
    <label for="agree">
      <input type="checkbox" v-model="agree" name="agree" id="agree">
      Acepto terminos y condiciones
    </label>
    <label for="country">Selecciona tu pais de origen</label>
    <select name="country" id="country" v-model="selection">
      <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
    </select>
  </form>
  <h3 v-if="inputText && selection" :style="{color: agree ? 'green' : 'red'}">{{ `Hola ${inputText} de ${selection}` }}</h3>
</template>

<script lang="ts" setup>
import { ref, Ref } from 'vue'

const countries:Array<string> = ['Spain', 'Portugal', 'France', 'USA', 'Germany', 'Colombia']

let inputText:Ref<string> = ref(''),
    agree:Ref<boolean> = ref(false),
    selection: Ref<string> = ref('')


</script>

<style scope>
.form {
  width: 20%;
  display: flex;
  flex-direction: column;
  gap: 0.5em;
}
</style>