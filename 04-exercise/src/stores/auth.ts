import { defineStore } from 'pinia'

const useAuth = defineStore('auth', {
    state: () => {
        return {
            token: null,
            baseURL: 'http://127.0.0.1:8000'
        }
    },
    actions: {
        async register(name: string, username: string, email: string, password: string) {
            const uri = `${this.baseURL}/auth/register`
            const response = await fetch(uri, {
                method: 'POST',
                headers: {
                    'Content-type': 'Application/json',
                    Accept: 'Application/json'
                },
                body: JSON.stringify({ name, username, email, password })
            })

            const result = await response.json()

            if (response.status === 200) {
                alert('El usuario ha sido registrado exitosamente')

                return true
            } else if (response.status === 400) {
                alert(result.detail)

                return false
            }

            // TODO: Manage result
        },
        async login(username: string, password: string) {
            const uri = `${this.baseURL}/auth/login`
            const response = await fetch(uri, {
                method: 'POST',
                headers: {
                    'Content-type': 'Application/json',
                    Accept: 'Application/json'
                },
                body: JSON.stringify({ username, password })
            })

            const result = await response.json()

            if (response.status === 200) {
                this.token = result.access_token

                return true
            } else if (response.status === 401) {
                alert(result.detail)

                return false
            }
        },
        async logout() {
            this.token = null
        },
        async getNotes() {
            const uri = `${this.baseURL}/notes`
            const response = await fetch(uri, {
                headers: {
                    'Content-type': 'Application/json',
                    Accept: 'Application/json',
                    Authorization: `Bearer ${this.token}`
                }
            })

            const result = await response.json()

            if (response.status === 200) {
                return result
            } else if (response.status === 400) {
                alert(result.detail)

                return []
            }
        },
        async createNotes(title: string, description: string) {
            const uri = `${this.baseURL}/notes`
            const response = await fetch(uri, {
                method: 'POST',
                headers: {
                    'Content-type': 'Application/json',
                    Accept: 'Application/json',
                    Authorization: `Bearer ${this.token}`
                },
                body: JSON.stringify({ title, description })
            })

            const result = await response.json()

            if (response.status === 200) {
                alert('Se ha creado la nota de forma correcta')

                return true
            } else if (response.status === 400) {
                alert(result.detail)

                return false
            }
        }
    }
})

export default useAuth
