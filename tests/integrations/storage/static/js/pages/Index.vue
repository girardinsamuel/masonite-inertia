<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl text-center mb-10">Welcome {{ user }} on Inertia/Masonite playground</h1>

    <div class="flex items-center space-x-2">
      <inertia-link href="/inertia/page-2" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Hello World
      </inertia-link>

      <inertia-link href="/inertia/lazy-props" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Lazy Props
      </inertia-link>

      <inertia-link href="/inertia/states" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        States
      </inertia-link>

      <inertia-link href="/inertia/external" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        External link (through Inertia)
      </inertia-link>

      <inertia-link href="/inertia/add-errors" as="button" method="post" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Submit form with errors
      </inertia-link>

      <a href="/inertia/other-root" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Other root
      </a>
    </div>
    <!-- <inertia-link href="/error" as="button" method="post" preserve-state>
      Post
    </inertia-link>-->
  </div>
</template>

<script>
import Layout from "@/Layout"

export default {
  name: "Index",
  layout: Layout,
  props: {
    user: {
      type: String,
      default: "",
    },
    // lazy: {
    //   type: String,
    //   default: 0,
    // },
  },
  // data() {
  //   return {
  //     preserved: this.user,
  //     not_preserved: "",
  //   }
  // },
}
</script>
