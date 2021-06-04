<template>
    <div class = "mainTextContainer">
        <h2>Abstract</h2>
        <button>
            <i class="fas fa-clipboard fa-2x" v-if="this.rendered" v-clipboard:copy="this.abstract" @click="showCopy"></i>
        </button>
        <button>
            <i class="fas fa-download fa-2x" @click="download(); showDownload()" v-if="this.rendered" ></i>
        </button>
        <p>{{this.abstract}}</p>
        <hr>
    <!-- <b-dropdown id="dropdown-1" text="Translate Abstract" class="m-md-2">
        <b-dropdown-item @click="translateLang(es)">Spanish</b-dropdown-item>
        <b-dropdown-item @click="translateLang(fr)">French</b-dropdown-item>
        <b-dropdown-item @click="translateLang(ru)">Russian</b-dropdown-item>
        <b-dropdown-item @click="translateLang(it)">Italian</b-dropdown-item>
        <b-dropdown-item @click="translateLang(ko)">Korean</b-dropdown-item>
        <b-dropdown-item @click="translateLang(zh)">Chinese</b-dropdown-item>
        <b-dropdown-item @click="translateLang(ja)">Japanese</b-dropdown-item>
    </b-dropdown> -->
        <p>{{this.translatedText}}</p>
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
            // url: "http://backendcs361.herokuapp.com/abstract/es/",
            url: "http://backendcs361.herokuapp.com/abstract/",
            abstract: "",
            noData: false,
            rendered: false,
            es: "es", 
            fr: "fr", 
            ru: "ru", 
            it: "it", 
            ko: "ko", 
            zh: "zh", 
            ja: "ja",
            translatedText: "",
        }
    },
    mounted(){
        this.getData()
    },
    methods: {
        translateLang(inputLang) { 
            console.log(inputLang);
            const requestOptions = { 
                method: "POST", 
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ Text: this.abstract})
            }; 
            var frontURL = "https://translation-microservice.azurewebsites.net?toLanguageCode="
            var languageCode = inputLang
            var finalURL = frontURL + languageCode
            fetch(finalURL, requestOptions)
            .then(response=>response.text())
            .then(data=>{ 
                this.translatedText = data
                if(this.translatedText.length == 0){
                    this.noData = true; 
                }
                this.rendered = true;
            })
        },
        getData(){ 
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            fetch(fullUrl).then(response=> response.json())
            .then(data=> {
                this.abstract = data
                if(this.abstract.length == 0){ 
                    this.noData = true;
                }
                this.rendered = true
            })
        },

        showCopy(){ 
            this.$toast("Copied Text!", {
                timeout: 2000
            });
        },
        download(){ 
            var element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.abstract));
            element.setAttribute('download', 'Abstract.txt');

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

button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
</style>