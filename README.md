# RESTFUL API for BUP Alumni Website
### About
A website for the alumnus of Bangladesh University of Professionals (BUP).

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
##### Migrate & Collect Static
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
> Authentication
```
"/api/account/register/" [User Registration]
"/api/account/login" [Login] 
```
> Profile
```
"/api/account/profile/" [Displays profile list] [POST to create] 
"/api/account/profile/<user_id>/" [Displays a specific profile] [PUT to update, DELETE to delete]
```
> Blog
```
"/api/blog/post/" [Displays blog list] [POST to create] 
"/api/blog/post/<blog_id>/" [Displays a specific blog] [PUT to update, DELETE to delete]
"/api/blog/comment/<blog_id>" [Displays comment list of a specific blog] 
"/api/blog/comment/create" [POST to create comment]

```