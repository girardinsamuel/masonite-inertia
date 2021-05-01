import { createApp, h } from "vue"
import { app, plugin } from "@inertiajs/inertia-vue3"
import route from "ziggy-js"
import { Ziggy } from "./routes"

const el = document.getElementById("app");

const inertiaApp = createApp({
  render: () =>
    h(app, {
      initialPage: JSON.parse(el.dataset.page),
      resolveComponent: (name) =>
        require(`./pages/${name}`).default,
        // import(`@/pages/${name}`).then((module) => module.default),
    }),
})
  .use(plugin)
  .mixin({
    methods: {
      route: (name, params, absolute) => route(name, params, absolute, Ziggy),
    },
  })

inertiaApp.mount(el)