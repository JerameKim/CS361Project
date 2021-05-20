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
            mainText: "",
            formatText: [],
            finalText: "",
        }
    },
    mounted(){
        this.getData()
    },

    methods: { 
        // removes whitespace lines
        modifyData(){ 
            for(var i =0; i < this.formatText.length; i++){
                if(this.formatText[i] == "\n"){
                    continue; 
                }
                this.finalText = this.mainText

                this.mainText = this.finalText + this.formatText[i] 

                // console.log(this.formatText[i])
            }
        },

        getData(){ 
            const fullUrl = this.url + this.wikiTag
            console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                // this.mainText = data
                this.formatText = data
                this.modifyData()
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
p{
    white-space: pre-line;
}
</style>