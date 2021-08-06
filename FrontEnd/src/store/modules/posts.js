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
};

export default {
    state,
    getters,
    mutations,
    actions,
};