import { login, register, getCurrentUserInfo } from "../../services/auth";

const state = {
  user: null,
};

const getters = {
  getUser: (state) => state.user,
};

const mutations = {
  setUser: (state, user) => (state.user = user),
};

const actions = {
  async login({ commit }, { username, password }) {
    const authResponse = await login(username, password).catch((e) => e);
    commit("setUser", authResponse.data);
    const userInfo = await getCurrentUserInfo().catch((e) => e);
    commit("setUser", { ...authResponse.data, ...userInfo.data });
    return authResponse;
  },
  async register({ commit }, accountInfo) {
    const authResponse = await register(accountInfo).catch((e) => e);
    commit("setUser", authResponse.data);
    return authResponse;
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
