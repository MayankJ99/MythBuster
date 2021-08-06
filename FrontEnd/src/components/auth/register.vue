<template>
  <v-form>
    <v-stepper v-model="stepper">
      <v-stepper-step step="1" :complete="stepper > 2">
        Account Info
      </v-stepper-step>
      <v-stepper-content step="1">
        <v-text-field
          v-model="registrationInfo.username"
          label="Username"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.email"
          label="Email"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.password"
          label="Password"
          outlined
          dense
          type="password"
        />
        <v-btn color="primary" @click="stepper = 2">Continue</v-btn>
      </v-stepper-content>
      <v-stepper-step step="2" :complete="stepper > 3">
        Your Info
      </v-stepper-step>
      <v-stepper-content step="2">
        <v-text-field
          v-model="registrationInfo.first_name"
          label="First Name"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.last_name"
          label="Last Name"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.bio"
          label="Your Bio"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.occupation"
          label="Occupation"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.location"
          label="Location"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.education"
          label="Education"
          outlined
          dense
        />
        <v-btn @click="stepper = 1">Back</v-btn>
        <v-btn color="primary" @click="stepper = 3">Continue</v-btn>
      </v-stepper-content>
      <v-stepper-step step="3"> Social Media </v-stepper-step>
      <v-stepper-content step="3">
        <v-text-field
          v-model="registrationInfo.linkedin"
          label="LinkedIn"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.twitter"
          label="Twitter"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.github"
          label="GitHub"
          outlined
          dense
        />
        <v-text-field
          v-model="registrationInfo.website"
          label="Website"
          outlined
          dense
        />
        <v-btn @click="stepper = 2">Back</v-btn>
        <v-btn>Register</v-btn>
      </v-stepper-content>
    </v-stepper>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      stepper: 1,
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
    onRegisterClick() {
      console.log(this.registrationInfo);
    },
  },
};
</script>
