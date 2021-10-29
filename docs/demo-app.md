---
description: >-
  You can play with the online legacy demo or scaffold a simple demo directly
  into your project !
---

# Demo app

## Official Ping CRM demo

There is an official demo called `PingCRM` to demonstrate Inertia.js capabilities with Laravel framework.

You can now see this demo with MasoniteFramework here [https://pingcrm-masonite.herokuapp.com/](https://pingcrm-masonite.herokuapp.com/)

You can browse the code to understand how to use this package here

[https://github.com/girardinsamuel/pingcrm-masonite](https://github.com/girardinsamuel/pingcrm-masonite)

## Scaffold a demo into your project

You can also quickly scaffold a demo page into your project to start playing with Inertia.js easily.

{% hint style="warning" %}
You need to have [installed](./#installation) the package first. Also it's advised you commit/stash all your changes first because some \(minor\) modifications will be made to your project.
{% endhint %}

```text
python craft inertia:demo
```

This will automatically :

* publish a demo controller
* publish two routes in `routes/web.py`
* create a demo view in `templates/inertia.html`
* update npm packages and `webpack.mix.js`
* add Vue 3 demo app in `resources/js`

Then update your npm dependencies and compile the app

```text
npm install
npm run watch
```

Finally run your server

```text
python craft serve
```

And open the demo at [http://localhost:8000/inertia](http://localhost:8000/inertia) 🚀 !

