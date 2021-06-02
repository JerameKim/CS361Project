<template>
    <div>
        <appHeader :darkMode="true" v-if="!darkActive" ></appHeader>
        <appHeader :darkMode="false" v-if="darkActive" ></appHeader>
        <div id = "apiContent" v-if="!darkMode" class = "lightAPI">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
            <br>
            <h4 style="font-weight: bold"> How to use an API</h4>
            <a href="https://technologyadvice.com/blog/information-technology/how-to-use-an-api/">Introductory Article</a>
            <br>
            <a href="https://www.youtube.com/watch?v=GZvSYJDk-us"> Video Overview </a>
            <br>
            <hr>
            <h3 style="font-weight: bold">API Specific usage</h3>
            <p>Replace <strong>{tag}</strong> with the tag/keyword of the Wikipedia article.</p>
                <ul>
                    <li>In any regular Wikipedia url, the tag can be found as the text after the final "/"</li>
                    <li>For example, the tag for "https://en.wikipedia.org/wiki/Modern_family" would be <strong>Modern_family</strong></li>
                </ul>
            <p>Replace <strong>{lang}</strong> with the 2 character language code of the Wikipedia article.</p>
                <ul>
                    <li>In any regular Wikipedia url, the lang can be found as the first 2 chars after "https://"</li>
                    <li>For example, the tag for "https://en.wikipedia.org/wiki/Modern_family" would be <strong>en</strong></li>
                </ul>
            <hr>
            <ul class="list-group">
                <li class="list-group-item">
                    <h3>Article Abstract <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/abstract/{tag}'" @click="showCopy"></i>
                    </button>
                    
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/abstract/{lang}/{tag}</p>
                    <p>This endpoint fetches the first paragraph of any Wikipedia article.</p>
                    <p>Return data is raw text</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Citations <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/citations/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/citations/{lang}/{tag}</p>
                    <p>This endpoint fetches the citation text and links of any Wikipedia article.</p>
                    <p>Returned in JSON format with each object having a link, text and id attribute.</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/text/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/text/{lang}/{tag}</p>
                    <p>This endpoint fetches all the raw text in the article.</p>
                    <p>Return data is raw text</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/photos/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/photos/{lang}/{tag}</p>
                    <p>This endpoint fetches the photo source links and their captions.</p>
                    <p>Return data is JSON formatted with each object having a src, caption and id field</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                    <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/categories/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/categories/{lang}/{tag}</p>
                    <p>This endpoint fetches the categories and articles that are related to the current article.</p>
                    <p>Return data is JSON formatted with each object having a link, and text field that holds the article's title.</p>
                </li>
            </ul>
        </div>
        <div id = "apiContent" v-if="darkMode" class = "darkAPI">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
            <br>
            <h4 style="font-weight: bold"> How to use an API</h4>
            <a href="https://technologyadvice.com/blog/information-technology/how-to-use-an-api/">Introductory Article</a>
            <br>
            <a href="https://www.youtube.com/watch?v=GZvSYJDk-us"> Video Overview </a>
            <br>
            <hr>
            <h3 style="font-weight: bold">API Specific usage</h3>
            <p>Replace <strong>{tag}</strong> with the tag/keyword of the Wikipedia article.</p>
                <ul>
                    <li>In any regular Wikipedia url, the tag can be found as the text after the final "/"</li>
                    <li>For example, the tag for "https://en.wikipedia.org/wiki/Modern_family" would be <strong>Modern_family</strong></li>
                </ul>
            <p>Replace <strong>{lang}</strong> with the 2 character language code of the Wikipedia article.</p>
                <ul>
                    <li>In any regular Wikipedia url, the lang can be found as the first 2 chars after "https://"</li>
                    <li>For example, the tag for "https://en.wikipedia.org/wiki/Modern_family" would be <strong>en</strong></li>
                </ul>
            <hr>
            <ul class="list-group">
                <li class="list-group-item">
                    <h3>Article Abstract <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/abstract/{tag}'" @click="showCopy"></i>
                    </button>
                    
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/abstract/{lang}/{tag}</p>
                    <p>This endpoint fetches the first paragraph of any Wikipedia article.</p>
                    <p>Return data is raw text</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Citations <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/citations/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/citations/{lang}/{tag}</p>
                    <p>This endpoint fetches the citation text and links of any Wikipedia article.</p>
                    <p>Returned in JSON format with each object having a link, text and id attribute.</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/text/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/text/{lang}/{tag}</p>
                    <p>This endpoint fetches all the raw text in the article.</p>
                    <p>Return data is raw text</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                        <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/photos/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/photos/{lang}/{tag}</p>
                    <p>This endpoint fetches the photo source links and their captions.</p>
                    <p>Return data is JSON formatted with each object having a src, caption and id field</p>
                </li>
                <li class="list-group-item">
                    <h3>Article Text <span class="badge bg-success">GET</span>
                    <button>
                    <i title="Copy URL" class="fas fa-clipboard-list" v-clipboard:copy="'https://backendcs361.herokuapp.com/categories/{tag}'" @click="showCopy"></i>
                    </button>
                    </h3>
                    <p style="font-weight: bold">https://backendcs361.herokuapp.com/categories/{lang}/{tag}</p>
                    <p>This endpoint fetches the categories and articles that are related to the current article.</p>
                    <p>Return data is JSON formatted with each object having a link, and text field that holds the article's title.</p>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
import Header from "./Header"

export default ({
    props: [
        "darkMode"
    ],
    data() { 
        return { 
            active: false
        }
    },
    methods: { 
        showCopy(){ 
            this.$toast("Copied Text!", {
                timeout: 2000
            });
        },
    }, 
    components: { 
        appHeader: Header,
    }
})
</script>

<style scoped>
#apiContent{ 
    text-align: left;
    margin-left: 30px;
    margin-top: 10px;
}
.fas{ 
    padding: 10px;
}
button { 
    outline: none; 
    background: transparent; 
    border: 1px solid transparent
}
.darkAPI{ 
    background-color: black;
}
.lightAPI{ 
    background-color: black;
}
</style>

