<template>
  <div class="post">
    <h3>{{ title }}</h3>
    <p>{{ content }}</p>
    <input type="text" 
      v-model="msg"
      @keydown.enter="handleChange()"
    >
  </div>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue'
defineProps({
  "title": String,
  "content": String,
})
const emit = defineEmits(["showMsg"])

const msg: Ref<string> = ref('')
const handleChange:Function = () => {
  emit("showMsg", msg.value)
}
</script>

<style scoped>
.post {
  width: 300px;
  height: 150px;
  background-color: antiquewhite;
  border-radius: 10px;
  padding: 10px;
}
</style>