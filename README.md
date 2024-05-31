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

### Manual Testing

#### Navbar

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Site link <https://meena-rathi.github.io/quiz_javascript/>| redirect to the Home Page| MR icon cliked | Home page | Pass |
| All N | Questions page appears | Clicked on the start button |  Question is displayed | Pass |
| Player name Text Field | Error message for disallowed spaces| Clicked on the start button  |Spaces are not allowed | Pass |
| Player name Text Field |  Player name is required| Clicked on the start button |Player Name is required| Pass |
| Start | 	Questions appear on screen | Clicked start button | Questions dislpay | Pass |


#### Footer

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Facebook link in navigation| Leads to correct site and opens in a new tab| Clicked on Facebook link|  Facebook page open |Pass |
| Instagram link in navigation | Leads to correct site and opens in a new tab | Clicked on Instagram link | Instagram open  | Pass |
| Twitter link in navigation | Leads to correct site and opens in a new tab | Clicked on Twitter link |Twitter open | Pass |

#### Home Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Menu button| Leads to correct menu page| Clicked on Menu button |  Menu page open |Pass |
| Reservation button|Leads to correct Reservation page | Clicked on Reservation button | Reservation page open |Pass |

#### Menu Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Lunch button| Lunch menu open| Clicked on lunch button | lunch Menu  open |Pass |
| Dinner button| Dinner menu open| Clicked on Dinner button | Dinner menu open |Pass |
| Drink button| Drink menu open| Clicked on Drink button | Drink Menu open |Pass |

#### Reservation Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Sign In| Reservation must be open after login the page | After sign In | Reservation open |Pass |
| Email | Email vaild | Enter email | The email is correct | Pass |
| Email | Email not vaild | Enter email | The email is not correct | Pass |
| Email | Email already registered | Enter email | This email is already registered | Pass |
| Contact Number | The Enter contact Number is valid | Enter contact number | The contact number is correct | Pass |
| Contact Number | The Enter contact Number is not valid | Enter contact number | The contact number is not correct | Pass |
| Date | Only select the current or future date | Select Date | Only select the current or future date | Pass |
| Date | Past Dates not selected | Select Date | user can't select the past Date | Pass |
| reservation Button | All fileds enter valid data | Submit reservation | View reservation page open | Pass |

#### View Reservation

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logged User| View the reservation | Logged User | View Reservation | Pass |

#### Delete Reservation

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logged User| Delete the Reservation from view Reservation page | Logged User | Delete Reservation | Pass |

#### Delete Reservation

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| logged User| Edit the Reservation from view Reservation page | Logged User | Edit Reservation | Pass |
| Edit  | All filed contain the valid Data | Edit | No error Data updated | Pass |
| Edit  | If any filed is not valid | Edit |  error Data has not been updated | Pass |

