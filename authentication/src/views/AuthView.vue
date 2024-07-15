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
import AuthService from '@/services/AuthServices'

let email: Ref<string> = ref('')
let password: Ref<string> = ref('')

const authUser = async () => {
  const auth = new AuthService()
  const success = await auth.login(email.value, password.value)

  if (success) {
    alert('Exito')
  } else {
    alert('Login incorrecto')
  }
}
</script>

<style scoped></style>
