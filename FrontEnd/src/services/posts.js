import axios from "axios";

export async function getAllPosts() {
  return await axios.get(
    `${process.env.VUE_APP_API_URL}/api/feed/questions/all/`
  );
}
