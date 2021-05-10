<template>
    <div id="content">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
    <h3>Your tag is {{tag}}</h3>
        <div class="row">
            <div id="row1col1" class="col-sm-8">
                <!-- Send the content/tag tag to abstractView so that abstract can be loaded -->
                <abstractView :wikiTag= "tag" ></abstractView>
            </div>
            <div id="row1col2" class="col-sm">
                <mainText :wikiTag = "tag"></mainText>
            </div>
        </div>
        <div class="row">
            <div id="row2col1" class="col-sm">
                <photosView :wikiTag = "tag"></photosView>
            </div>
            
            <div id="row2col2" class="col-sm">
                <citationsView :wikiTag = "tag"></citationsView>
            </div>

            <div id="row2col3" class="col-sm">
                <categoriesView :wikiTag = "tag"></categoriesView>
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
    props: ['tag'],
    // data() { 
    //     return {
    //         tag: this.$route.params.tag
    //     }
    // },
    // watch: { 
    //     // Whenever $route is changed, execute code
    //     '$route'(to, from){ 
    //         this.id = to.params.id;
    //     }
    // },

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
    background-color: #dbdbdb;
    border-radius: 4px;
    padding: 4px 8px;
    display: inline-block;
}
.col-sm {
    border-style: solid;
    border-color: #95a5a6;
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

</style>


