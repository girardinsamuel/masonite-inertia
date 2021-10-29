<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl text-center mb-10">Hello World {{ first_name }}</h1>
    <inertia-link href="/inertia" as="button" class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Go back</inertia-link>
  </div>
</template>

<script>
import Layout from "@/Layout"

export default {
  name: "HelloWorld",
  layout: Layout,
  props: {
    first_name: String,
  },
};
</script>
