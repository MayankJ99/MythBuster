<template>
  <div>
    <v-container>
      <v-row>
        <v-col class="text-h3" cols="12">
          {{ getUser.first_name }} {{ getUser.last_name }}
        </v-col>
      </v-row>
      <v-row class="ma-0">
        <v-col class="text-subtitle-1 pa-0 grey--text" cols="12">
          @{{ getUser.username }}
        </v-col>
      </v-row>
      <v-row class="ma-0">
        <v-col class="text-subtitle-1 pa-0 grey--text" cols="12">
          Joined on {{ createdDate }}
        </v-col>
      </v-row>
      <v-row class="ma-0">
        <v-col class="text-subtitle-1 pa-0" cols="12">
          {{ getUser.profile.bio }}
        </v-col>
      </v-row>
      <v-row v-if="getUser.profile.linkedin" class="ma-0">
        <v-col class="text-subtitle-1 pa-0" cols="12">
          LinkedIn {{ getUser.profile.linkedin }}
        </v-col>
      </v-row>
      <v-row v-if="getUser.profile.twitter" class="ma-0">
        <v-col class="text-subtitle-1 pa-0" cols="12">
          LinkedIn {{ getUser.profile.twitter }}
        </v-col>
      </v-row>
      <v-row v-if="getUser.profile.github" class="ma-0">
        <v-col class="text-subtitle-1 pa-0" cols="12">
          LinkedIn {{ getUser.profile.github }}
        </v-col>
      </v-row>
    </v-container>
    <v-container class="ma-14 pa-0">
      <v-row>
        <v-col>Your Posts</v-col>
      </v-row>
      <v-row class="start">
        <v-col :key="post.id" v-for="post in userPosts" cols="12">
          <post
            :title="post.title"
            :body="post.question_text"
            :labels="post.tags"
            :timestamp="post.created_at"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import post from "../components/post/post.vue";
export default {
  components: { post },
  name: "Profile",
  methods: {
    ...mapActions(["loadAllPosts"]),
  },
  created() {
    this.loadAllPosts();
  },
  computed: {
    ...mapGetters(["getUser", "getPosts"]),
    userPosts() {
      let posts = this.getPosts
        ? this.getPosts.filter((post) => post.user === this.getUser.username)
        : [];
      console.log(posts);
      return posts;
    },
    createdDate() {
      const monthList = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ];
      let creationDate = new Date(this.getUser.profile.created_at);
      let day = creationDate.getDate();
      let month = monthList[creationDate.getMonth()];
      let year = creationDate.getFullYear();
      return `${month} ${day}, ${year}`;
    },
  },
};
</script>
