<template>
  <div class="hello">
    <h1>Wikipedia Scraper</h1>
    <p> What in the Wikipedia?<br></p>
    <form> 
      <div>
        <input id="user-url" name="user-url-input" type="text" v-model = "message" placeholder ="Enter URL">

        <button id = "submit-btn">Go!</button>
      </div>
    </form>
  </div>
</template>

<script>
// when this is component is referenced then it will have these attributes
export default {
  name: 'home',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#user-url {
  background-color: white;
  border-width: 20px;
  border-style: solid;
  width: 30px;
  height: 40px;
  /* border: none; */
}
</style>
