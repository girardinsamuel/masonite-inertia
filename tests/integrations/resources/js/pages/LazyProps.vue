<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl text-center mb-10">Lazy Props</h1>

    <ul>
      <li>Basic prop : {{ basic }}</li>
      <li>Callable prop : {{ callable }}</li>
      <li>Lazy prop : {{ lazy_prop }}</li>
    </ul>

    <div class="flex items-center space-x-2 mt-10">
      <inertia-link href="/inertia/lazy-props" :only="['lazy_prop']" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Refresh with only (lazy_prop)
      </inertia-link>
      <inertia-link href="/inertia" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Go back</inertia-link>
    </div>

  </div>
</template>

<script>
import Layout from "@/Layout"

export default {
  name: "LazyProps",
  layout: Layout,
  props: {
    basic: String,
    callable: Number,
    lazy_prop: Number,
  },
};
</script>
