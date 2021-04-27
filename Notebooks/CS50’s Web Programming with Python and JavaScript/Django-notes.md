# Django

**HTTP***is widely-accepted internet protocol for how messages are tranfered back and forth over the internet*

HTTP works dynamically in this way: the client/user sends a request to the sever then it interpects the request to display data in a different way, that request might look like something like this;

```py
GET / HTTP/1.1
Host: www.exmaple.com
...
```
After recieving a request, a sever will then send back a response. Such a response will include the HTTP version, a status code (200 means OK), a description of the content, and then some additional information.

![status code](https://cs50.harvard.edu/web/2020/notes/3/images/codes.png)

```Django``` is a web framework, it's a set of tools that is already built for us that's just going to make it easy to started by writing Python code in order to design fully fedge web applications.

To install:

```pip3 install Django```

To create a project:

```django-admin startproject PROJECT_NAME```

Start the project by running ```python3 manage.py runserver```

Django is totally different from other frameworks. Essentially django let's you create apps within the same project directory in order to sync the workflow.

This done by going into your terminal and runing the command: ```python3 manage.py startapp APP_NAME``` 

