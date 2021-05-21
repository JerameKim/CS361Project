<template>
    <div>
        <h2>Abstract</h2>
        <button>
        <i class="fas fa-clipboard-list fa-2x" v-if="this.rendered" v-clipboard:copy="this.abstract" @click="showCopy"></i>
        </button>
        <button>
        <i class="fas fa-download fa-2x" @click="download(); showDownload()" v-if="this.rendered" ></i>
        </button>
        <p>{{this.abstract}}</p>
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
            rendered: false
        }
    },
    mounted(){
        this.getData()
    },
    methods: { 
        getData(){ 
            // const fullUrl = this.url + this.wikiTag
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            console.log(fullUrl)
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
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
</style>