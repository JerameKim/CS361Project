<template>
  <div>
    <img alt="Weird Globe1" src="/assets/globe.jpg" contain height = "200px" width = "200px">
    <h1>Wikipedia Scraper</h1>
    <p> What in the Wikipedia?<br></p>
    <form id = "main-form"  onsubmit="return false"> 
      <div>
        <input id="user-url" type="text" v-model = "wikiURL" v-on:keyup.enter="exampleFunction(wikiURL)" placeholder ="Enter your Wikipedia URL">
        <button id = "submit-btn" class="main-btn"  type="button" @click="exampleFunction(wikiURL)">Go!</button>
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
      wikiURL: "", 
      finalIndex: -1,
      wikiFront: "https://en.wikipedia.org/wiki/", // 30 chars here 
      userFront: "",
      isWiki: 2, // 0 for match, anything else for not match
    }
  },
  methods: { 
    // Handle the wikipedia URL to find tag
    exampleFunction(inputURL){ 
      this.finalIndex = inputURL.lastIndexOf("/")

      // First 30 chars of user input
      this.userFront = inputURL.slice(0, 30)
      // Compare userFront and "https://en.wikipedia.org/wiki/"
      this.isWiki = this.userFront.localeCompare(this.wikiFront)

      // 0 if exact match 
      if(this.isWiki == 0){ 
        // Make request to page and see if valid 
        // if page valid, do something
      } else {
        // do actions to show that not good 
        // animate button shake and make input form red
      }

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
  width: 25rem;
  height: 2rem;
  padding: 10px;
  font-size: 20px;

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
