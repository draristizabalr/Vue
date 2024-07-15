<template>
  <div class="container mt-2">
    <form @submit.prevent="authUser">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          v-model="email"
        />
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth'

const email: Ref<string> = ref('')
const password: Ref<string> = ref('')

const authUser = () => {
  const auth = getAuth()
  signInWithEmailAndPassword(auth, email.value, password.value)
    .then(() => {
      alert('Éxito!')
    })
    .catch((error: Error) => {
      alert('Error: ' + error.message)
    })
}
</script>

<style scoped></style>
