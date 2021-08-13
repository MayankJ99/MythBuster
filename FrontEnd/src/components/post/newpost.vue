<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field v-model="post.title" outlined dense label="Title" />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-textarea
            v-model="post.question_text"
            outlined
            dense
            label="Your Question"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
export default {
  name: "NewPostForm",
  props: ["post"],
};
</script>

<style></style>
