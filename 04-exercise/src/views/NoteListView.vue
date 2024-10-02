<template>
    <main>
        <h1>Note list</h1>
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Titulo</th>
                    <th>Descripción</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(note, noteIndex) in notes" :key="noteIndex">
                    <td>{{ noteIndex + 1 }}</td>
                    <td>{{ note.title }}</td>
                    <td>{{ note.description }}</td>
                </tr>
            </tbody>
        </table>
        <div class="create-note-container" @click="router.push({ name: 'note-create' })">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="128"
                height="128"
                viewBox="0 0 1024 1024"
            >
                <path
                    fill="currentColor"
                    d="M799.344 960.288h-736v-800h449.6l64.704-62.336l-1.664-1.664H63.344c-35.344 0-64 28.656-64 64v800c0 35.344 28.656 64 64 64h736c35.344 0 64-28.656 64-64V491.632l-64 61.088zM974.224 41.44C945.344 13.76 913.473-.273 879.473-.273c-53.216 0-92.032 34.368-102.592 44.897c-14.976 14.784-439.168 438.353-439.168 438.353c-3.328 3.391-5.76 7.535-7.008 12.143c-11.488 42.448-69.072 230.992-69.648 232.864c-2.976 9.664-.32 20.193 6.8 27.217a26.64 26.64 0 0 0 18.913 7.84c2.752 0 5.52-.4 8.239-1.248c1.952-.656 196.496-63.569 228.512-73.12c4.224-1.248 8.048-3.536 11.216-6.624c20.208-19.936 410.112-403.792 441.664-436.384c32.624-33.664 48.847-68.657 48.223-104.097c-.591-35.008-17.616-68.704-50.4-100.128m-43.791 159.679c-17.808 18.368-157.249 156.16-414.449 409.536l-19.68 19.408c-29.488 9.12-100.097 31.808-153.473 49.024c17.184-56.752 37.808-125.312 47.008-157.743C444.8 466.464 808.223 103.6 822.03 89.968c2.689-2.689 27.217-26.257 57.44-26.257c17.153 0 33.681 7.824 50.465 23.92c20.065 19.248 30.4 37.744 30.689 55.024c.32 17.792-9.84 37.456-30.191 58.464"
                />
            </svg>
        </div>
        <button class="logout-button" @click.prevent="clickLogout">Cerrar sesión</button>
    </main>
</template>

<script lang="ts" setup>
import { ref, type Ref, onMounted } from 'vue'
import useAuth from '@/stores/auth'
import router from '@/router'

interface Note {
    id: number
    title: string
    description: string
    user_id: number
}

const store = useAuth()
const notes: Ref<Note[]> = ref([])

onMounted(async () => {
    const getNotes: Note[] = await store.getNotes()

    notes.value = getNotes
})

function clickLogout() {
    store.logout()
    router.push({ name: 'login' })
}
</script>

<style scoped>
main {
    width: 100%;
    padding: 3rem 2rem;
}

h1 {
    text-align: center;
    margin-bottom: 5rem;
}

table {
    width: 100%;
    border: 1px solid #444;
    border-collapse: collapse;
}

th {
    text-align: center;
    border: 1px solid #444;
    padding: 0.25rem 0.5rem;
    background-color: rgba(0, 125, 200, 0.8);
}

tbody tr:nth-child(even) {
    background-color: #ddd;
}

td {
    border: 1px solid #444;
    padding: 0.25em 0.5em;
}

td:first-child {
    text-align: center;
}

.create-note-container {
    cursor: pointer;
    position: absolute;
    bottom: 30px;
    right: 30px;
    width: 45px;
    height: 45px;
    padding: 0.75em;
    border-radius: 9999999em;
    background-color: rgba(0, 125, 200, 0.8);
    color: whitesmoke;
    display: flex;
    align-items: center;
    justify-content: center;
}

.create-note-container * {
    width: 30px;
    height: 30px;
}

.create-note-container:hover {
    scale: 1.3;
}

.create-note-container:active {
    scale: 0.9;
    background-color: rgba(0, 125, 200, 1);
}

.logout-button {
    position: absolute;
    top: 30px;
    right: 45px;
    color: whitesmoke;
    border: 1px solid #444;
    border-radius: 0.5rem;
    background-color: salmon;
    font-size: 18px;
    font-weight: bold;
}
</style>
