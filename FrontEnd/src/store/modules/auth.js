import { login } from "../../services/auth";

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
    async login(commit, { username, password }) {
        const authResponse = await login(username, password).catch((e) => e);
        commit("setUser", authResponse.data);
    },
};

export default {
    state,
    getters,
    mutations,
    actions,
};