# Django - Blog

A [Django](https://pypi.org/project/Django/) project that creates a blogging site.

## How to use it
### Environment startup
1. Clone the repository to your file system
2. At the directory level of the cloned project, create `.env` to hold any 
    environment variables you want in your container
3. Open your [Docker](https://www.docker.com/products/docker-desktop/) desktop application
4. Open up your shell of choice (ex. fish, bash, powershell...)
5. At the directory level of the cloned project, run `docker compose up --build`
### Django startup
Simply apply the migrations:

    $ python manage.py migrate
    

Now run the development server:

    $ python manage.py runserver

## Taking it to the next level
1. Apply GitHub actions to auto-format files
2. Visually spruce up the Django blog
3. Make a separate repository using the [Meltano](https://hub.docker.com/r/meltano/meltano) base image to pipe 
    data from project .sqlite database to Postgres database

## Resources
- [awesome-django](https://github.com/wsvincent/awesome-django)