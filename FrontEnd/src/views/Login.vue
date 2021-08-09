<template>
  <v-container class="ma-6 cont">
    <v-row align="center" justify="center">
      <v-col cols="12" md="7">
        <v-card color="#1B1E27" class="card" rounded dark elevation="4">
          <v-card-title>Welcome back</v-card-title>
          <v-card-text>
            <login-screen />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="5">
        <v-row class="title">
          <h2 class="myth">Myth&nbsp;</h2>
          <h2 class="buster">Buster</h2>
        </v-row>
        <v-row class="content">
          <p>
            A platform where Programmers can post topics or opinions to be
            discussed and scrutinized
          </p>
        </v-row>

        <v-row class="animation">
          <v-img
            src="../assets/animation.svg"
            class="ma-10 animation"
            max-width="24rem"
          ></v-img>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LoginScreen from "../components/auth/login.vue";

export default {
  name: "Login",
  components: {
    LoginScreen,
  },
};
</script>

<style scoped>
.cont {
  max-width: 90vw;
}
.title {
  display: flex;
  justify-content: center;
  margin-top: 6rem;
  margin-bottom: 2rem;
  margin-left: 6rem;
  margin-right: 6rem;
}
.content {
  display: flex;
  justify-content: center;
  text-align: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 1rem;
  color: #c5baba;
  margin-top: 0%;
  margin-left: 4rem;
  margin-right: 4rem;
}
.myth {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #9673ff;
  font-size: 3rem;
}
.buster {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #57baff;
  font-size: 3rem;
}
.animation {
  display: flex;
  justify-content: center;
  text-align: center;
  margin-top: 4rem;
}
.card {
  padding-top: 6%;
  padding-bottom: 4%;
  margin-top: 6%;
}
</style>
