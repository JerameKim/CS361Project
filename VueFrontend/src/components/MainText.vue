<template>
    <div class="mainTextContainer">
        <h2>Main Text</h2>
        <i class="fas fa-clipboard-list fa-2x"></i>
        <i class="fas fa-download fa-2x"></i>
        <p>{{this.mainText}}</p>
    </div>
</template>

<script>

export default({
    props: [
        'wikiTag'
    ],
    data() { 
        return{ 
            url: "http://backendcs361.herokuapp.com/text/",
            mainText: ""
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
                this.mainText = data
            })
        },

        // printTag(){ 
        //     console.log("Your tag: ")
        //     console.log(this.wikiTag)
        // },
    }
})
</script>

<style scoped>
.mainTextContainer{ 
    height: 400px;
    overflow: auto;
}
</style>