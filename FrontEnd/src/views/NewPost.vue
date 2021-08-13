<template>
  <v-card class="ma-0 ma-md-12 py-4">
    <v-card-title>New Post</v-card-title>
    <v-card-text>
      <newpost :post="post" />
    </v-card-text>
    <v-card-actions class="px-md-4">
      <v-spacer />
      <v-btn @click="onCreate" color="#9673FF">Submit</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
import newpost from "../components/post/newpost.vue";
export default {
  components: { newpost },
  name: "NewPost",
  data() {
    return {
      post: {
        title: "",
        question_text: "",
      },
    };
  },
  methods: {
    ...mapActions(["createPost"]),
    onCreate() {
      // let tags = this.post.tags.split(",").map((item) => item.trim());
      this.createPost(this.post);
      this.$router.push("/");
    },
  },
};
</script>
