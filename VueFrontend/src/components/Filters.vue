<template>
    <div class="mainCointainer">
        <br>
        <h2>What would you like to see?</h2>
        <i class="fas fa-download fa-2x"></i>
        <div class="row">
            <div class="col-sm">
                <h4>Subsections</h4>

                <input type="checkbox" id="abstract" value="abstract">
                <label for="abstract"> Abstract </label><br>
                <input type="checkbox" id="tables" value="tables">
                <label for="abstract"> Tables </label><br>
                <input type="checkbox" id="mainText" value="mainText">
                <label for="abstract"> Main text</label><br>
                <input type="checkbox" id="photos" value="photos">
                <label for="abstract"> Photos </label><br>
                <input type="checkbox" id="citations" value="citations">
                <label for="abstract"> Citations </label><br>
            </div>
            <div class="col-sm">
                <h4>Language Display</h4>
                <h6>This is where I will use teammate's microservice to translate the article and its subsections into another language</h6>
                    <select name="langs" id="lngs">
                        <option value="en">English</option>
                        <option value="sp">Spanish</option>
                        <option value="gm">German</option>
                        <option value="fr">French</option>
                    </select>
            </div>
        </div>
    </div>
</template>

<style scoped>
.col-sm{
    border-style: solid;
    border-color: #95a5a6;
    border-radius: 6px;
    padding: 10px;
    margin: 6px;
}
</style>