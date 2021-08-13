<template>
  <v-app>
    <v-app-bar app color="#1B1E27" dark>
      <v-btn icon text v-if="!atHomeRoute" to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn v-if="getUser === null" outlined to="/login">Login</v-btn>
      <v-btn v-if="getUser === null" text to="/register">Register</v-btn>
      <v-btn text v-if="getUser !== null" to="/profile">{{
        getUser.username
      }}</v-btn>
      <v-btn icon v-if="getUser !== null" to="/new">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn
        v-if="getUser !== null"
        class="mr-2"
        icon
        elevation="2"
        raised
        color="#57BAFF"
        to="/profile"
      >
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
    atHomeRoute() {
      return this.$route.path === "/";
    },
  },
};
</script>
