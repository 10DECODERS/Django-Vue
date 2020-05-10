import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use({
    install (Vue) {
    Vue.prototype.$api = axios.create({
      baseURL: 'http://localhost:8000/'
    })
  }
})

Vue.config.productionTip = false


new Vue({
  render: h => h(App),
  router,
  components: { App }
}).$mount('#app')