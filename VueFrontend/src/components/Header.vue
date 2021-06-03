<template>
    <div>
        <nav id="navBar" class="navbar navbar-expand-lg">
            <div class="container-fluid">
                <a class="navbar-brand nav-link" href="#"><router-link to="/">Simple Wiki</router-link></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> 
                    <span class="navbar-toggler-icon"></span> 
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
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

})
</script>

<style scoped>
.navbar-brand{ 
    cursor: default;
}
a { 
    color: #6c757d;
}

</style>