import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";

axios.interceptors.request.use((config) => {
  let user = store.getters.getUser;
  if (user !== null && user !== undefined) {
    let token = user.token;
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
