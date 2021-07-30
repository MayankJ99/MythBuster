<template>
  <v-app>
    <v-app-bar app color="#1B1E27" dark>
      <v-spacer></v-spacer>
      <v-btn
        class="profile-btn"
        depressed
        elevation="2"
        icon
        raised
        rounded
        small
        min-width="50"
      >
        <v-avatar size="30" color="#57BAFF">
          <v-icon color="#1B1E27">mdi-account-outline</v-icon>
        </v-avatar>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
