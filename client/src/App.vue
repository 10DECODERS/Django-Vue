<template>
  <div id="container">
     <!-- <all-users /> -->
    <router-view/>   
  </div>
</template>

<script>
//import AllUsers from './components/AllUsers.vue'

export default {
  name: 'App',
  //  components: {
  //   AllUsers,
  // }
}
</script>

<style>
#container{
    margin-top: 60px;
    margin-left: 100px;
    margin-right: 100px;
}
</style>
