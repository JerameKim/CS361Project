<template>
    <div id="content">
        <div class="row">
            <div id = "row1col1" class="col-sm"><h2>Abstract</h2></div>
            <div id = "row1col2" class="col-sm"><h2>Main Text</h2></div>
            <div id = "row1col3" class="col-sm"><h2>Photos</h2></div>
        </div>
        <div class="row">
            <div id = "row2col1" class="col-sm"><h2>Section 1</h2></div>
            <div id = "row2col2" class="col-sm"></div>
            <div id = "row2col3" class="col-sm"><h2>Data Table</h2></div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Content",
};
</script>

<style >
h2{ 
    background-color: #DBDBDB;
    border-radius: 4px;
    padding: 4px 8px;
    display: inline-block;
}
.col-sm{ 
    border-style: solid; 
    border-color: #95a5a6; 
    border-radius: 6px;
    padding: 10px;
    margin: 6px;
    text-align: left;
}
.row{ 
    padding-left: 30px;
    padding-right: 30px;
}

</style>


