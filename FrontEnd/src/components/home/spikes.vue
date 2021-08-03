<template>
  <v-container>
    <v-row style="margin-top: 1%">
      <h1 class="spikeText">Spikes</h1>
      <v-spacer></v-spacer>
      <v-btn
        class="spikeBtn popular white--text"
        depressed
        elevation="2"
        raised
        rounded
        small
        color="#9673ff"
        >Popular
      </v-btn>
      <v-btn
        class="spikeBtn recent white--text"
        depressed
        elevation="2"
        raised
        rounded
        small
        color="#57BAff"
        >Recent
      </v-btn>
    </v-row>
    <template>
      <v-item-group class="spikeVideos">
        <v-container>
          <v-row>
            <v-col v-for="n in 6" :key="n" cols="12" md="2">
              <v-item v-slot="{ active, toggle }">
                <v-card
                  :color="active ? 'primary' : ''"
                  class="d-flex align-center"
                  dark
                  height="250"
                  width="200"
                  elevation="6"
                  @click="toggle"
                >
                  <v-scroll-y-transition>
                    <div v-if="active" class="text-h2 flex-grow-1 text-center">
                      Active
                    </div>
                  </v-scroll-y-transition>
                </v-card>
              </v-item>
              <p class="spikeVideoSubtitle">17 chained 🔥</p>
            </v-col>
          </v-row>
        </v-container>
      </v-item-group>
    </template>
  </v-container>
</template>

<script>
export default {
  name: "SpikesSeciton",
};
</script>

<style scoped>
.spikeText {
  color: #57baff;
  margin-left: 2%;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.spikeVideos {
  margin-top: 1%;
}

.spikeVideoSubtitle {
  margin-top: 10px;
  margin-left: 1%;
  color: #979797;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.spikeBtn {
  margin-top: 1%;
  text-transform: none;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.popular {
  opacity: 1;
  margin-right: 1%;
}

.recent {
  opacity: 0.7;
  margin-right: 2%;
}
</style>
