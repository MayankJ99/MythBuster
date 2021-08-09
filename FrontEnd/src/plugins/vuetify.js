import Vue from "vue";
import Vuetify from "vuetify/lib";

const vuetify = new Vuetify({
  theme: {
    themes: {
      dark: {
        primary: "#9673FF",
        secondary: "#1b1e27",
      },
    },
    dark: true,
  },
});

Vue.use(Vuetify);

export default vuetify;
