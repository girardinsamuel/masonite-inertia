const mix = require("laravel-mix");
const path = require("path");
/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Masonite application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */
mix
  .js("tests/integrations/resources/js/app.js", "app.js")
  .vue({ version: 3 })
  .setPublicPath("tests/integrations/storage/compiled/js")
  .setResourceRoot("/static/")
  .webpackConfig(webpack => {
    return {
      output: { chunkFilename: "[name].js", publicPath: "/static/js/" },
    }
  })
  .alias({
    "@": path.resolve("tests/integrations/resources/js"),
  })
