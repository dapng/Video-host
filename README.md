# Vido-host
##### Backend project
###### Realised:

+ Registration and authorization
+ Uploading and viewing videos
+ Following and unfollowing
+ Follower list and my following
+ Likes in video
###### Created using:
+ Python 3.8
+ FastApi, Google-auth, Ormar, Pydantic, SQLAlchemy, Starlette.
+ Server: Uvicorn
+ DataBase: SQLite

## Installation

You need to install [Python](https://www.python.org/downloads/) v3.8+ to run.
Download the project and open it in the development environment.

Install.

```sh
pip install requirements.txt
```

Starting the server.

```sh
uvicorn main:app --reload
```

# Project screenshots
##### Swagger
![](https://i.postimg.cc/s2C5tbF6/1055.png)
#### Auth
![](https://i.postimg.cc/JzkbYMFH/1054.png)
> The user's token can be obtained in auth,
> using the developer tools in the browser
> To log in, you must specify the 
> data of your Google account
> Authorization of access to the address: Localhost
> The user's token is used in Postman

#### Uploading a video
![](https://i.postimg.cc/LskjRv2H/1057.png)

#### Subscribe to a user
![](https://i.postimg.cc/V6YnNMkX/1056.png)


#### Viewing subscriptions
![](https://i.postimg.cc/65SrhyMN/1053.png)

#### Viewing videos in the browser
![](https://i.postimg.cc/m2kLsS77/1059.png)


## License
**Free Software**
