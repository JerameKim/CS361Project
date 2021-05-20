<template>
    <div>
        <h2>Abstract</h2>
        <i class="fas fa-clipboard-list fa-2x" v-if="this.rendered" v-clipboard:copy="this.abstract" @click="showCopy"></i>
        <i class="fas fa-download fa-2x" @click="download(); showDownload()" v-if="this.rendered" ></i>
        <p>{{this.abstract}}</p>
    </div>
</template>

<script>

export default({
    props: [
        'wikiTag'
    ],
    data() { 
        return{ 
            url: "http://backendcs361.herokuapp.com/abstract/",
            abstract: "",
            rendered: false
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
                this.abstract = data
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
