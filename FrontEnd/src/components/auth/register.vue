<template>
  <v-form ref="registerForm" lazy-validation>
    <v-snackbar top v-model="snackbar" :timeout="3000" :color="snackbarColor">
      {{ snackbarText }}
    </v-snackbar>
    <v-stepper v-model="stepper" vertical>
      <v-stepper-step step="1" :complete="stepper > 1" color="">
        Account Info
      </v-stepper-step>
      <v-stepper-content step="1">
        <v-text-field
          v-model="registrationInfo.username"
          label="Username"
          :autofocus="stepper === 1"
          ref="formUsername"
          :rules="[rules.nonEmpty, rules.username]"
          class="pt-1"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.email"
          label="Email"
          ref="formEmail"
          :rules="[rules.nonEmpty, rules.email]"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.password"
          label="Password"
          ref="formPassword"
          outlined
          :rules="[rules.nonEmpty, rules.eightMinimum, rules.password]"
          dense
          type="password"
        />
        <v-btn color="primary" @click="attemptNextStep">Continue</v-btn>
      </v-stepper-content>
      <v-stepper-step step="2" :complete="stepper > 2">
        Your Info
      </v-stepper-step>
      <v-stepper-content step="2">
        <v-text-field
          v-model="registrationInfo.first_name"
          label="First Name"
          :rules="[rules.nonEmpty]"
          ref="formFirstName"
          :autofocus="stepper === 2"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.last_name"
          label="Last Name"
          :rules="[rules.nonEmpty]"
          ref="formLastName"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.bio"
          label="Your Bio"
          :rules="[rules.nonEmpty]"
          ref="formBio"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.occupation"
          label="Occupation (Optional)"
          ref="formOccupation"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.location"
          label="Location (Optional)"
          ref="formLocation"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.education"
          label="Education (Optional)"
          ref="formEducation"
          outlined
          dense
        />
        <v-btn @click="stepper = 1" class="mr-2">Back</v-btn>
        <v-btn color="primary" @click="attemptNextStep">Continue</v-btn>
      </v-stepper-content>
      <v-stepper-step step="3"> Social Media </v-stepper-step>
      <v-stepper-content step="3">
        <v-text-field
          v-model="registrationInfo.linkedin"
          label="LinkedIn (Optional)"
          :autofocus="stepper === 3"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.twitter"
          label="Twitter (Optional)"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.github"
          label="GitHub (Optional)"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.website"
          label="Website (Optional)"
          outlined
          dense
        />
        <v-btn @click="stepper = 2" class="mr-2">Back</v-btn>
        <v-btn @click="onRegisterClick" color="primary">Register</v-btn>
      </v-stepper-content>
    </v-stepper>
  </v-form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      stepper: 1,
      snackbar: false,
      registerState: 0, // 0 - Data entry, 1 - Processing, 2 - Success, 3 - Failure
      registrationInfo: {
        email: "",
        username: "",
        password: "",
        first_name: "",
        last_name: "",
        bio: "",
        occupation: "",
        location: "",
        education: "",
        linkedin: "",
        twitter: "",
        github: "",
        website: "",
      },
      rules: {
        username(value) {
          return (
            /^[a-zA-Z0-9]{4,}$/g.test(value) ||
            "Your username must be at least 4 alphanumeric characters"
          );
        },
        email(value) {
          return (
            /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(value) ||
            "Please enter a valid email address"
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
    ...mapActions(["register"]),
    async onRegisterClick() {
      this.registerState = 1;
      let registerResponse = await this.register(this.registrationInfo);
      this.registerState = registerResponse.status === 201 ? 2 : 3;
      if (registerResponse.status) {
        setTimeout(() => {
          this.$router.push("/");
        }, 1000);
      }
    },
    attemptNextStep() {
      switch (this.stepper) {
        case 1:
          if (
            !(
              this.$refs["formUsername"].validate() &&
              this.$refs["formEmail"].validate() &&
              this.$refs["formPassword"].validate()
            )
          ) {
            this.$refs["registerForm"].validate();
            return;
          }
          break;
        case 2:
          if (
            !(
              this.$refs["formFirstName"].validate() &&
              this.$refs["formLastName"].validate() &&
              this.$refs["formBio"].validate() &&
              this.$refs["formOccupation"].validate() &&
              this.$refs["formLocation"].validate() &&
              this.$refs["formEducation"].validate()
            )
          ) {
            return;
          }
          break;
        default:
          break;
      }
      this.$refs["registerForm"].resetValidation();
      this.stepper += 1;
    },
  },
  computed: {
    snackbarColor() {
      switch (this.registerState) {
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
      switch (this.registerState) {
        case 1:
          return "Creating Account...";
        case 2:
          return "Account Created!";
        case 3:
          return "Error Creating Account";
        default:
          return "Something seems strange...";
      }
    },
  },
  watch: {
    registerState(value) {
      this.snackbar = value !== 0;
    },
  },
};
</script>

<style scoped>
.theme--dark.v-stepper {
  background: #252a36;
}
</style>
