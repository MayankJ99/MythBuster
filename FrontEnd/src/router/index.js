import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Post from "../views/Post.vue";
import Register from "../views/Register.vue";
import Profile from "../views/Profile.vue";
import NewPost from "../views/NewPost.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/post",
    name: "Post",
    component: Post,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/profile",
    name: "My Profile",
    component: Profile,
  },
  {
    path: "/new",
    name: "New Post",
    component: NewPost,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
