import axios from "axios";

export async function login(username, password) {
  return await axios.post(`${process.env.VUE_APP_API_URL}/api/users/login/`, {
    username: username,
    password: password,
  });
}

export async function register(userInfo) {
  return await axios.post(
    `${process.env.VUE_APP_API_URL}/api/users/register/`,
    userInfo
  );
}

export async function getCurrentUserInfo() {
  return await axios.get(`${process.env.VUE_APP_API_URL}/api/users/profile/`);
}
