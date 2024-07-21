<template>
  <h1>Social Login</h1>
  <button v-for="social, index in socials" :key="index"
    @click="() => loginSocial(social)"
  >Login with {{ social }}</button>
</template>

<script lang="ts" setup>
  import { FacebookAuthProvider, GoogleAuthProvider, signInWithPopup, getAuth } from 'firebase/auth'

  interface socialsProvider {
    [key: string]: GoogleAuthProvider
    Google: GoogleAuthProvider
    Facebook: FacebookAuthProvider
  }
  
  const socialProvider: socialsProvider = {
    Google: new GoogleAuthProvider(),
    Facebook: new FacebookAuthProvider(),
  }
  const auth = getAuth()

  const loginSocial: Function = (social: string) => {
    signInWithPopup(auth, socialProvider[social])
      .then(() => {
        // const provider = socialProvider[social]
        // const credential = provider.credentialFromResult(result)
        // const token = credential?.accessToken
        // console.log(token)
        alert('Success!')
      })
      .catch( (error) => {
        console.log(error)
        alert('Login Failed!')
      })
  }
  const socials: string[] = [
    'Google',
    'Facebook'
  ]
</script>

<style scoped>

</style>