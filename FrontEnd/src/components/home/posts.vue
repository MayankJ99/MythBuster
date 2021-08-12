<template>
  <v-container>
    <postcreen />
  </v-container>
</template>

<script>
import postcreen from "../post/postcreen.vue";
export default {
  components: { postcreen },
  name: "PostsSection",
};
</script>

<style scoped>
.popular {
  opacity: 1;
  margin-right: 1%;
}

.recent {
  opacity: 0.7;
  margin-right: 2%;
}

.postsText {
  color: #57baff;
  margin-left: 2%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.postsBtn {
  margin-top: 1%;
  text-transform: none;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.content {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.96rem;
}

.title {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.date {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 0.8rem;
}

.tag {
  margin-right: 1%;
}
</style>
