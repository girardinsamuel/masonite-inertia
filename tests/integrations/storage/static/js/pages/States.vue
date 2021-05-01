<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl text-center mb-10">States</h1>
    <input type="text" placeholder="preserved state data" v-model="preserved" />
    <input type="text" placeholder="not preserved state data" v-model="name" />

    <inertia-link href="/inertia/states" preserve-state as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Reload</inertia-link>
    <inertia-link href="/inertia/states" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Reload (without preserving)</inertia-link>

    <inertia-link href="/inertia" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Go back</inertia-link>
  </div>
</template>

<script>
import Layout from "@/Layout"

export default {
  name: "States",
  layout: Layout,
  props: {
    name: String,
  },
  data () {
    return {
      preserved: "",
      name: this.name
    }
  }
}
</script>
