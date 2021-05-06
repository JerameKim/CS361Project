<template>
    <div id="content">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
        <div class="row">
            <div id="row1col1" class="col-sm-8">
                <h2>Abstract</h2>
                <i class="fas fa-clipboard-list fa-2x"></i>
                <i class="fas fa-download fa-2x"></i>
                <placeholder></placeholder>
            </div>
            <div id="row1col2" class="col-sm">
                <h2>Main Text</h2>
                <i class="fas fa-clipboard-list fa-2x"></i>
                <i class="fas fa-download fa-2x"></i>
                <placeholder></placeholder>
            </div>
        </div>
        <div class="row">
            <div id="row2col1" class="col-sm">
                <h2>Photos</h2>
                <i class="fas fa-download fa-2x"></i>
                <placeholder></placeholder>
            </div>
            <div id="row2col2" class="col-sm">
                <h2>Citations</h2>
                <i class="fas fa-clipboard-list fa-2x"></i>
                <i class="fas fa-download fa-2x"></i>
                <placeholder></placeholder>
            </div>
            <div id="row2col3" class="col-sm">
                <h2>Data Tables</h2>
                <i class="fas fa-download fa-2x"></i>
                <placeholder></placeholder>
            </div>
        </div>
    </div>
</template>

<script>
import Abstract from "./Abstract";

export default {
    name: "Content",
    components: {
        placeholder: Abstract,
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


