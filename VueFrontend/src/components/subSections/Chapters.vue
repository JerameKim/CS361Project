<template>
    <div class="mainTextContainer">
        <h2>Chapters</h2>
        <button>
            <i class="fas fa-download fa-2x" @click="download(); showDownload()" v-if="this.rendered" ></i>
        </button>
		<ul v-if="!this.noData">
            <li v-for="(chapter, chapterIdx) in chaptersArray" v-bind:key="chapterIdx">
                <a :href=chapter.link>{{chapter.text}}</a>
            </li>
        </ul>
        <h4 id="noData" v-if="this.noData">
            There is no available chapters data
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
            url: "http://backendcs361.herokuapp.com/chapters/",
			chaptersArray: [],
            chapters: "",
            noData: false,
            rendered: false,
			lines: [],
        }
    },
    mounted(){
        this.getData()
    },
    methods: { 
		parseData() { 
			// creates with array of strings that are "citation, \nlink\n\n"
            for(var i = 0; i < this.chaptersArray.length; i ++){ 
                var line = this.chaptersArray[i].text + ", \n" + this.chaptersArray[i].link + "\n\n"
                this.lines.push(line)
            }
		},
        getData(){ 
            const fullUrl = this.url + this.lang + "/" + this.wikiTag
            console.log(fullUrl)
            fetch(fullUrl).then(response=> response.json())
            .then(data=> {
                this.chaptersArray = data
                if(this.chaptersArray.length == 0){ 
                    this.noData = true;
                }
                this.rendered = true
				this.parseData();
            })
        },

        download(){ 
            var finalString = '';
            var element = document.createElement('a');

            // put all img sources into a sources string
            for(var i = 0; i < this.lines.length; i ++){ 
                finalString += this.lines[i] 
            }

            element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(finalString));
            element.setAttribute('download', 'Chapters.txt');
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
ul { 
	padding-top: 20px; 
	list-style: circle;
}
.mainTextContainer{ 
    height: 400px;
    overflow: auto;
}
</style>