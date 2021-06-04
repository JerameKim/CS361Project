<template>
    <div class="mainTextContainer">
        <h2>Categories</h2>
        <button>
            <i class="fas fa-download fa-2x" v-if="this.rendered" @click="download(); showDownload()"></i>
        </button>
        <ul>
            <li v-for="(category, categoryIdx) in categories" v-bind:key="categoryIdx">
                <a :href=category.link>{{category.text}}</a>
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
            url: "http://backendcs361.herokuapp.com/categories/",
            categories: [],
            finalString: "",
            rendered: false,
            noData: false,
            lines: [],
        }
    },
    created(){
        this.getData()
    },
    methods: { 
        parseData(){ 
            // creates with array of strings that are "citation, \nlink\n\n"
            for(var i = 0; i < this.categories.length; i ++){ 
                var line = this.categories[i].text + ", \n" + this.categories[i].link + "\n\n"
                this.lines.push(line)
            }
        },
        getData(){ 
            // const fullUrl = this.url + this.wikiTag
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            //console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> { 
                this.categories = data
                if(this.categories.length == 0){
                    this.noData = true;
                }
                this.rendered = true
                this.parseData()
            })
        },
        download(){ 
            console.log("Download Started")
            var finalString = '';
            var element = document.createElement('a');

            // corectly does populatino
            for(var i = 0; i < this.lines.length; i ++){ 
                finalString += this.lines[i] 
            }

            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(finalString));
            element.setAttribute('download', 'Categories.txt');
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
ul{
    padding-top: 20px;
    list-style: circle;
}
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
</style>