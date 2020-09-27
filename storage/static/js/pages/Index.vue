<template>
  <div>
    <h1>Hello {{ user }}</h1>
    <p>Lazy: {{ lazy }}</p>
    <p>ERRORS: {{ $page.messages.error }}</p>
    <!-- <inertia-link href="/helloworld"> -->
    <inertia-link :href="route('helloworld')">
      Go to Hello World
    </inertia-link>
    <input type="text" placeholder="preserved state data" v-model="preserved" />
    <input type="text" placeholder="not preserved state data" v-model="lazy" />
    <!-- <inertia-link href="/" preserve-state> -->
    <inertia-link href="/" :only="['user']">
      Refresh
    </inertia-link>
    <inertia-link href="/error" method="post" preserve-state>
      Post
    </inertia-link>
  </div>
</template>

<script>
export default {
  name: "Index",
  props: {
    user: {
      type: String,
      default: "",
    },
    lazy: {
      type: String,
      default: 0,
    },
  },
  data() {
    return {
      preserved: this.user,
      not_preserved: "",
    };
  },
};
</script>
