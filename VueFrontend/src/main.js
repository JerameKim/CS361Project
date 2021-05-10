import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import VueRouter from 'vue-router'; 
import VueResource from 'vue-resource';
import { routes }from './routes.js'; 
import {BootstrapVue } from 'bootstrap-vue'; 
import './styles/app.scss'

Vue.use(VueResource);
Vue.use(BootstrapVue)
Vue.use(VueRouter); 



const router = new VueRouter({
  routes
});


new Vue({
  el: '#app', 
  router,
  render: h => h(App),
}).$mount('#app')
