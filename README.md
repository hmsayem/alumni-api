# Alumni REST API Server 
A REST API server built with Django REST framework for the Alumni of Bangladesh University of Professionals that allows its' users to:

- [x] Register & Login
- [x] Create/Update/Delete profile
- [x] Update settings
- [x] Create/Update/Delete/Like/Unlike blog posts

[![Python](https://img.shields.io/badge/Python-3.8-critical)]()
[![Django](https://img.shields.io/badge/Django-3.1-green)]()
[![Django](https://img.shields.io/badge/DRF-3.12-yellowgreen)]()

### How to set up
##### Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
git clone https://github.com/hmsayem/alumni-api.git && cd alumni-api
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

### API Reference

#### Register
```http

POST /api/account/register/

```
Request Body:
```json
{
    "first_name": "Hossain",
    "last_name": "Mahmud",
    "username": "hmsayem",
    "email": "hmsayem@gmail.com",
    "password": "changeit"
}

```
#### Login
```http

POST /api/account/login/

```
Request Body:
```json
{
    "username": "hmsayem",
    "password": "changeit"
}
```
> Login reqeust returns a token and an expiry as a json response. The token should be set as the authorization header. 

#### Get all users
```http

GET /api/account/user/

```
#### Get user
```http

GET /api/account/user/${user_id}/

```
#### Update user
```http

PUT /api/account/user/${user_id}/

```
Request Body:
```json
{
    "username": "sayem",
    "email": "sayem@gmail.com"
}
```
> This request will update the username and email of the specified user. Server will deny the request if the specified user is not same as the logged in user.

##### Get profiles of all users
```http

GET /api/account/profile/

```
##### Create profile for a user
```http

POST /api/account/profile/

```
Request Body:
```json
{
    "about": "Passionate about implementing new projects",
    "faculty": "FST",
    "department": "ICT",
    "roll": 17511058,
    "batch": 2017,
    "passing_year": 2021
}
```
> This request will create the above profile for the logged in user.

##### Get profile of a user
```http

GET /api/account/profile/${user_id}/

```
##### Update profile of a user
```http

PUT /api/account/profile/${user_id}/

```
Request Body:
```json
{
    "roll": 17511060,
    "batch": 2018
}
```
> This request will update the roll and batch of the specified user. Server will deny the request if the specified user is not same as the logged in user.

##### Delete profile of a user
```http

DELETE /api/account/profile/${user_id}/

```
> Server will deny the request if the specified user is not same as the logged in user.

##### Get job descriptions of all users
```http

GET /api/account/job/

```
##### Create job description for a user
```http

POST /api/account/job/

```
Request Body:
```json
{
    "title": "Software Engineer",
    "company": "AppsCode Inc.",
    "start_date": "2021-03-01"
}
```
> This request will create the above job description for the logged in user.
##### Get job description of a user
```http

GET /api/account/job/${user_id}/

```
##### Update job description of a user
```http

PUT /api/account/job/${user_id}/

```
Request Body:
```json
{
    "start_date": "2021-04-01"
}
```
> This request will update the start_date of the specified user. Server will deny the request if the specified user is not same as the logged in user.

##### Delete job description of a user
```http

DELETE /api/account/job/${user_id}/

```
> Server will deny the request if the specified user is not same as the logged in user.

##### Get Social links of all users
```http

GET /api/account/social/

```

##### Create Social links for a user
```http

POST /api/account/social/

```
Request Body:
```json
{    
    "facebook": "https://www.facebook.com/hm.sayem",
    "linkedin": "https://www.linkedin.com/in/hmsayem",
    "github": "https://github.com/hmsayem"
}
```
> This request will create the above social links for the logged in user.


##### Get Social links of a user
```http

GET /api/account/social/${user_id}/

```
##### Update Social links of a user
```http

PUT /api/account/social/${user_id}/

```
Request Body:
```json
{
    "facebook": "https://www.facebook.com/sayem",
    "linkedin": "https://www.linkedin.com/in/sayem",
}
```
> This request will update the facebook and linked in links of the specified user. Server will deny the request if the specified user is not same as the logged in user.

##### Delete Social links of a user
```http

DELETE /api/account/social/${user_id}/

```
> Server will deny the request if the specified user is not same as the logged in user.

##### Get all blog posts
```http

GET /api/blog/post/

```
##### Create blog post
```http

POST /api/blog/post/

```
Request Body:
```json
{
    "title": "Blog Post 1",
    "body": "<p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using<strong> Lorem Ipsum</strong> is that it has a more-or-less normal distribution of letters, as opposed to using &#39;Content here, content here&#39;, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for &#39;lorem ipsum&#39; will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>",
    "category": "Dynamic Programming"
}
```
> This request will create the above blog post. Server will set the logged in user as the author of this blog post.
##### Get blog post
```http

GET /api/blog/post/${blog_id}/

```
##### Update blog post
```http

PUT /api/blog/post/${blog_id}/

```
Request Body:
```json
{
    "title": "Blog Post 2"
}
```
> This request will update the title of the specified blog post. Server will deny the request if the author of the blog post is not same as the logged in user.
##### Delete blog post
```http

DELETE /api/blog/post/${blog_id}/

```
> Server will deny the request if the author of the blog post is not same as the logged in user.

##### Like/Unlike blog post
```http

PUT /api/blog/like/${blog_id}/

```
> This request will add a like to the specified blog post. If the post is already liked by the logged in user, the request will remove the like from it. 
