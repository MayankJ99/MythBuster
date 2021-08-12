<template>
  <v-app>
    <v-app-bar app color="#1B1E27" dark>
      <v-spacer></v-spacer>
      <v-btn v-if="getUser === null" outlined to="/login">Login</v-btn>
      <v-btn v-if="getUser === null" text to="/register">Register</v-btn>
      <v-btn class="mr-2" icon elevation="2" raised color="#57BAFF">
        <v-icon>mdi-account-outline</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main style="background-color: #252a36">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "App",
  data: () => ({
    //
  }),
  computed: {
    ...mapGetters(["getUser"]),
  },
  methods: {
    logUser() {
      console.log(this.getUser);
    },
  },
};
</script>
