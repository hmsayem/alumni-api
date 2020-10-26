# RESTFUL API for BUP Alumni Website
### About
A website for the alumnus of Bangladesh University of Professionals (BUP).
[Click here](http://bup.pythonanywhere.com/) to view a live version of the website. <br> <br>
[![Python](https://img.shields.io/badge/Python-3.8-critical)]()
[![Django](https://img.shields.io/badge/Django-3.1-green)]()
[![Django](https://img.shields.io/badge/DRF-3.12-yellowgreen)]()

### Features

- Blog
- Batch and Faculty wise student database
- Personal profile for each Alumni
- Job Portal
- Career counselling sessions
- Mentoring


### How to set up
##### Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
git clone https://github.com/hmsayem/BUP-Alumni.git && cd BUP-Alumni
pip install -r requirements.txt
```
##### Migrate
```
python manage.py migrate
```
##### Create Admin User
```
python manage.py createsuperuser
```
##### Run Server
```
python manage.py runserver
```
>  The blog should be available at `localhost:8000`. You can login as an admin at `http://localhost:8000/admin`.

### API Endpoints
You can call any of the service URL directly from a client browser. It will return a JSON formatted results.
> #####Authentication
```
"/api/account/register/" 
```
`POST` Register.
```
"/api/account/login/" 
```
`POST` Login.

> #####Settings

```
"/api/account/user/"
```
`GET`  Returns Users. 
```
"/api/account/user/user_id"
```
`PUT` Update Settings. 

> #####Profile 

```
"/api/account/profile/"
```
`GET`  Returns Profiles. <br> 
`POST` Create Profile. 

```
"/api/account/profile/user_id/"
```
`GET`  Returns Profile.<br> 
`PUT` Update Profile.<br>
`DELETE` Delete Profile.

```
"/api/account/job/"
```
`GET`  Returns Job descriptions. <br> 
`POST` Add job description.

```
"/api/account/job/user_id/"
```
`GET`  Returns Job description.<br> 
`PUT` Update Job description. <br>
`DELETE` Delete Job description.
 
```
"/api/account/social/"
```
`POST` Add Social links.
```
"/api/account/social/user_id/"
```
`GET`  Returns Social links.<br> 
`PUT` Update Social links. <br>
`DELETE` Delete Social links.
 

> #####Blog
```
"/api/blog/post/"
```
`GET` Returns Blog Posts. <br>
`POST` Create Blog Post.
```
"/api/blog/post/blog_id/"
```
`GET` Returns Blog post. <br>
`PUT` Update Blog Post. <br>
`DELETE` Delete Blog Post.

```
"/api/blog/comment/blog_id/"
```
`GET` Returns comments.

```
"/api/blog/comment/create/"
```

`POST` Create Comment.

```
"/api/blog/like/blog_id"
```
`GET` Like / Unlike post.
