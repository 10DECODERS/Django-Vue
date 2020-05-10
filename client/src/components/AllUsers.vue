<template>
  <div id="employee-table">
    <div class="btn">
      <router-link to="/adduser">
        <b-button variant="outline-primary">Add User</b-button>
      </router-link>
    </div>
    <p>List of Users</p>
    <table>
      <thead>
        <tr>
          <th>id</th>
          <th>First name</th>
          <th>Last name</th>
          <th>DOB</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user of responses" :key="user.id">
          <td>{{user.id}}</td>
          <td>{{ user.first_name }}</td>
          <td>{{ user.last_name }}</td>
          <td>{{user.DOB}}</td>
          <td>
            <button @click="updateUser(user)">edit</button>
          </td>
          <td>
            <button class="btn" @click="deleteUser(user.id)">
              <i class="fa fa-trash"></i>
            </button>
          </td>
          <b-modal id="bv-modal-example" hide-footer title="User">
            <div class="d-block text-center">
              <div>first name:{{user.first_name}}</div>
              <div>Last name:{{user.last_name}}</div>
              <div>DOB:{{user.DOB}}</div>
              <b-button class="mt-2" variant="outline-danger" block @click="hideModal">Close</b-button>
            </div>
          </b-modal>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { APIService } from "../APIService";

// const API_URL = 'http://localhost:8000';
const apiService = new APIService();

export default {
  name: "all-users",

  data() {
    return {
      responses: [],
      user: []
    };
  },
  methods: {
    getUsers() {
      apiService.getUsers().then(response => {
        this.responses = response.response;
      });
    },
    getUser(id) {
      fetch("http://localhost:8000/api/v1/users/" + id, {
        method: "GET"
      }).then(response => {
        this.user = response;
        console.log("3333333", this.user);
      });
    },

    deleteUser(id) {
      fetch("http://localhost:8000/api/v1/users/" + id, {
        method: "DELETE"
      }).then(() => {
        console.log("DELETED");
        this.getUsers();
      });
    },
    updateUser: function(user) {
      this.$router.push({
        name:"update-form",
        params: {
          id: user.id,
          first_name: user.first_name,
          last_name: user.last_name,
          DOB: user.DOB
        },
        query:{
          id:user.id
        }
      });
    },
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    }
  },

  created() {
    this.getUsers();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  font-size: 45px;
}
.btn {
  text-align: end;
}
.adduser {
  width: 160px;
}
</style>
