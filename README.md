## Project: Event Management System
### Project Description:
An Event Management System where users can create, manage, and join events.

### For run docker-compose:
🏃‍♂️ Run the project
It's now time to run the project.

First of all, let's run the database.
docker-compose up -d db

🏗️ Build the Django app
Now that the database is running let's build the Django app.
docker compose build

🏃‍♂️ Run the Django app
Now that the image is built, let's run the Django app.
docker compose up