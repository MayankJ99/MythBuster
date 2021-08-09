<template>
  <v-container class="container">
    <v-form class="form">
      <v-text-field
        style="margin-bottom: 2%"
        v-model="registrationInfo.username"
        label="Username"
        outlined
      />
      <v-text-field
        style="margin-bottom: 4%"
        v-model="registrationInfo.password"
        label="Password"
        outlined
      />
      <v-btn
        dark
        outlined
        class="mr-4"
        @click="onLoginClick"
        color="#9673FF"
        ripple="#9673FF"
      >
        Login
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      registrationInfo: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    usernameRule(value) {
      return /^[a-zA-Z0-9]{4,}$/g.test(value)
        ? null
        : "Usernames may only be alphanumeric characters";
    },
    eightMinimum(value) {
      return /^[\S]{8,}$/.test(value) ? null : "This field cannot be empty";
    },
    nonEmpty(value) {
      return /^.{1,}[\S]*.{1,}$/.test(value)
        ? null
        : "This field cannot be empty";
    },
    onLoginClick() {
      console.log(this.registrationInfo);
    },
  },
};
</script>

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
