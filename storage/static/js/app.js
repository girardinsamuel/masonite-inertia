import Vue from "vue";
import { InertiaApp } from "@inertiajs/inertia-vue";
import route from "ziggy-js";
import { Ziggy } from "./routes";

Vue.mixin({
  methods: {
    route: (name, params, absolute) => route(name, params, absolute, Ziggy),
  },
});
// OR
// Vue.prototype.$route = (...args) => route(...args).url();

Vue.use(InertiaApp);

const app = document.getElementById("app");

new Vue({
  render: (h) =>
    h(InertiaApp, {
      props: {
        initialPage: JSON.parse(app.dataset.page),
        resolveComponent: (name) => require(`./pages/${name}`).default,
      },
    }),
}).$mount(app);
