import { ref, type Ref } from 'vue'

class AuthService {
  private URL: string
  private jwt: Ref<string>
  private error: Ref<string>

  constructor() {
    this.URL = 'http://localhost:3000/'
    this.jwt = ref('')
    this.error = ref('')
  }

  getJwt(): Ref<string> {
    return this.jwt
  }

  getError(): Ref<string> {
    return this.error
  }

  async login(email: string, password: string): Promise<boolean> {
    try {
      const response = await fetch(this.URL + 'login', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify({ username: email, password })
      })
      const result = await response.json()

      console.log(response.status)
      console.log(result.status)

      if (response.status !== 200) {
        this.error.value = 'Login failed'
        return false
      } else {
        this.jwt.value = result.token
        return true
      }
    } catch (error) {
      this.error.value = 'Login failed'
      return false
    }
  }
}

export default AuthService
