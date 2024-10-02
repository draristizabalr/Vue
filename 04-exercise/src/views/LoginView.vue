<template>
    <main class="container">
        <h1>Login</h1>
        <form>
            <label for="username">Nombre de Usuario:</label>
            <input type="text" name="username" autocomplete="off" v-model="username" />
            <label for="password">Contraseña:</label>
            <input type="password" name="password" autocomplete="off" v-model="password" />
            <div class="button-container">
                <button type="submit" @click.prevent="loginUser">Ingresar</button>
                <RouterLink :to="{ name: 'register' }" class="register-button">Register</RouterLink>
            </div>
        </form>
    </main>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'
import { RouterLink } from 'vue-router'
import useAuth from '@/stores/auth'
import router from '@/router'

const store = useAuth()
const username: Ref<string> = ref('')
const password: Ref<string> = ref('')

const loginUser = async () => {
    const result = (await store.login(username.value, password.value)) as boolean

    if (result) {
        username.value = ''
        password.value = ''
        router.push({ name: 'note-list' })
    }
}
</script>

<style scoped>
.container {
    width: 100%;
    height: 100%;
    padding: 4em 2em;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 2em;
}

form {
    width: 32rem;
    padding: 2rem 1rem;
    border: 1px dashed #333;
    border-radius: 0.5rem;
    background-color: lightgray;
    display: grid;
    grid-template-columns: 30% 1fr;
    grid-template-rows: repeat(2, 1fr) 4rem;
    gap: 1rem;
}

label {
    display: flex;
    color: #333;
    align-items: center;
    font-weight: bold;
}

input {
    padding: 0.75rem;
    border-radius: 0.5rem;
    border: 1px solid #666;
}

.button-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: end;
    gap: 2em;
    grid-column: 1 / 3;
}

button,
.register-button {
    cursor: pointer;
    width: fit-content;
    height: fit-content;
    padding: 0.25em 0.5em;
    font-size: 1.25em;
    border: 1px solid #555;
    border-radius: 0.5rem;
    text-decoration: none;
    color: whitesmoke;
}

button {
    background-color: cornflowerblue;
}

.register-button {
    background-color: salmon;
}

button:hover,
.register-button:hover {
    scale: 1.05;
}

button:active,
.register-button:active {
    scale: 0.95;
}
</style>
