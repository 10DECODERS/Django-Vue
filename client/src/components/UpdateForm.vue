<template>
  <div id="container">
    <form @submit="updateUser">
      <p>Update User</p>
      <label>First name</label>
      <input v-model="employee.first_name" id="fisrtname" type="text" />
      <label>Last name</label>
      <input v-model="employee.last_name" id="lastname" type="text" />
      <label>DOB</label>
      <input v-model="employee.DOB" id="dob" type="date" />
      <input type="submit" value="update" class="btn submit-btn prev-btn" />
    </form>
  </div>
</template>

<script>
import { APIService } from "../APIService";
const apiService = new APIService();
export default {
  name: "update-form",
  data() {
    return {
      employee: {
        id: "",
        first_name: "",
        last_name: "",
        DOB: ""
      }
    };
  },
  methods: {
    async updateUser(e) {
      e.preventDefault();
      let result = await apiService.updateUser(this.employee);
      if (result) {
        this.$router.push("/users");
      }
    }
  },
  mounted() {
    this.employee = this.$router.history.current.params;
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
</style>
