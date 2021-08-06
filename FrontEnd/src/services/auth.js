import axios from "axios";

export async function login(username, password) {
    return await axios.post(`${process.env.VUE_APP_API_URL}/api/users/login`, {
        username,
        password,
    });
}