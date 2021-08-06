<template>
  <v-container>
    <v-row style="margin-top: 3%">
      <h1 class="postsText">Posts</h1>
      <v-spacer></v-spacer>
      <v-btn
        class="postsBtn popular white--text"
        depressed
        elevation="2"
        raised
        rounded
        small
        color="#9673ff"
        >Popular
      </v-btn>
      <v-btn
        class="postsBtn recent white--text"
        depressed
        elevation="2"
        raised
        rounded
        small
        color="#57BAff"
        >Recent
      </v-btn>
    </v-row>
    <v-col v-for="n in 2" :key="n">
      <v-card color="#252a36" dark elevation="0">
        <v-card-title class="text-h5 title">
          Default VueJS projects require less files than default ReactJS
          projects
        </v-card-title>
        <v-card-text class="content"
          >Lorem Ipsum is simply dummy text of the printing and typesetting
          industry. Lorem Ipsum has been the industry's standard dummy text ever
          since the 1500s, when an unknown printer took a galley of type and
          scrambled it to make a type specimen book. It has survived not only
          five centuries, but also the leap into electronic typesetting,
          remaining essentially unchanged. It was popularised in the 1960s with
          the release of Letraset sheets containing Lorem Ipsum passages, and
          more recently with desktop publishing software like Aldus PageMaker
          including versions of Lorem Ipsum.
        </v-card-text>
        <v-card-text class="date">
          <v-col>
            <v-row>January 1, 1970</v-row>
            <v-row
              ><p>7 comments</p>
              <p>&nbsp; | &nbsp;</p>
              <p>2 claims</p></v-row
            >
          </v-col>
        </v-card-text>

        <v-card-actions>
          <v-row style="margin-left: 1%">
            <v-btn
              depressed
              elevation="2"
              raised
              rounded
              color="#FE9898"
              x-small
              class="tag"
              >ReactJS</v-btn
            >
            <v-btn
              depressed
              elevation="2"
              raised
              rounded
              color="#41B883"
              x-small
              class="tag"
              >VueJS</v-btn
            >
            <v-btn
              depressed
              elevation="2"
              raised
              rounded
              color="#616161"
              x-small
              class="tag"
              >Comparison</v-btn
            >
          </v-row>
        </v-card-actions>
        <!-- <v-divider style="margin-top: 4%"></v-divider> -->
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
export default {
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
