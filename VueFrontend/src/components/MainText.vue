<template>
    <div class="mainTextContainer">
        <h2>Main Text</h2>
        <button>
            <i class="fas fa-clipboard-list fa-2x" v-if="this.rendered" v-clipboard:copy="this.finalText" @click="showCopy"></i>
        </button>
        <button>
            <i class="fas fa-download fa-2x" v-if="this.rendered" @click="download(); showDownload()"></i>
        </button>
        <p>{{this.mainText}}</p>
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
            url: "http://backendcs361.herokuapp.com/text/",
            mainText: "",
            formatText: [],
            finalText: "",
            noData: false,
            rendered: false,
        }
    },
    mounted(){
        this.getData()
    },

    methods: { 

        showCopy(){ 
            this.$toast("Copied Text!", {
                timeout: 2000
            });
        },

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
            // const fullUrl = this.url + this.wikiTag
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                this.formatText = data
                if(this.formatText.length == 0){ 
                    this.noData = true;
                }
                this.modifyData()
                this.rendered = true
            })
        },
        download(){ 
            var element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.finalText));
            element.setAttribute('download', 'MainText.txt');

            element.style.display = 'none'; 
            document.body.appendChild(element);

            element.click();

            document.body.removeChild(element);
        },
        showDownload(){ 
            console.log("Download")
            this.$toast.success("Your download should start shortly",{
                timeout: 2000
            })
        }
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
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
</style>