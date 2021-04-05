<h1 align="center">Milestone Project 3 - Home Cooking</h1>

[View project here](https://home-cooking-milestone3-proj.herokuapp.com/)

This interactive site is based around individuals who would like a place to keep their recipes all 
in one place as well as share it with the rest of the world. Being able to create new recipes, 
edit and delete recipes on demand from the computers to their mobile phones. They would have the chance to write 
down the ingredients needed and the steps required to make the specific dish. 
If any issues arise, they would have the chance to reach out to the site administrator by sending them an email. 

This site would be utilizing Python which was taught from the Code Institute as well as using MongoDB. 
I will be using various technologies as well such as HTML5, CSS3, JQuery and Materialize. 
This project will be responsive and accessible to different size browsers and devices.

<h2 align="center"><img src="#">

## User Experience (UX)

### The Audience

The intended audience for this project is all individuals, from students who are about to leave home for the first time to go 
to universities and want to write down Mums cooking, all way to individuals who like to experiment in the kitchen but need a 
place to remember what they have done.  

### User Objectives

To have a place to store customised recipes and for them to be accessed anywhere from any device. The user would be able to 
register to begin the journey of adding a recipe to their account. From there, they would be able to log in and create their recipe. 
They would be able to add the ingredients and steps taken to make their dish once saved. The user would have the option to edit, 
delete and even share their recipes because by default all recipes would be set to private. 

The user would be able to edit their recipes and if they are logged into their account. Users who do not have an account but can 
see shared recipes, will not be able to edit or amend recipes. If the user is trying to look for something, there would be search 
functionality for them to be able to search by ingredient or by the name of the dish. Once all is achieved, the user can log out. 
If the user is trying to look for something, there would be search functionality for them to be able to search by ingredient or 
by the name of the dish. Once all is achieved, the user can log out. 

### My Objectives

My objectives are going to be achieved by taking images from free image stock websites that would have images of recipes, meals and 
kitchen crockery that I want to advertise. The recipes and ingredients would be taken from other websites to use as the data being 
pulled from the database. The users would be able to contact the site admin if they have any queries or questions as it would 
incorporate a contact form that would be linked to a live email address. The site would have a registration form and a login/logout 
functionality to allow users to have their profiles. It would also have validation included with error messages if 
the username or password is wrong.

The site would have a CRUD software architectural style (Create, Read, Update and Delete) for basic operations of persistent storage 
with the recipes being added by the users. Validation would also be in this part of the site as only the recipe owner would be able 
to edit and share the specific recipe.

The navigation bar and footer would be built within the base file and the content for the rest of the site would be built within 
their specific .html files. Within the footer, there would be social media links which would connect the user to the sites alternative 
social platforms.

## User Stories

The intended type of users for which this site would be focused towards are individuals who would like to store their 
homemade recipes online

1. As a user, I want to be able to register to the website so I can have an account.
1. As a user, I want to be able to login to the website so I start creating recipes.
1. As a user, I want an error message to appear if I typed my username/password incorrectly so I can attempt again with the correct username/password.
1. As a user, I want to be able to create and save a recipe and categories so I can start building a list of meals.
1. As a user, I want to be able to add my recipes to pre-created and newly-created categories.
1. As a user, I want to be able to update the saved recipe so I can change what has been saved.
1. As a user,  I want to be able to delete a saved recipe so I can remove it from the list of saved recipes.
1. As a user, I want to share my recipes with users who have not logged in so I can share my favourite recipes with other site visitors.
1. As a user, I want to be to send an email to the site admin so I can contact them if I have any issues.
1. As a user, I want to be able to logout from the website so I can go on other websites.

## Design

-   #### Colour Scheme
    -   The colour scheme I will be working with is mainly white but with a touch of greasy of-white/cream colour 
    to portray cooking and grease as well as it is most commonly used for baking. The text colour will be black to keep 
    the text easy to read (Will be using WebAIM to check the contrast of the colour scheme).

-   #### Typography
    -   I have chosen to use [Merriweather](https://fonts.google.com/specimen/Merriweather) and [Heebo](https://fonts.google.com/specimen/Heebo) 
    font as the main fonts throughout the website with Sans Serif as the emergency font in the case for any reason 
    the font is not being imported into the site correctly. Both [Merriweather](https://fonts.google.com/specimen/Merriweather)
    and [Heebo](https://fonts.google.com/specimen/Heebo) are attractive fonts to use as it easy to clear and easy to read, they are also has a touch formality 
    without being formal.

-   #### Imagery
    -   The images that were used are based on the content of what it is portraying. Displaying ingredients, finished 
    meals and kitchen crockery without diverting them for the task they need to complete. 

*   ### Wireframes

    #### Home Page
    - Home Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-web-browser.png)
    - Home Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-tablet.png)    
    - Home Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-mobile.png)

    #### Login Page
    - Login Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-web-browser.png)
    - Login Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-tablet.png)    
    - Login Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-mobile.png)

    #### Register Page
    - Register Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-web-browser.png)
    - Register Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-tablet.png)    
    - Register Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-mobile.png)

    #### Home Login Page
    - Home Login Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-web-browser.png)
    - Home Login Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-tablet.png)    
    - Home Login Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-mobile.png)

    #### New Meal Page
    - New Meal Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-web-browser.png)
    - New Meal Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-tablet.png)    
    - New Meal Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/new-meal-page-mobile.png)

    #### Profile Page
    - Profile Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-web-browser.png)
    - Profile Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-tablet.png)    
    - Profile Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/profile-page-mobile.png)

    #### Admin Page
    - Admin Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-web-browser.png)
    - Admin Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-tablet.png)    
    - Admin Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/admin-page-mobile.png)

    #### Contact Us Page
    - Contact Us Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-web-browser.png)
    - Contact Us Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-tablet.png)    
    - Contact Us Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/contact-us-page-mobile.png)

    Master Wireframe
    - Master Wireframe - [View](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/homemade-recipes.bmpr)
    
## Features

The features that will be utilised in this project will be as follows:



### Existing Features



## Technologies Used

###  Programming Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 was used to structure and present content on my website.
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 was used to provide my website with style.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - JavaScript was used to make the site interactive.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python was used as the backend language to access and parse data.

### Databases, Frameworks, Libraries, Programs and Templates Used

#### Databases
1. [Mongodb:](https://www.mongodb.com/)
    - Database which stores the data to be recalled onto the website.

#### Frameworks
1. [Materialize:](https://materializecss.com/)
    - Responsive front-end framework to assist with the responsiveness and styling of the website.
1. [JQuery Core 3.6.0:](https://code.jquery.com/)
    - JQuery library was implemented to use features within Materialize

#### Library
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome 5.13.3:](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

#### Programs
1. [Grammerly:](https://app.grammarly.com/)
    - Online tool which assists with the English grammar.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the code of the project after being pushed from GitPod.
1. [GitPod:](https://www.gitpod.io/)
    - A cloud development environment that allows us to create the website.
1. [Google Chrome:](https://www.google.co.uk/intl/en_uk/chrome/)
    - Default browser used to visually display the build process as well as utilising Chrome Dev Tools to assist where needed.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](#) during the design process.
1. [RandomKeygen:](https://randomkeygen.com/)
    - A tool to randomly generate a password.
1. [Heroku:](https://www.heroku.com)
    - A platform as a service (PaaS) that enables me to deploy my website in the cloud.

#### Templates

1. [Github Code Institute Template:](https://github.com/Code-Institute-Org/gitpod-full-template)
    - A template provided by the Code Institute which has the preinstalled tools that will get us started.

## Testing



### Validation



#### Results



### Further Testing

#### User Stories Testing from User Experience (UX) Section - [View Results](#)



#### Functionality and Usability Testing - [View Results](#)



#### Browser and Responsive Testing



### Known Issues



## Deployment



### Making a Clone



## Credits

### Content



### Code



### Media



### Acknowledgements

