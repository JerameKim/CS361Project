<template>
    <div>
        <nav v-if="darkMode" id="navBarLight" class="navbar navbar-expand-lg bg-light">
            <div class="container-fluid">
                <a class="navbar-brand nav-link" href="#"><router-link to="/">Simple Wiki</router-link></a>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> 
                    <span class="navbar-toggler-icon"></span> 
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link" href="#" ><router-link to="/content" class="text-secondary">Content</router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#" ><router-link to="/api" class="text-secondary">API</router-link></a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <nav v-if="!darkMode" id="navBarDark" class="navbar navbar-expand-lg bg-dark">
            <div class="container-fluid">
                <a id="barTitle" class="navbar-brand nav-link" href="#" ><router-link to="/">Simple Wiki</router-link></a>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <!-- <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">
                                <router-link to="/" class="text-secondary">Home</router-link></a>
                        </li> -->
                        <li class="nav-item">
                            <a class="nav-link" href="#" ><router-link to="/content" class="text-secondary">Content</router-link></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#" ><router-link to="/api" class="text-secondary">API</router-link></a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>

export default ({
    props: [
        'darkMode'
    ],
})
</script>

<style scoped>
.navbar-brand{ 
    cursor: default;
}
#navBarDark{ 
    color: white;
}
a { 
    color: black
}
</style>