## Introduction ##

I've developed a restaurant table reservation website. Users can view the menu for lunch and dinner. They can book reservations for a specific date and time, ensuring they can't select past dates. Only future and current dates are selectable. Additionally, users can delete and edit their reservations.

## User Personas ##

A family wants to spent time together with delicious food.
A person wants to go with his firends for dinner or lunch. 

## User Stories ##

* I have designed the user stories outlined in my [GitHub project](https://github.com/users/meena-rathi/projects/2).
* I followed the agile methodology to implement my project using GitHub Projects.
* Each user story has its own acceptance criteria.

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

These are wire frames of my website.

![ogIn](documentation/wireframe/Signin.png)

![SignUp](documentation/wireframe/signup.png)

![Home](documentation/wireframe/Home.png)

![menu](documentation/wireframe/menu.png)

![Reservation](documentation/wireframe/reservation.png)

![Edit Reservation](documentation/wireframe/Editreservation.png)

![View Reservation](documentation/wireframe/Viewreservation.png)

### Entity Relational Diagram

I have designed the ERD Diagram on th excel sheet.

![Erd](documentation/entity/entity-diagram.JPG)


## Fonts ##

The 'Lato' font family, a sans-serif typeface, has been selected for use across the resturtant project. 

Font Colors: The color scheme for text is primarily brown, gray and white.

## Screenshots of Finished Website ##

These are full website on screenshots.

![signup](/documentation/fullwebisteimages//signup.JPG)
![login](/documentation/fullwebisteimages/login.JPG)
![signout](/documentation/fullwebisteimages/Signout.JPG)
![home](/documentation/fullwebisteimages/home1.JPG)
![menu](/documentation/fullwebisteimages/menu.JPG)
![reservation](/documentation/fullwebisteimages/reservation.JPG)
![view reservation](/documentation/fullwebisteimages/viewreservation.JPG)
![Edit reservation](/documentation/fullwebisteimages/editreservation.JPG)
![detele reservation](/documentation/fullwebisteimages/deletealert.JPG)


## Features ##

When a user signed In, a message must be displayed.

For reservation and viewing reservations, signing in is mandatory.

![signin](/documentation/feature/signinmessage.JPG)

The navigation bar is active and highlights the current page you are on, making navigation easier.

The navigation bar is responsive, making it convenient for visitors using smaller screens.

![navbar](/documentation/feature/navigation.JPG)

The footer contain the adress and social icon.

![footer](/documentation/feature/footer.JPG)

The menu page has three tabs: Lunch, Dinner, and Drinks. Lunch menu is ative when page reload. When a user clicks on the Lunch tab, they see the lunch menu. Clicking on the Dinner tab shows the dinner menu, and clicking on the Drinks tab displays the drinks menu.

![menu](/documentation/feature/menu.JPG)

when user crete the resertion if the emil is lredy exir it must show error thsi lredy exit.
when user enter new emil is sve dt in dtbse reditert to view resetion.

![reservation](/documentation/feature/createreservation.JPG)

When a user creates a reservation, if the email already exists, it should display an error message indicating that it already exists. If the user enters a new email, the data is saved in the database and redirected to view the reservation.

![view reservation](/documentation/feature/viewreservation.JPG)

After successfully creating the reservation, the user can edit or delete the reservation here.

![delete reservation](/documentation/feature/deletealert.JPG)

When a user clicks on the delete button, a pop-up alert appears asking, "Are you sure you want to delete?"

![delete reservation](/documentation/feature/deletemessage.JPG)

When the reservation is successfully deleted, a message appears confirming the deletion.

![Edit reservation](/documentation/feature/editresertionmessage.JPG)

When a user edits the form, if something goes wrong, a message must be displayed.

![Edit reservation](/documentation/feature/editreservation.JPG)

When a user edits the form, if something goes wrong, a error must displayed. if not the form edit successfully.

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

## Testing

### Validation

Python was validated using [PEP8 CI python linter](https://pep8ci.herokuapp.com/), with no errors or warnings.

CSS was validated using [jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input), with no errors or warnings.

HTML was validated using [W3C Validator](https://validator.w3.org/#validate_by_uri), with no errors or warnings.

### Manual Testing

#### Navbar

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | redirect to the Home Page| MR icon cliked | Home page | Pass |
| Menu Tabs | redirected to particular paged cliked on the tab | Clicked on th tabs | Page opened as per clicked tab | Pass |

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

#### Edit Reservation

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| logged User| Edit the Reservation from view Reservation page | Logged User | Edit Reservation | Pass |
| Edit  | All filed contain the valid Data | Edit | No error Data updated | Pass |
| Edit  | If any filed is not valid | Edit |  error Data has not been updated | Pass |

## Fixed Bugs ##

1. When user made the reservtion the reservation page is not redirecting.
2. Fixed the email validation.
3. Fixed Edit date validation.
4. Fixed contact number validation.


## Credits ##

1. https://stackoverflow.com/questions/31548373/django-1-8-django-crispy-forms-is-there-a-simple-easy-way-of-implementing-a
2. https://pixabay.com/ 
3.  To deisgn Menu (https://www.google.com/search?q=how+to+design+menu+card+for+restaurant+bootstrap+5+code&sca_esv=60b997825705a04a&rlz=1C1CHBD_enPK955PK955&biw=1366&bih=607&sxsrf=ACQVn09aseLtTNtj54HsY9BRUGUIJjSdmA%3A1712300129767&ei=YaAPZvqnLr-Txc8PgZicsAg&oq=how+to+design+menu+card+for+restaurant+bootstrap+5+co&gs_lp=Egxnd3Mtd2l6LXNlcnAiNWhvdyB0byBkZXNpZ24gbWVudSBjYXJkIGZvciByZXN0YXVyYW50IGJvb3RzdHJhcCA1IGNvKgIIATIFECEYoAEyBRAhGKABMgQQIRgVSKYfULkKWOoRcAF4AZABAJgBhwGgAbkCqgEDMi4xuAEDyAEA-AEBmAIEoALKAsICChAAGEcY1gQYsAOYAwCIBgGQBgaSBwMzLjGgB84Q&sclient=gws-wiz-serp#fpstate=ive&vld=cid:c092b7c7,vid:KRENd1sv3tE,st:0)
4. [I think therefore I blog](https://github.com/Code-Institute-Solutions/blog)
5. https://stackoverflow.com/questions/23956288/django-all-auth-email-required
6. https://docs.djangoproject.com/en/4.2/topics/http/urls/