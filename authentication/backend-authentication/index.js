import express from 'express'
import { PORT, SECRET_JWT_KEY } from './config.js'
import { UserRepository } from './user-repository.js'
import jwt from 'jsonwebtoken'
import cookieParser from 'cookie-parser'
import cors from 'cors'

const app = express()

app.use(express.json())
app.use(cookieParser())
app.use(cors())

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.post('/login', async (req, res) => {
  const { username, password } = req.body

  try {
    const user = await UserRepository.login({ username, password })
    const token = jwt.sign({ id: user._id, username: user.username }, SECRET_JWT_KEY, {
      expiresIn: '15m'
    })

    user.token = token

    res
      .cookie('acces_token', token, {
        httpOnly: true,
        // eslint-disable-next-line no-undef
        secure: process.env.NODE_ENV === 'production'
      })
      .send({ publicUser: user })
  } catch (error) {
    res.status(401).send(error)
  }
})

app.post('/register', async (req, res) => {
  const { username, password } = req.body

  try {
    const id = await UserRepository.create({ username, password })
    res.send({ id })
  } catch (error) {
    res.status(500).send(error)
  }
  res.send('Register route')
})

app.listen(PORT, () => {
  console.log(`Server runnning on port ${PORT}`)
})
