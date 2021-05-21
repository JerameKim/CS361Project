<template>
  <div :class="darkState">
    <appHeader :darkMode="true" v-if="darkActive" ></appHeader>
    <appHeader :darkMode="false" v-if="!darkActive" ></appHeader>

    <b-button variant="dark" class="darkButton" v-if="!darkActive" @click = "switchDark">Dark Mode</b-button>
    <b-button variant="light" class="darkButton" v-if="darkActive" @click = "switchDark">Light Mode</b-button>

    <img alt="Weird Globe1" src="/assets/simpleGlobe.png" height = "200px" width = "250px">
    <h1>WikiReducer</h1>
    <p>Wikipedia, but simpler<br></p>
    <form id = "main-form"  onsubmit="return false"> 
      <div>
        <input id="user-url" type="text" v-model = "wikiURL" v-on:keyup="verifyURL(wikiURL)" placeholder ="Enter a valid Wikipedia URL">
        <!-- <button id = "submit-btn" class="main-btn"  type="button" @click="verifyURL(wikiURL)">Go!</button> -->
        <router-link id ="go-btn" v-if="isValid" :to="referenceTag" tag="button"> Go! </router-link>
      </div>
    </form>
    <div>
      <br>
      <br>
      <!-- This btn will take us to component with the api links -->
      <router-link to="/filter" id="filter-btn" class ="main-btn btn btn-light">Advanced</router-link>
    </div>
  </div>
</template>

<script>
import Header from "./Header"
// import FiltersView from "./Filters";

// when this is component is referenced then it will have these attributes
export default {
  
  name: 'Home',
  
  data() { 
    return { 
      wikiURL: "", 
      wikiFront: "https://en.wikipedia.org/wiki/", // 30 chars here 
      userFront: "",
      isWiki: 2, // 0 for match, anything else for not match
      wikiTag: "",
      lang: "", 
      referenceTag: "",
      isValid: false, 
      darkActive: false,
    }
  },
  computed: { 
    darkState() { 
      return this.darkActive ? 'dark--active' : 'dark--inactive';
    }
  },
  methods: { 
    switchDark(){ 
      this.darkActive = !this.darkActive
    },
    // Handle the wikipedia URL to find tag, 
    // make call to heroku to see if we can work it in
    verifyURL(inputURL){ 

      // get the lang
      this.lang = inputURL.slice(8, 10)
      // get the tag
      this.wikiTag = inputURL.slice(30)

      // Exact match and total length is great, 
      if((inputURL.length> 30)){ 
        // Is a wikipedia page, route to somewhere else.
        this.isValid = true;
        this.referenceTag = "/content/" + this.lang + "/" + this.wikiTag;
        console.log("Valid input");
        console.log(this.referenceTag)
      } else {
        console.log("Input invalid")
      }
    },
  },
  components: { 
    appHeader: Header,
  },
}
</script>

<style scoped>

/* Colors 

Baby Blue: #D4F1F4
Blue Green: #75E6DA
Blue Grotto: #189AB4
Navy Blue: #05445E

 */
.dark--inactive{
  background-color: blue;
  /* background-color: white */
  color:  #2c3e50;
} 

.dark--active{ 
  background-color: red
  /* background-color: black */
}
.darkButton { 
  position: absolute; 
  top: 0; 
  right: 0;
  margin-top: 80px;
  margin-right: 30px;
}
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
#go-btn{ 
  margin-left: 30px;
	font-size:25px;
	font-weight:350;
  height: 3.3rem; 
  width: 7rem;
	border-radius: 8px;

}
#filter-btn{ 
  background-color: #3ddbcc;
	border-radius: 8px;
	font-size:20px;
	font-weight:350;
  height: 3rem; 
  width: 8rem;
  text-align: center;
	text-shadow:0px 1px 0px grey;
}
.main-btn { 
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
