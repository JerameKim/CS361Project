import Content from './components/Content.vue';
import Home from './components/Home.vue';
import ApiCalls from './components/Api.vue';
// import AbstractVue from './components/Abstract.vue';

export const routes = [
    { path: '', component:  Home},

    // children: routes inside content
    { path: '/content/:tag', component: Content, props: true},
    // { path: '/content', component: Content, children: [
    //     { path: 'abstract', component: AbstractVue},
    //     { path: 'api', component: ApiCalls},
    // ]},
    
    { path: '/api', component: ApiCalls},
]
