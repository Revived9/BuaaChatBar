<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id" class="post-item">
      <h3>{{ post.title }}</h3>
      <p>{{ post.excerpt }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  posts: {
    type: Array,
    required: true
  }
})
</script>
