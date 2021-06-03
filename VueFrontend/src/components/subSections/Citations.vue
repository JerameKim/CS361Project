<template>
    <div class="mainTextContainer">
        <h2>Citations</h2>
        <button v-if="!this.noData">
            <i class="fas fa-clipboard fa-2x" v-if="this.rendered" v-clipboard:copy="this.finalString" @click="showCopy();"></i>
        </button>
        <button v-if="!this.noData">
            <i class="fas fa-download fa-2x" v-if="this.rendered" @click="showDownload()"></i>
        </button>
        <ul v-if="!this.noData">
            <li v-for="(citation, citationIdx) in citations" v-bind:key="citationIdx">
                <p>{{citation.text}} (<a :href=citation.link>link</a>)</p>
                <hr>
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
            url: "http://backendcs361.herokuapp.com/citations/",
            citations: [],
            lines: [],
            finalString: "",
            noData: false,
            rendered: false,
        }
    },
    created(){
        this.getData()
    },
    methods: { 
        parseData(){ 
            // creates with array of strings that are "citation, \nlink\n\n"
            for(var i = 0; i < this.citations.length; i ++){ 
                var line = this.citations[i].text + ", \n" + this.citations[i].link + "\n\n"
                this.lines.push(line)
            }
        },

        getData(){ 
            // const fullUrl = this.url + this.wikiTag
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            //console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                this.citations = data
                if(this.citations[0].id == -3){
                    this.noData = true
                }
                this.rendered = true
                this.parseData()
            })
        },
        download(){ 
            var finalString = '';
            var element = document.createElement('a');

            // put all img sources into a sources string
            for(var i = 0; i < this.lines.length; i ++){ 
                finalString += this.lines[i] 
                // console.log("Current source: " + this.photos[i].src)
                // console.log("All sources:" + sourcesString)
            }
            // console.log("ALL sources: " + sourcesString)
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(finalString));
            element.setAttribute('download', 'Citations.txt');
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
            this.download()
        },
        showCopy(){ 
            this.$toast("Copied Text!", {
                timeout: 2000
            });
        }
    }
})
</script>

<style scoped>
.mainTextContainer{ 
    height: 400px;
    overflow: auto;
}
ul { 
    list-style: circle;
}
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}

</style>