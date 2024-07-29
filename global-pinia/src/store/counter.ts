import { defineStore } from "pinia"

export const useCounterStore = defineStore('counter', {
  state: () => {
    return {
      count: 0
    }
  },
  getters: {
    times2: (state) => state.count * 2
  },
  actions: {
    incremente(val = 1) {
      this.count += val
    },
    reset() {
      this.count = 0
    }
  }
})