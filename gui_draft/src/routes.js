import Content from './components/Content.vue';
import Home from './components/Home.vue'

export const routes = [
    // whenever we visit this domain, load this component. 
    { path: '', component:  Home},
    { path: '/content', component: Content}
]