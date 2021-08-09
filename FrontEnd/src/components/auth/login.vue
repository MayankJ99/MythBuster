<template>
  <v-container class="container">
    <v-form class="form">
      <v-text-field
        style="margin-bottom: 2%"
        v-model="username"
        label="Username"
        outlined
      />
      <v-text-field
        style="margin-bottom: 4%"
        v-model="password"
        label="Password"
        outlined
      />
      <v-btn
        dark
        outlined
        class="mr-4"
        @click="validate"
        color="#9673FF"
        ripple="#9673FF"
      >
        Login
      </v-btn>
    </v-form>
  </v-container>
</template>

<style scoped>
.border {
  border: 1px solid white;
  background-color: #252a36;
  border-radius: 2rem;
}
.title {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.form {
  margin-top: 4%;
  margin-bottom: 4%;
}
</style>
