<template>
    <div>
        <h2>Abstract</h2>
        <i class="fas fa-clipboard-list fa-2x" v-clipboard:copy="this.abstract" @click="showCopy"></i>
        <i class="fas fa-download fa-2x" @click="download()"></i>
        <!-- <h3><strong>Abstract tag is {{wikiTag}}</strong></h3> -->
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
            abstract: ""
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
            })
        },

        showCopy(){ 
            this.$toast.success("Copy Success");
        },
        download(){ 
            console.log("Download")
            var element = document.createElement('a');
            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.abstract));
            element.setAttribute('download', 'File.txt');

            element.style.display = 'none'; 
            document.body.appendChild(element);

            element.click();

            document.body.removeChild(element);
        }

        
        // printTag(){ 
        //     console.log("Your tag: ")
        //     console.log(this.wikiTag)
        // },
    }
})
</script>
