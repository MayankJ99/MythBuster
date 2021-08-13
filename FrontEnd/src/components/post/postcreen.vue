<template>
  <v-container class="ma-14 pa-0 cont">
    <v-row class="start">
      <v-col :key="post.id" v-for="post in getPosts" cols="12">
        <post
          :title="post.title"
          :body="post.question_text"
          :labels="post.tags"
          :timestamp="post.created_at"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import post from "./post.vue";
export default {
  components: { post },
  name: "PostScreen",
  created() {
    this.loadAllPosts();
  },
  methods: {
    ...mapActions(["loadAllPosts"]),
  },
  computed: {
    ...mapGetters(["getPosts", "getPostsStatus"]),
  },
};
</script>

<style scoped>
.cont {
  max-width: 90vw;
}
.start {
  margin-top: 2%;
}
.username {
  text-align: center;
  align-content: center;
  justify-content: center;
  color: #57baff;
  margin-left: 1%;
  font-size: 1rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.title {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  word-break: keep-all;
}
.desc {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin-left: 1rem;
  font-size: 1rem;
  word-spacing: 2px;
}
p {
  color: grey;
}
/* .claims {
  align-content: flex-end;
  text-align: end;
  justify-content: end;
} */
</style>
