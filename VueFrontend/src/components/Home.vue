<template>
  <div>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="<%= BASE_URL %>/css/darktheme.css"> -->
    <link href="<%= BASE_URL %>/css/darktheme.css">
    <appHeader></appHeader>
    <button id="darkButton" type="button" class="btn btn-secondary" @click="darkThemeSwitch">Switch Theme</button>
    <br>
    <img alt="Weird Globe1" src="/assets/simpleGlobe.png" height = "200px" width = "250px">
    <h1>WikiReducer</h1>
    <p>Wikipedia, but simpler<br></p>
    <form id = "main-form"  onsubmit="return false"> 
      <div>
        <input id="user-url" type="text" v-model = "wikiURL" v-on:keyup="verifyURL(wikiURL)" placeholder ="Enter a valid Wikipedia URL">
        <router-link class="btn btn-light" id ="go-btn" v-if="isValid" :to="referenceTag" tag="button" :showData="showAbstract">Go!</router-link>
      </div>
    </form>
    <br>
    <button class="button" v-on:click="showFilter = !showFilter">
      <i class="fa fa-angle-double-down"></i>
    </button>
    <div v-if="showFilter">
      <br>
      <h5>What would you like to see?</h5>
        <div class="row">
            <div class="col-sm">
                <p>Select sections you would like to see</p>
                <input type="checkbox" id="abstract" value="abstract" checked="true" v-model="showAbstract">
                <label for="abstract"> Abstract </label><br>
                <input type="checkbox" id="categories" value="categoires" checked = "false" v-model="showCategories">
                <label for="categories"> Categoires </label><br>
                <input type="checkbox" id="chapters" value="chapters" checked = "false" v-model="showChapters">
                <label for="chapters"> Chapters </label><br>
                <input type="checkbox" id="mainText" value="mainText" checked="true" v-model="showMain">
                <label for="mainText"> Main text</label><br>
                <input type="checkbox" id="photos" value="photos" checked="true" v-model="showPhotos">
                <label for="photos"> Photos </label><br>
                <input type="checkbox" id="citations" value="citations" checked="true" v-model="showCitations">
                <label for="citations"> Citations </label><br>
            </div>
        </div>
      <br>
    </div>
  </div>
</template>

<script>
import Header from "./Header";
// when this is component is referenced then it will have these attributes
export default {
  name: 'Home',
  data() { 
    return { 
      wikiURL: "", 
      userFront: "",
      isWiki: 2, // 0 for match, anything else for not match
      wikiTag: "",
      lang: "", 
      referenceTag: "",
      isValid: false, 
      darkActive: false,
      showFilter: false,

      showAbstract: true, 
      showCategories: true,
      showChapters: false, 
      showMain: true, 
      showPhotos: true, 
      showCitations: true,
    }
  },
  methods: { 
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
        // make the validation code 
        var abstractView = "0"; 
        var mainTextView = "0"; 
        var categoriesView = "0"; 
        var photosView = "0";
        var citationsView = "0"; 
        var chaptersView = "0";

        if(this.showAbstract) { 
          abstractView = "1";
        } 
        if(this.showCategories){
            categoriesView = "1" 
        } 
        if(this.showChapters){ 
          chaptersView = "1";
        }
        if(this.showMain){
          mainTextView = "1";
        } 
        if(this.showPhotos){
          photosView = "1";
        } 
        if(this.showCitations){ 
          citationsView = "1";
        }
        var showCode = abstractView + categoriesView + chaptersView + mainTextView + photosView + citationsView;
        // creates the url route
        this.referenceTag = "/content/" + showCode + "/" + this.lang + "/" + this.wikiTag + "/";
        // lets us know the reference tag and if it was succesful a
        // console.log("Valid input");
        // console.log(this.referenceTag)
      } else {
        // console.log("Input invalid")
      }
    },

    _addDarkTheme() {
      let darkThemeLinkEl = document.createElement("link");
      darkThemeLinkEl.setAttribute("rel", "stylesheet");
      darkThemeLinkEl.setAttribute("href", "/css/darktheme.css");
      darkThemeLinkEl.setAttribute("id", "dark-theme-style");

      let docHead = document.querySelector("head");
      docHead.append(darkThemeLinkEl);
    },
    _removeDarkTheme() {
      let darkThemeLinkEl = document.querySelector("#dark-theme-style");
      let parentNode = darkThemeLinkEl.parentNode;
      parentNode.removeChild(darkThemeLinkEl);
    },
    darkThemeSwitch() {
      let darkThemeLinkEl = document.querySelector("#dark-theme-style");
      if (!darkThemeLinkEl) {
        this._addDarkTheme()
      } else {
        this._removeDarkTheme()
      }
    },
  },
  components: { 
    appHeader: Header,
  },
}
</script>

<style scoped>
#user-url{
  border-radius: 9px;
  border-style: solid;
  border-color: #21262d;
  border-width: 1.4px;
  width: 25rem;
  height: 2rem;
  padding: 10px;
  font-size: 20px;
}

.button, input[type="submit"], input[type="reset"] {
	background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
	cursor: pointer;
	outline: inherit;
}

#go-btn{ 
  margin-left: 30px;
}

.advancedButton{ 
  position: absolute; 
  bottom: 30px; 
  right: 0;
  margin-right: 30px;
}

#darkButton { 
  position: absolute;
  top: 60px;
  right: 0;
  margin-top: 30px;
  margin-right: 20px;
}

label{
  margin-left: 9px;
}
</style>
