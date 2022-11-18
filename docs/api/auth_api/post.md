# Login

A login is the authentication system used in order to get the authentication token. Without token, you can't access to private data. That help you to protect your application.

POST /login
---

This endpoint gives you an authorization through an authentication token given the user and password.

**Arguments**

* `user`: The user to authenticate. **Required**
* `password`: The password to authenticate. **Required**

**Example Request**

```bash
GET https://desafioplaneta.com/api/login/?api_key={YOUR API KEY}
```

**Example Response**

[response_get_game.json](responses/response_post_login.json)