const mix = require("laravel-mix");
const path = require("path");

mix
  .js("resources/js/inertia_demo.js", "storage/compiled/js")
  .vue({ version: 3 })

mix.alias({
  "@": path.resolve("resources/js"),
});