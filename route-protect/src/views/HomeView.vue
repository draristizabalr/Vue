<template>
  <form class="formulario" @submit="sendToServer">
    <label for="note">Nota:</label>
    <input type="text" name="note" id="note">
    <button type="submit" class="boton">Enviar</button>
  </form>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'

let note: Ref<string> = ref('')

const URL = 'https://xxxxxxxxxxxxx'
const sendToServer = async () => {
  const response = await fetch(URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
    },
    body: JSON.stringify({
      note: note.value
    })
  })
  const result = await response.json()
}

</script>

<style scoped>
.formulario {
  width: 300px;
  margin: 1em;
  padding: 1em;
  display: grid;
  grid-template-columns: 20% 1fr;
  gap: 1em;
}
.boton {
  grid-column: 1 / 3;
}
</style>
