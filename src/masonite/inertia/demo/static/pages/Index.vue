<template>
  <img alt="Vue logo" src="https://v3.vuejs.org/logo.png" />
  <h1>{{ msg }}</h1>
  <inertia-link href="/inertia-hello">Open link</inertia-link>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      msg: "Hello Masonite, Vue 3.0 and Inertia !"
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>