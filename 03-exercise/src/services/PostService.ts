import { ref, type Ref } from 'vue'
import type { IPost } from '@/interfaces/IPost'

class PostService {
  private posts: Ref<IPost[]>
  private URL: string
  private post: Ref<IPost>

  constructor() {
    this.posts = ref<IPost[]>([])
    this.URL = 'https://jsonplaceholder.typicode.com/posts'
    this.post = ref<IPost>({})
  }

  getPosts(): Ref<IPost[]> {
    return this.posts
  }

  getPost(): Ref<IPost> {
    return this.post
  }

  async fetchAll(): Promise<void> {
    try {
      const response = await fetch(this.URL)
      const json = await response.json()

      this.posts.value = await json
    } catch (error) {
      console.error(error)
    }
  }

  async fetchPost(id: string | string[]): Promise<void> {
    try {
      const response = await fetch(`${this.URL}/${id}`)
      const json = await response.json()

      this.post.value = await json
    } catch (error) {
      console.log(error)
    }
  }
}

export default PostService
