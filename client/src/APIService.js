import axios from 'axios';
const API_URL = 'http://localhost:8000';
export class APIService {

    constructor() {
    }

    getUsers() {
        const url = `${API_URL}/api/v1/users/`;
        return axios.get(url).then(response => response.data);
    }


    createUsers(user) {

        const url = `${API_URL}/api/v1/users/`;
        return axios.post(url, user);
    }

    updateUser(data) {
        const url = `${API_URL}/api/v1/users/${data.id}`;
        const api_data = {
            method: "put",
            url,
            data,
          };
        return axios(api_data).then(response => response.data);
    }
    getUser(id) {
        const url = `${API_URL}/api/v1/users/:id`;
        return axios.get(url, id).then(response => response.data);
    }

    deleteUser(id) {
        const url = `${API_URL}/api/v1/users/$id`;
        return axios.delete(url, id);
    }

}