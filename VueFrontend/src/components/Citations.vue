<template>
    <div class="mainTextContainer">
        <h2>Citations</h2>
        <i class="fas fa-clipboard-list fa-2x"></i>
        <i class="fas fa-download fa-2x"></i>

        <ul>
            <li v-for="(citation, citationIdx) in citations" v-bind:key="citationIdx">
                <p>{{citation.text}} (<a :href=citation.link>link</a>)</p>
                <hr>
            </li>
        </ul>
    </div>
</template>

<script>

export default({
    props: [
        'wikiTag'
    ],
    data() { 
        return{ 
            url: "http://backendcs361.herokuapp.com/citations/",
            citations: [],
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
                this.citations = data
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
ul { 
    list-style: circle;
}
</style>