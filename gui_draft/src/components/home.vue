<template>
  <div>
    <img alt="Weird Globe1" src="/assets/globe.jpg" contain height = "200px" width = "200px">
    <h1>Wikipedia Scraper</h1>
    <p> What in the Wikipedia?<br></p>
    <form id = "main-form"> 
      <div>
        <input id="user-url" name="user-url-input" type="text" v-model = "message" placeholder ="Enter URL">
        <button id = "submit-btn" class="main-btn" >Go!</button>
      </div>
    </form>
    <div>
      <!-- This btn will take us to component with the api links -->
      <button id = "api-btn" class="main-btn">Advanced</button>
      <!-- <button id = "api-btn" class="main-btn">APIs</button> -->
    </div>
  </div>
</template>

<script>
// when this is component is referenced then it will have these attributes
export default {
  name: 'Home',
  data() { 
    return { 
      message: ""
    }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

/* Colors 

Baby Blue: #D4F1F4
Blue Green: #75E6DA
Blue Grotto: #189AB4
Navy Blue: #05445E

 */
#user-url {
  background-color: white;
  border-radius: 8px;
  border-style: solid;
  border-color: #e6e6e6;
  font-size: 30px;
  width: 25rem;
  height: 2rem;
  padding: 10px;

}
#user-url:focus{ 
  outline: none;
  border-color: #cbf1f5;
}
#submit-btn{ 
  margin-left: 30px;
	font-size:25px;
	font-weight:350;
  height: 3.3rem; 
  width: 7rem;
}
#api-btn{ 
  background-color: #3ddbcc;
	border-radius: 8px;
  margin-top: 5rem;
	font-size:20px;
	font-weight:350;
  height: 3rem; 
  width: 8rem;
  text-align: center;
	text-shadow:0px 1px 0px grey;
}
.main-btn { 
  background-color: #3ddbcc;
	border-radius: 8px;
	cursor:pointer;
	color: white;
	padding: 10px;
  text-align: center;
	text-shadow:0px 1px 0px grey;
}
.main-btn:hover{ 
  background:linear-gradient(to bottom, #3ddbcc 5%, #599bb3 100%);
	background-color:#408c99;
}
.main-btn:active{ 
  position:relative;
	top:1px;
}

</style>
