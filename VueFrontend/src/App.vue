<template>
  <div id="app" >
    <!-- <appHeader ></appHeader> -->
    <!-- <appContent></appContent> -->
    <router-view ></router-view>
  </div>
</template>

<script>
  // import Header from "./components/Header";
  // import Content from "./components/Content";

  export default {
    name: 'App',
    data() { 
      return { 
        darkActive: false,
      }
    },
    computed: { 
      darkState() { 
        return this.darkActive ? 'dark--active' : 'dark--inactive';
      }
    },
    components: {
      // appHeader: Header,
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

#noData {
    padding-top: 100px; 
    text-align: center;
}

</style>
