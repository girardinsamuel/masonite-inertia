# Validation

## Sharing errors/success messages

In order for your server-side validation errors to be available client-side, Masonite adapter shares flash messages **automatically.** You can find more information in [Shared data ](shared-data.md#flash-messages)section.

## Sharing form validation errors

TODO for M4

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

