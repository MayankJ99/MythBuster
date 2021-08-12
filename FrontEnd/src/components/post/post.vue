<template>
  <v-card color="#252a36" elevation="0">
    <v-card-title>{{ title }}</v-card-title>
    <v-card-subtitle>{{ timestamp }}</v-card-subtitle>
    <v-card-text>
      {{ body }}
    </v-card-text>
    <v-card-actions>
      <v-chip :key="label" v-for="label in labels">
        {{ label.tag_name }}
      </v-chip>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Post",
  props: ["title", "body", "timestamp", "labels"],
};
</script>
