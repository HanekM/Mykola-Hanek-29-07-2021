This is the test task for message-app
=======

Here I provide Postman collection to download and import to your local Postman:

https://drive.google.com/file/d/1QHsBzvDvvdP2qdaiVjy1t_8RTjubX0vh/view?usp=sharing

In Postman collection, you can see the list of all endpoints and the examples how to use them.

I've implemented a bonus task with auth using JWT auth system, so that it is necessary to get an access token before getting into it.
```
{
    "email": "admin@gmail.com",
    "password": "admin"
}
```

You can also log in as an admin at https://message-app-01.herokuapp.com/admin/ to see all test users avaivable. You are able to choose any existing user as a sender or a receiver, just remember that only the receivers are able to see messages sent to them. 
