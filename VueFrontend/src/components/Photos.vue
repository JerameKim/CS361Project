<template>
    <div class="mainTextContainer">
        <h2>Photos</h2>
        <i class="fas fa-download fa-2x"></i>
        <ul>
            <li v-for="(photo, photoIdx) in photos" v-bind:key="photoIdx">
                <div class="inner">
                    <a :href=photo.src v-if="photo.id == 1">Title Photo</a>
                    <a :href= photo.src v-else>{{photo.caption}}</a>
                    <br>
                    <img :src=photo.src :alt=photo.caption>
                    <hr>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>

export default({
    props: [
        'wikiTag'
    ],
    data() { 
        return{ 
            url: "http://backendcs361.herokuapp.com/photos/",
            photos: [],
        }
    },
    mounted(){
        this.getData()
    },
    methods: { 
        getData(){ 
            const fullUrl = this.url + this.wikiTag
            console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                this.photos = data
            })
        },
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
}
ul{
    list-style-type: none;
    padding-left: 8px; 
    margin: 0;
}
/* li{
    list-style: none;
}; */
</style>