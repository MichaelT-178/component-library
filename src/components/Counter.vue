<template>
  <div>
    <h1>Counter</h1>
    <p>Current count: {{ count }}</p>
    <button @click="increment">Increment</button>
    <button @click="decrement">Decrement</button>
  </div>
</template>


<script setup>
import { ref } from 'vue'

const count = ref(0)

const increment = () => {
  count.value++
}

const decrement = () => {
  count.value--
}

</script>


<style scoped>

h1 {
  color: #42b983;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  border: none;
  background-color: #42b983;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #359a72;
}

</style>
