import type { InjectionKey } from 'vue'
import { createStore, type Store } from 'vuex'

export interface State {
  count: number
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>({
  state () {
    return {
      count: 0
    }
  },
  getters: {
    times2(state: State): number {
      return state.count * 2
    }
  },
  mutations: {
    increment (state: State): void {
      state.count++
    },
    reset (state: State): void {
      state.count = 0
    },
    setCounter(state: State, value: number ) {
      state.count = value
    }
  },
  // actions: {

  // },
  // module: {

  // }
})
