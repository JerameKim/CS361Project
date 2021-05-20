<template>
    <div class="mainTextContainer">
        <h2>Categories</h2>
        <i class="fas fa-download fa-2x"></i>

        <ul>
            <li v-for="(category, categoryIdx) in categories" v-bind:key="categoryIdx">
                <a :href=category.link>{{category.text}}</a>
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
            url: "http://backendcs361.herokuapp.com/categories/",
            categories: [],
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
                this.categories = data
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
ul{
    list-style: circle;
}
</style>