<template>
    <div id="content">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
        <div class="row">
            <div id="row1col1" class="col-sm-4">
                <!-- Send the content/tag tag to abstractView so that abstract can be loaded -->
                <abstractView :wikiTag = "tag" :lang = "lang"></abstractView>
            </div>
            <div id="row1col2" class="col-sm">
                <mainText :wikiTag = "tag" :lang = "lang"></mainText>
            </div>
        </div>
        <div class="row">
            <div id="row2col1" class="col-sm">
                <photosView :wikiTag = "tag" :lang = "lang"></photosView>
            </div>
            
            <div id="row2col2" class="col-sm">
                <citationsView :wikiTag = "tag" :lang = "lang"></citationsView>
            </div>

            <div id="row2col3" class="col-sm">
                <categoriesView :wikiTag = "tag" :lang = "lang"></categoriesView>
            </div>
        </div>
    </div>
</template>

<script>
import Abstract from "./Abstract";
import MainTextView from "./MainText";
import CitationsView from "./Citations";
import CategoriesView from "./Categories";
import PhotosView from "./Photos";


export default {
    name: "Content",
    props: [
        'lang', 
        'tag'
    ],

    components: {
        abstractView: Abstract,
        mainText: MainTextView,
        citationsView: CitationsView,
        categoriesView: CategoriesView,
        photosView: PhotosView
    },
};
</script>

<style>
h2 {
    background-color: #EAE5E5;
    border-radius: 4px;
    padding: 4px 8px;
    display: inline-block;
}
.col-sm {
    border-style: solid;
    border-color: #cccece ;
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
#row1col1{
    margin-top: 16px;
    border-style: none; 
}
.fas{ 
    padding-left: 10px;
}
#content{ 
    padding: 0px 30px;
}

</style>


