<template>
    <div class="mainTextContainer">
        <h2>Photos</h2>
        <button>
            Download Links
            <i class="fas fa-download fa-2x" @click="download(); showDownload()" v-if="this.rendered"></i>
        </button>
        <ul>
            <li v-for="(photo, photoIdx) in photos" v-bind:key="photoIdx">
                <div class="inner">
                    <img :src=photo.src :alt=photo.caption download>
                    <br>
                    <a :href=photo.src v-if="photo.id == 1">Title Photo</a>
                    <a :href= photo.src v-else>{{photo.caption}}</a>
                    <hr>
                </div>
            </li>
        </ul>
        <h4 id="noData" v-if="this.noData">
            There is no available citation data
        </h4>
        <b-spinner v-if="!this.rendered" id="loadingSpinner" label="Spinning"></b-spinner>
    </div>
</template>

<script>

export default({
    props: [
        'lang', 
        'wikiTag'
    ],
    data() { 
        return{ 
            url: "http://backendcs361.herokuapp.com/photos/",
            photos: [],
            rendered: false,
            noData: false,
        }
    },
    mounted(){
        this.getData()
    },
    methods: { 
        getData(){ 
            // const fullUrl = this.url + this.wikiTag
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            //console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                this.photos = data
                if(this.photos.length == 0){ 
                    this.noData = true;
                }
                this.rendered = true
            })
        },
        showDownload(){ 
            this.$toast.success("Downloading image sources",{
                timeout: 2000
            })
        },
        download(){ 
            console.log("Download Started")
            var sourcesString = '';
            var element = document.createElement('a');

            // put all img sources into a sources string
            for(var i = 0; i < this.photos.length; i ++){ 
                // console.log(this.photos[i].src);
                sourcesString += this.photos[i].src 
                sourcesString += "\n"
                // console.log("Current source: " + this.photos[i].src)
                // console.log("All sources:" + sourcesString)

            }
            // console.log("ALL sources: " + sourcesString)
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(sourcesString));
            element.setAttribute('download', 'ImageSources.txt');
            element.style.display = 'none'; 
            document.body.appendChild(element);
            element.click();
            document.body.removeChild(element);
        }
    }
})
</script>

<style scoped>
.mainTextContainer{ 
    height: 400px;
    overflow: auto;
}
.inner{
    align-content: center;
    padding-top: 10px;
}
ul{
    list-style-type: none;
    padding-left: 8px; 
    margin: 0;
}
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
</style>