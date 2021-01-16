# Validation

### Sharing errors/success messages

In order for your server-side validation errors to be available client-side, Masonite adapter shares flash messages **automatically** through an `errors` prop and a  `success` prop.

It means that when you flash a message in session in your controller, the message will be available client-side \(in your e.g. Vue.js component\).

```python
self.request.session.flash("success", "User created.")
self.request.session.flash("errors", "An error occured.")
```

With the Vue adapter you would then access the messages with

```javascript
$page.props.success  // == "User created."
$page.props.errors  // == "An error occured."
```

You can disable flash messages automatic sharing in [inertia configuration](../advanced/configuration.md) by setting  `INCLUDE_FLASH_MESSAGES` to `False`.

### Sharing form validation errors

{% hint style="warning" %}
Unlike Laravel adapter, here you must \(for now\) add form validation errors manually in session. Hopefully it exists handy helpers for that in Masonite.
{% endhint %}

For example you would do in your controller

```javascript
errors = self.request.validate(
    validate.required(["name", "email"]),
    validate.length(["name", "email"], max=50),
    validate.email("email")
)
if errors:
    return self.request.redirect_to("users.create")
        .with_errors(errors) // add errors to session
        .with_input()
return self.request.redirect_to("users").with_success("User created!")
```

