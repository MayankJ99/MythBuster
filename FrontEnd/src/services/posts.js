import axios from "axios";

export async function getAllPosts() {
  return await axios.get(
    `${process.env.VUE_APP_API_URL}/api/feed/questions/all/`
  );
}

export async function createPost(postInfo) {
  return await axios.post(
    `${process.env.VUE_APP_API_URL}/api/feed/createQuestion/`,
    postInfo
  );
}
