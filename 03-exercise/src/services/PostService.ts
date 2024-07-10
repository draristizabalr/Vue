import { ref, type Ref } from 'vue'
import type { IPost } from '@/interfaces/IPost'

class PostService {
  private posts: Ref<IPost[]>

  constructor () {
    this.posts = ref<IPost[]>([])
  }

  getPosts (): Ref<IPost[]> {
    return this.posts
  }

  async fetchAll (): Promise<void> {
    try {
      const URL: string = 'https://jsonplaceholder.typicode.com/posts'
      const response = await fetch(URL)
      const json = await response.json()

      this.posts.value = await json
    } catch (error) {
      console.error(error)
    }
  }
}

export default PostService