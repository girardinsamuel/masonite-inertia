<template>
  <div>
    <h1>Hello World {{ first_name }}</h1>
    <inertia-link href="/">< Go back</inertia-link>
    <p>Current route: {{ route().current() }}</p>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    first_name: String,
  },
};
</script>
