## Introduction ##


## User Personas ##

A family wants to spent time together with delicious food.
A person wants to go with his firends for dinner or lunch. 

## User Stories ##
I have designed the user stories outlined in my [GitHub project](https://github.com/users/meena-rathi/projects/2).
I followed the agile methodology to implement my project using GitHub Projects.
Each user story has its own acceptance criteria.

The user storys in my GitHub project are as follows:

* As a site user, I can easily create an account to access the website.
* As a site user, I can make a reservation for a table on the current date or future dates so that I have a reservation.
* As a site user, I can see my reservation.
* As a site user, I can edit or delete my reservation.
* As a site admin, I can create, delete, and update reservations.

## User Goals ##

New User: 

- I can navigate the website without any hassle.
- The website provides enough information for me to understand what the restaurant is about.
- The sign-up process is easy and straightforward.

Pervious user:

- Signing in is easy.
- I can view and manage my bookings easily.

## Website Owner Goals

- Allow users to view, modify, and manage their bookings effortlessly.
- Send timely confirmations and date.
- Design an intuitive layout for easy access to menu.
- Ensure the sign-up process is simple, with minimal steps and clear instructions.

## Design

### Wireframes

### Entity Relational Diagram

![Erd](documentation/entity_relational_diagram/erd.png)


## Fonts ##
The 'Lato' font family, a sans-serif typeface, has been selected for use across the resturtant project. Font Colors: The color scheme for text is primarily brown, gray and white.

## Screenshots of Finished Website ##

![signup](/documentation/images/signup.JPG)

![home](/documentation/images/home1.JPG)
![Dinner](/documentation/images/dinner.JPG)
![Lunch](/documentation/images/lunchmenu.JPG)
![Drink](/documentation/images/drink.JPG)
![home](/documentation/images/home1.JPG)

## Features ##

The navigation bar is active and highlights the current page you are on, making navigation easier.

The navigation bar is responsive, making it convenient for visitors using smaller screens.


## Deployment

- Set up a PostgreSQL server on ElephantSQL.
- Adjusted the settings file to use the ElephantSQL database.
- Set up cloudinary.
- Stored the SECRET_KEY and DATABASE_URL in an env.py file, and added env.py to .gitignore.
- Installed Gunicorn (version 20.1) and added it to requirements.txt.
- Created a Procfile to declare the web process and command to run the project.
- Added a runtime.txt file with the supported Python version, close to the version used in development.
- Set DEBUG to False in the settings file.
- Added Heroku to the ALLOWED_HOSTS in the settings file (with .herokuapp).
- Pushed the code to GitHub.
- Created a new app on Heroku.
- In the app's settings tab, clicked "Reveal Config Vars" and added DATABASE_URL (from ElephantSQL) and SECRET_KEY.
- Connected the Heroku app to the GitHub repository via the deploy tab.
- Clicked "Deploy Branch" to deploy the project.

Here is a link to my Deployed project: [reseturtant reservation](https://resturtantbooking-f16cfcc27fc2.herokuapp.com/)

## Languages and Frameworks

This project was created using Django 4.2.1 and Bootstrap 5.3.
The additional libraries used can be found in the requirements.txt file.
CSS
