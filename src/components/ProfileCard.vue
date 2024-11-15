<template>
  <div class="profile-card">
    <img :src="profileImage" alt="Profile Picture" class="profile-image" />
    <h1>{{ name }}</h1>
    <p>{{ bio }}</p>
  </div>
</template>


<script setup>
import { ref } from 'vue';

const profileImage = ref('https://via.placeholder.com/150');
const name = ref('John Doe');
const bio = ref('Programming guy who programs programs.');

</script>


<style scoped>
.profile-card {
  text-align: center;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  max-width: 300px;
  margin: 0 auto;
}

.profile-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 15px;
}

h1 {
  font-size: 20px;
  color: #333;
  margin-bottom: 10px;
}

p {
  font-size: 14px;
  color: gray;
}
</style>
