import { createApp, h } from "vue";
import { app, plugin } from "@inertiajs/inertia-vue3";
import route from "ziggy-js";
import { Ziggy } from "./routes";

// Vue.mixin({
//   methods: {
//     route: (name, params, absolute) => route(name, params, absolute, Ziggy),
//   },
// });
// OR
// Vue.prototype.$route = (...args) => route(...args).url();

// Vue.use(InertiaApp);

const el = document.getElementById("app");

createApp({
  render: () =>
    h(app, {
      initialPage: JSON.parse(el.dataset.page),
      resolveComponent: (name) =>
        // require(`./pages/${name}`).default,
        import(`@/pages/${name}`).then((module) => module.default),
    }),
})
  .use(plugin)
  .mount(el);