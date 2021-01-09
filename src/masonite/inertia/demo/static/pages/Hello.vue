<template>
  <div>
    <h1>Hello {{ first_name }}</h1>
    <p>You just navigated with Inertia.js 🚀 !</p>
    <inertia-link href="/inertia">&lt; Go back</inertia-link>
  </div>
</template>

<script>
export default {
  name: "HEllo",
  props: {
    first_name: String,
  },
};
</script>
