<template>
  <v-container>
    <v-row>
      <v-spacer class="d-xs-none d-md-flex" />
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Sign Up</v-card-title>
          <v-card-text>
            <register />
          </v-card-text>
        </v-card>
      </v-col>
      <v-spacer class="d-xs-none d-md-flex" />
    </v-row>
  </v-container>
</template>

<script>
import register from "../components/auth/register.vue";
export default {
  components: { register },
};
</script>
