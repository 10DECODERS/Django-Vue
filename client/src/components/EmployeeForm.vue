<template>
  <div id="container">
    <div class="container">
      <p>ADD USER</p>
      <b-form-group id="input-group-1" label="First name" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.first_name"
          type="text"
          required
          placeholder="first name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="last Name:" label-for="input-2">
        <b-form-input
          id="lastname"
          v-model="user.last_name"
          type="text"
          required
          placeholder="Last name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="DOB:" label-for="input-3">
        <b-form-input id="DOB" v-model="user.DOB" type="date" required placeholder="DOB"></b-form-input>
      </b-form-group>

      <b-button variant="primary" class="submitbtn" @click="createUsers(user)">Submit</b-button>
    </div>
  </div>
</template>

<script>
import { APIService } from "../APIService";
const apiService = new APIService();
export default {
  name: "employee-form",
  data() {
    return {
      user: {
        first_name: "",
        last_name: "",
        DOB: ""
      }
    };
  },
  methods: {
    createUsers: function(user) {
      apiService.createUsers(user).then(data => {
        if (data) {
          this.first_name = user.first_name;
          this.last_name = user.last_name;
          this.DOB = user.DOB;
          this.$router.push("/users");
        }
      });
    }
  }
};
</script>

<style scoped>
input {
  width: 275px;
}
form {
  margin-left: 20px;
}
#container {
  margin-top: 60px;
  margin-left: auto;
  margin-right: auto;
  width: 600px;
}
.submitbtn {
  text-align: center;
}
</style>
