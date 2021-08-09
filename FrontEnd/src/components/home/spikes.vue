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
          <v-row style="row">
            <v-col v-for="n in 5" :key="n" cols="12" md="2" class="col">
              <v-item style="border-radius: 10px">
                <v-card dark elevation="6" height="250" width="200">
                  <video
                    controls
                    height="250"
                    width="170"
                    class="video"
                    src="https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_10mb.mp4"
                  />
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
// import videoPlayer from "vue-md-player";
// import "vue-md-player/dist/vue-md-player.css";

export default {
  name: "SpikesSeciton",
  // components: {
  //   videoPlayer,
  // },
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
  margin-left: 4%;
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
.video {
  object-fit: cover;
}
.col {
  margin-right: 2%;
}
</style>
