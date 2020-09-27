import Vue from "vue";
import { InertiaApp } from "@inertiajs/inertia-vue";
import route from "ziggy-js";
// import { Ziggy } from "./ziggy";

Vue.mixin({
  methods: {
    route: (name, params, absolute) =>
      route(name, params, absolute, window.Ziggy),
  },
});

Vue.use(InertiaApp);

const app = document.getElementById("app");

// Vue.prototype.$route = (...args) => route(...args).url();

new Vue({
  render: (h) =>
    h(InertiaApp, {
      props: {
        initialPage: JSON.parse(app.dataset.page),
        resolveComponent: (name) => require(`./pages/${name}`).default,
      },
    }),
}).$mount(app);
