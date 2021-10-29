# File uploads

### Example

Coming soon.

### Limitations

Uploading files using a `multipart/form-data` request is not natively supported in some languages for the `put`, `patch` or `delete` methods. The workaround here is to simply upload files using `post` instead.

Masonite support form method spoofing, which allows you to upload the files using `post`, but have the framework handle the request as a `put` or `patch` request. This is done by including a `__method` attribute in the data of your request. [https://docs.masoniteproject.com/the-basics/requests#changing-request-methods-in-forms-and-urls](https://docs.masoniteproject.com/the-basics/requests#changing-request-methods-in-forms-and-urls).

With inertia.js it can be done this way ([from official doc](https://inertiajs.com/file-uploads)).

```
Inertia.post(`/users/${user.id}`, {
  _method: 'put',
  avatar: form.avatar,
})
```
