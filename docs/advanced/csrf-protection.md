# CSRF protection

## CSRF Token

The adapter will include a `XSRF-TOKEN` cookie on each response with the value of Masonite generated CSRF Token. Client requests made with `axios` through inertia frontend adapters will include `X-XSRF-TOKEN` header.

Thanks to `VerifyCSRFToken` middleware, Masonite will verify the presence of the CSRF Token in the header allowing CSRF verification.

## Handling mismatches

Coming soon.
