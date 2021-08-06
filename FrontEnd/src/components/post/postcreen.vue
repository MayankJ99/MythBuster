<template>
  <v-container class="ma-14 pa-0 cont">
    <v-row class="start">
      <v-col cols="12" md="9">
        <v-card color="#252a36" dark elevation="0">
          <v-card-title>
            <v-row>
              <v-btn
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
              <h4 class="username">EloBellow</h4>
            </v-row>
          </v-card-title>
          <v-card-title class="text-h4 title">
            Default VueJS projects require less files than default ReactJS
            projects
          </v-card-title>
          <v-card-text>January 1, 1970</v-card-text>
          <v-card-text class="desc"
            >Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam
            lacinia, metus in pharetra facilisis, libero est mattis lorem, non
            dictum felis nulla nec ante. Integer placerat neque eu risus auctor,
            id dapibus eros consequat. Quisque accumsan iaculis dolor eget
            pharetra. Nunc mollis consequat ante, a iaculis felis lacinia quis.
            Vivamus aliquet aliquam imperdiet. Aliquam erat volutpat. Donec
            ultricies dolor a tortor bibendum faucibus. Vestibulum mollis in
            turpis sit amet vehicula. Duis ultrices, purus sed laoreet bibendum,
            urna lectus rutrum mauris, vel finibus magna elit quis massa. Nulla
            sed nulla et mi dignissim gravida. Phasellus consequat feugiat
            libero, et tristique sapien euismod in. Sed et sem eget orci
            malesuada rhoncus et eget nulla. Suspendisse pulvinar id nunc non
            ullamcorper.
          </v-card-text>
          <v-card-text class="desc">
            Pellentesque sollicitudin consequat cursus. Cras purus dolor,
            imperdiet vitae laoreet blandit, finibus at massa. Morbi eu porta
            tellus. Aliquam hendrerit viverra fringilla. In et blandit est.
            Donec velit odio, vestibulum at nulla ac, tincidunt convallis
            tellus. Proin porttitor elementum massa id mattis. Aliquam vulputate
            interdum augue, in egestas enim tincidunt eu. Interdum et malesuada
            fames ac ante ipsum primis in faucibus. Fusce ac dolor vitae quam
            laoreet aliquet. Pellentesque iaculis mauris non tellus gravida
            facilisis.
          </v-card-text>
          <v-card-actions><v-divider></v-divider></v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="12" md="3">
        <v-card color="#1B1E27" dark elevation="4" class="claims" rounded>
          <v-card-title>3 claims</v-card-title>
          <v-card-text><v-divider></v-divider></v-card-text>
          <v-col v-for="n in 2" :key="n">
            <v-row>
              <v-col>
                <p style="color: gainsboro; margin: 0px; font-weight: 500">
                  VueJS has less files
                </p>
                <p>7 Agree</p>
              </v-col>
            </v-row>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.cont {
  max-width: 90vw;
}
.start {
  margin-top: 2%;
}
.username {
  text-align: center;
  align-content: center;
  justify-content: center;
  color: #57baff;
  margin-left: 1%;
  font-size: 1rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
.title {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  word-break: keep-all;
}
.desc {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin-left: 1rem;
  font-size: 1rem;
  word-spacing: 2px;
}
p {
  color: grey;
}
/* .claims {
  align-content: flex-end;
  text-align: end;
  justify-content: end;
} */
</style>
