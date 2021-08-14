<template>
  <v-container>
    <!-- <spikes-seciton /> -->
    <posts-section />
  </v-container>
</template>

<script>
import SpikesSeciton from "./spikes.vue";
import PostsSection from "./posts.vue";

export default {
  name: "HomeScreen",
  components: {
    SpikesSeciton,
    PostsSection,
  },
};
</script>
