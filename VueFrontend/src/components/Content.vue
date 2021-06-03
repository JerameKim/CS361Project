<template>
    <div>
        <appHeader></appHeader>
        <div id="content">
            <link
                rel="stylesheet"
                href="https://use.fontawesome.com/releases/v5.12.1/css/all.css"
                crossorigin="anonymous"
            />
            <div class="row">
                <div v-if="this.showAbstract" id="row1col1" class="col-sm-4">
                    <!-- Send the content/tag tag to abstractView so that abstract can be loaded -->
                    <abstractView :wikiTag="tag" :lang="lang"></abstractView>
                </div>
                <div v-if="this.showMain" id="row1col2" class="col-sm">
                    <mainText :wikiTag="tag" :lang="lang"></mainText>
                </div>
            </div>
            <div class="row">
                <div v-if="!this.showPhotos" id="row2col1" class="col-sm">
                    <photosView :wikiTag="tag" :lang="lang"></photosView>
                </div>
                 <div v-if="this.showChapters" id="row2col3" class="col-sm">
                    <chaptersView :wikiTag="tag" :lang="lang"></chaptersView>
                </div>
                <div v-if="this.showCitations" id="row2col2" class="col-sm">
                    <citationsView :wikiTag="tag" :lang="lang"></citationsView>
                </div>

                <div v-if="this.showCategories" id="row2col3" class="col-sm">
                    <categoriesView
                        :wikiTag="tag"
                        :lang="lang"
                    ></categoriesView>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Abstract from "./subSections/Abstract";
import MainTextView from "./subSections/MainText";
import CitationsView from "./subSections/Citations";
import CategoriesView from "./subSections/Categories";
import PhotosView from "./subSections/Photos";
import ChaptersView from "./subSections/Chapters";
import Header from "./Header";

export default {
    name: "Content",
    props: ["lang", "tag", "showData"],
    data() { 
        return { 
            showAbstract: false, 
            showChapters: false, 
            showMain: false, 
            showCategories: false, 
            showPhotos: false, 
            showCitations: false, 
        }
    },
    components: {
        abstractView: Abstract,
        mainText: MainTextView,
        citationsView: CitationsView,
        categoriesView: CategoriesView,
        photosView: PhotosView,
        chaptersView: ChaptersView,
        appHeader: Header,
    },
    created(){ 
        // this.showData comes in as a six digit string of numbers
        var firstChar = this.showData[0];
        var secondChar = this.showData[1];
        var thirdChar = this.showData[2];
        var fourthChar = this.showData[3];
        var fifthChar = this.showData[4];
        var sixthChar = this.showData[5];
        if(firstChar == 1){ 
            this.showAbstract = true;
        }
        if(secondChar == 1){ 
            this.showCategories = true; 
        }
        if(thirdChar == 1){ 
            this.showChapters = true;
        }
        if(fourthChar == 1){ 
            this.showMain = true;
        }
        if(fifthChar == 1){
            this.showPhotos = true;
        }
        if(sixthChar == 1){ 
            this.showCitations = true;
        }

        console.log("DATA IS " + this.showData);
    },

    methods: { 
        printTest(input, input1, input2){ 
            console.log(input, input1, input2);
            console.log("This input");
        }
    },
};
</script>

<style>
h2 {
    background-color: #eae5e5;
    border-radius: 4px;
    padding: 4px 8px;
    display: inline-block;
}
.col-sm {
    border-style: solid;
    border-color: #cccece;
    border-radius: 6px;
    padding: 10px;
    margin: 6px;
}
.row {
    margin-top: 10px;
    padding-left: 30px;
    padding-right: 30px;
    text-align: left;
}
#row1col1 {
    margin-top: 16px;
    border-style: none;
}
.fas {
    padding-left: 10px;
}
#content {
    padding: 0px 30px;
}
</style>


