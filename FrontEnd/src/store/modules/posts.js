import { createPost, getAllPosts } from "../../services/posts";

const state = {
  posts: null,
  postsStatus: 0, // -1: error, 0: Not loaded, 1: Posts Loading, 2: Posts Loaded Successfully
};

const getters = {
  getPosts: (state) => state.posts,
  getPostsStatus: (state) => state.postsStatus,
};

const mutations = {
  setPosts: (state, newPostList) => (state.posts = newPostList),
  setPostsStatus: (state, updatedStatus) => (state.postsStatus = updatedStatus),
};

const actions = {
  // TODO: Add functions to retrieve posts from API
  async loadAllPosts({ commit }) {
    let allPostsResponse = await getAllPosts();
    if (allPostsResponse.status == 200) {
      commit("setPosts", allPostsResponse.data);
      return allPostsResponse.data;
    } else {
      commit("setPostsStatus", -1);
      return [];
    }
  },
  async createPost({ commit, state }, postInfo) {
    let newPostResponse = await createPost(postInfo).catch((e) => e);
    if (newPostResponse.status === 200) {
      commit("setPosts", [...state.posts, newPostResponse.data]);
    }
    return newPostResponse.data;
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
