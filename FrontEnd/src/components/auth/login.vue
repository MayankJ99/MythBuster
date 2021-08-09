<template>
  <v-container class="container">
    <v-form class="form">
      <v-text-field
        style="margin-bottom: 2%"
        v-model="loginInfo.username"
        label="Username"
        outlined
      />
      <v-text-field
        style="margin-bottom: 4%"
        v-model="loginInfo.password"
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
import { mapActions } from "vuex";

export default {
  data() {
    return {
      snackbar: false,
      loginState: 0, // 0 - Data entry, 1 - Processing, 2 - Success, 3 - Failure
      loginInfo: {
        username: "",
        password: "",
      },
      rules: {
        username(value) {
          return (
            /^[a-zA-Z0-9]{4,}$/g.test(value) ||
            "Your username must be at least 4 alphanumeric characters"
          );
        },
        eightMinimum(value) {
          return (
            /^[\S]{8,}$/.test(value) || "This field needs at least 8 characters"
          );
        },
        password(value) {
          if (!/[a-z]/g.test(value)) {
            return "Your password needs at least one lower case letter";
          }
          if (!/[A-Z]/g.test(value)) {
            return "Your password needs at least one upper case letter";
          }
          if (!/[0-9]/g.test(value)) {
            return "Your password needs at least one number";
          }
          if (!/[\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]/g.test(value)) {
            return "Your password needs at least one special character";
          }
          return true;
        },
        nonEmpty(value) {
          return (
            (value !== "" && value !== null && value !== undefined) ||
            "This field cannot be empty"
          );
        },
      },
    };
  },
  methods: {
    ...mapActions(["login"]),
    async onLoginClick() {
      this.loginState = 1;
      let loginResponse = await this.login(
        this.loginInfo.username,
        this.loginInfo.password
      );
      this.loginState = loginResponse.status === 201 ? 2 : 3;
      if (loginResponse.status) {
        setTimeout(() => {
          this.$router.push("/");
        }, 1000);
      }
    },
  },
  computed: {
    snackbarColor() {
      switch (this.loginState) {
        case 1:
          return "warning";
        case 2:
          return "success";
        case 3:
          return "error";
        default:
          return "info";
      }
    },
    snackbarText() {
      switch (this.loginState) {
        case 1:
          return "Logging in...";
        case 2:
          return "Logged in!";
        case 3:
          return "Error Logging in";
        default:
          return "Something seems strange...";
      }
    },
  },
  watch: {
    loginState(value) {
      this.snackbar = value !== 0;
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
