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

<h2 align="center"><img src="documentation/images/responsive-homepage.png">

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
their specific .html files. Within the footer, there would be social media links that would connect the user to the sites alternative 
social platforms.

## User Stories

The intended type of users for which this site would be focused towards are individuals who would like to store their 
homemade recipes online

1. As a user, I want to be able to register to the website so I can have my own profile.
1. As a user, I want an error message to appear if I typed my username/password incorrectly so I can attempt again with the correct username/password.
1. As a registered user, I want to be able to edit my username and/or password so I can update my profile.
1. As a registered user, I want to be able to create and save a recipe so I view it whenever I want.
1. As a user, I want to be able to edit my recipes so I can amend them if I made a mistake.
1. As a registered user, I want to be able to share my recipe so I can allow other non registered users to see my meal
1. As a registered user,  I want to be able to delete a saved recipe so I can remove it from the list of saved recipes.
1. As a user, I want to be able to tell the difference between which recipes have been created by me vs recipes created by other users so I can know which ones I have shared.
1. As a user, I want to be to send an email to the site admin so I can contact them if I have any issues.
1. As a user, I want to be able to log out from the website so I can go on other websites.
1. As a user, I want to see an error page if I enter the wrong extension page within the URL so I know I am in the wrong location. 

## Design

-   #### Colour Scheme
    -   The colour scheme I will be working with is mainly white but with a touch of off-white/yellow colour to portray cooking and the light of food. The text colour will be black to keep the text easy to read (Will be using WebAIM to check the contrast of the colour scheme).

-   #### Typography
    -   I have chosen to use [Merriweather](https://fonts.google.com/specimen/Merriweather) and [Heebo](https://fonts.google.com/specimen/Heebo) 
    font as the main fonts throughout the website with Sans Serif as the emergency font in the case for any reason 
    the font is not being imported into the site correctly. Both [Merriweather](https://fonts.google.com/specimen/Merriweather)
    and [Heebo](https://fonts.google.com/specimen/Heebo) are attractive fonts to use as it easy to clear and easy to read, they are also has a touch formality 
    without being formal.

-   #### Imagery
    -   The images that were used are based on the content of what it is portraying. Displaying ingredients, finished 
    meals and kitchen crockery without diverting them for the task they need to complete. 

-   ### Wireframes

    #### Home Page
    - Home Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-web-browser.png)
    - Home Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-tablet.png)    
    - Home Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-page-mobile.png)

    I altered my design because representing the recipes looked better in cards than have accordian drop downs.

    #### Login Page
    - Login Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-web-browser.png)
    - Login Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-tablet.png)    
    - Login Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/login-page-mobile.png)

    #### Register Page
    - Register Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-web-browser.png)
    - Register Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-tablet.png)    
    - Register Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/registration-page-mobile.png)

    #### My Recipe Page
    - My Recipe Page Wireframe (Web Browser) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-web-browser.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-web-browser.png)
    - My Recipe Page Wireframe (Tablet) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-tablet.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-tablet.png)    
    - My Recipe Page Wireframe (Mobile) - [View PDF](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-mobile.pdf) | [View Image](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/wireframes/home-login-page-mobile.png)

    I altered my design because representing the recipes looked better in cards than have accordian drop downs.

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
    
More pages were created but were not accounted for in the beginning brief. I did however maintain the colour scheme and format throughout the site.

#### Database Mapping

The database was designed using an online tool called [DB Diagram](https://dbdiagram.io/). The tables where mapped depending on the field requirements.

Database Design - [Mapping](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/database/database-mapping.pdf)

## Features

The features that will be utilised in this project will be as follows:

### Existing Features

#### Site Features

- Responsive on devices sized 1024px, 768px, 425px, 375px and 320px.
- Allows the user to know the navigated hyperlinks, by having a hoover over feature within the hyperlinks.
- Navigation bar and footer pulled from the base file throughout all pages.

#### Home Page

- Shared recipes to be displayed at the bottom of the page.
- Only the registered owner of a recipe would be able to edit/delete a shared recipe.

#### Registration / Login

- Use to be added to the database when the user is registered.
- If passwords don't match within the registration page, an error message would appear.
- If the username or password don't match on the login page, an error message would and the user would not be able to log in.

#### Profile / Edit Username / Edit Password

- Once logged in, be directed to the the user recipe page.
- Once username or password has been changed, to be logged out and to log back in.
- When the password doesn't match on the change password page, the user would be unable to change the password.

#### My Recipe Page

- Search functionality to be able to search by the name of the recipe and/or by an ingredient.
- Reset button which resets the search and displays all recipes the user has created.
- If the recipe is labelled as Vegiterian, a V image would appear by the recipe name.
- User has the option to delete or edit the a recipe when selected.
- Page will display up to 6 recipes before a new page is created (Pagination)

#### Edit Page

- To recall the information related to that specific recipe.

#### Admin User / Meal Page

- Only admin user would be able to have the option to create, edit and delete a meal type.

#### Contact Modal

- A popup modal which would appear in the middle of the page.
- A confirmation alert box appears in the top of the screen when the message has successfully sent.

#### Error Pages

- If the page does not exist, a 404 error page would appear.
- The error 500 page will load when there is an internal server error.

### Features Left to Implement

- A confirm delete modal when the user deletes a recipe.
- For the admin user to be able to edit and delete recipes created by all users.
- When a user registers, an email verification to be sent to the user.
- To give the option for the user to click on forgotten password and n email to be sent them to be able to reset it for them.
- Specific filters on the 'My Recipe Page' so they can view just their favourite recipes, or if they want to have a drop-down to select their cuisine they want to see etc.

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
1. [DB Diagram](https://dbdiagram.io/)
    - Online tool to design the database.
1. [Mongodb:](https://www.mongodb.com/)
    - Database which stores the data to be recalled onto the website.

#### Frameworks
1. [Materialize 1.0.0:](https://materializecss.com/)
    - Responsive front-end framework to assist with the responsiveness and styling of the website.
1. [JQuery Core 3.6.0:](https://code.jquery.com/)
    - JQuery library was implemented to use features within Materialize
1. [EmailJS]()
    - Using emailJS service to send emails from the contact modal

#### Library
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome 5.13.3:](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Hover 5.15.3](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css)
    - Hover effects used for the animation on hovering over links and buttons.

#### Programs
1. [Grammerly:](https://app.grammarly.com/)
    - Online tool which assists with the English grammar.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the code of the project after being pushed from GitPod.
1. [GitPod:](https://www.gitpod.io/)
    - A cloud development environment that allows us to create the website.
1. [Visual Studio Code](https://code.visualstudio.com/)
    - Code editing software was used to replace GitPod as the free license expired due to over 50 hours useage. 
1. [GitHub Desktop:](https://desktop.github.com/)
    - A tool that allows you to interact with GitHub from the desktop
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

Testing was taken place during my build of the site. I was utilising Visual Studio Code  'Live Preview' to visually see what my website looks like with every change that is made. I was also utilising Chrome Dev Tools to assist with changes when code was not working as planned. Within Chrome Dev Tools, I was also utilising the responsive views to see the development for the responsive sizes. To test the JS that I was using, I would be using Chrome Dev Tools and choosing Console to make sure everything was running smoothly.

In this section, I would be testing the User Stories taken from the User Experience Section (UX), testing the functionality and usability, testing the responsive views as well as browser testing

### Validation

On code completion, i ensured my code was validated with no snytax errors. I used [W3C Markup Validator](https://validator.w3.org/) for HTML5, [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) for CSS3 to ensure my code is W3C Compliant. I used [JSHint](https://jshint.com/) to helps to detect errors and potential problems in your JavaScript code. I used (PEP8 Online)[http://pep8online.com/] to check if my code is PEP8 compliment.

#### Results

##### HTML

- Validating all the HTML files, the only standard HTML error I received that I did not add the "alt" attribute to the img element.
- On all HTML files, errors for the syntax is still there. Problem is that it doesn't read the Jinja2 library.

##### CSS

- Document was all pass once I fixed 2 classes either they were blank and had no styles associated with them and I put the wrong properties in the wrong class.

##### JS

- Everthing was passwed apart from one warning sign which is as expected as JSHint is using an old version of ES

##### Python

- Only needing to fix the line too long error, the python file passed without any further issues.

### Further Testing

#### User Stories Testing from User Experience (UX) Section - [View Results](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/testing-md-docs/user-testing-ux.md)

When carrying out the User Stories Testing, I placed my self as the user being provided instructions on how to achieve the goals that were identified. The intended type of users which this website is targeted for are individuals who looking for and/or looking to store recipes. I displayed screenshots with the results of each finding to provide evidence of the stories being achieved successfully.

#### Functionality and Usability Testing - [View Results](https://github.com/adnanmuhtadi/milestone-project-3/blob/master/documentation/testing-md-docs/features-function-testing.md)

Testing all my functions and features within the site and ensuring that it is usable across different browsers and devices. I laid the results out in a table with each section defining the feature/function, a description of what I am testing as well as if it passes or fails.

#### Browser and Responsive Testing

All tests which have been mentioned in the link above has been tested on the following browsers: Chrome, Edge and Firefox. All features and functions worked as expected, including the addition of UX designs (excpet for the known issues mentioned below). The site was also tested on different size devices which consisted of a laptop 13 inch, a tablet as well as a mobile phone.

### Known Issues

- The space between the carousel and the header is to big when changing the device size. 

## Deployment

### Making a Deployment

The project was deployed to Heroku and connected to GitHub pages using the following method:
1. To direct Heroku which application and dependencies are required to run the app being developed, 
create a requirements file.
    - In the terminal, enter "pip3 freeze --local > requirements.txt"
1. Install the Procfile file as that what Heroku looks for to know which files run the app and how to.
    - In the terminal, enter echo web: python app.py>Procfile
    - Note:  In the Procfile, there could be a blank line automatically created, go into the file, remove the blank line and save it again.
1. In [Heroku Dashboard](https://dashboard.heroku.com/), click on 'New', then click on 'Create new app'.
1. Providing it with a unique name and changing the region to 'Europe' (or whatever region you are in). Then click on 'Create app'.
1. In 'Deployment method' click on 'GitHub', Ensuring your GitHub username is visible, either 
search for your repository or type in exactly how your repository is spelt in GitHub. 
When it finds your Repository, it will be visible and you would click on 'Connect'
1. Scroll to the top of the page and click on 'Settings'.
1. Scroll down till you are in 'Config Vars' section and since we hide the environment variables. It would need to be 
added into Heroku manually. You would need to add the following: IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME, ensuring you putting the same values as you did in the env.py file
1. Going back to the terminal within GitPod. Commit and push the files that were created.
1. Once successfully pushed into GitHub, go back to Heroku and click on 'Enable Automatic 
Deployment' and then 'Deploy Branch'.
1. Once completed, a 'View' button would appear meaning the app has been deployed and successfully connected to Github.
1. As Heroku is now connected to Github, for the remaining for project, upload your files into GitHub and it would automatically sync with Heroku.

### Making a Clone

I had to get the SSH key from the repository which allowed me to clone the repository to my local hard drive. 
The method which I used to clone the project was via Github Desktop. I was able to connect my Github 
repository and clone my files through this method. 

1. Open the repository that needs to be cloned.
1. On the top-right side of the page, above the files, you will see a button 'Code' with an arrow point down.
1. Once clicked, a drop-down would appear which would give me the option 'Open with GitHub Desktop' 
(as I had already pre-installed [GitHub Desktop]() previously).
1. Once clicked, it would automatically open the application and request where for it to be saved.

<img src="documentation/images/making-a-clone.png">

## Credits

### Content

The content which i have used for most of my recipes are from the gym that i got to [Any Time Fitness Connect](https://connect.anytimefitness.co.uk/wellbeing/nutrition/recipes/)

### Code

Utilising the code that was used taught from the Code Instute Lessons consisted of (HTML5, CCS3, JavaScript and Python), i also utilised other sources which assisted me in the developing the specific areas.
 
- [Hoover Effects](https://ianlunn.github.io/Hover/)
    - Effects when hovering over buttons
- [Back button functionality](https://www.computerhope.com/issues/ch000317.htm)
- [Contact Modal](https://www.emailjs.com/)
    - Using emailJS service to send emails from the contact form

### Media

The main source for the images i have used is from [Unsplash](https://unsplash.com/) as they provide free useable images:

Carousel:
- [Image 1](https://unsplash.com/photos/EzH46XCDQRY)
- [Image 2](https://unsplash.com/photos/3D43SBDDkAc)
- [Image 3](https://unsplash.com/photos/KPDbRyFOTnE)

- [Background Image](https://unsplash.com/photos/08bOYnH_r_E)

- [Colour Options](https://materializecss.com/color.html)
    - Used from Materialize to set colour scheme across the site.

- [Vegetarian logo](https://upload.wikimedia.org/wikipedia/commons/e/ee/Vegetarian-mark.svg)
    - Used to identify if a recipe is vegetarian or not.

- [Responsive Header](http://ami.responsivedesign.is/#)
    - The header image for the readme file which shows the homepage of the site in different screen sizes.
    
### Acknowledgements

I want to thank my mentor Aaron Sinnott who guided me in the right direction and for his support. This project has allowed me to experience the powers of Python, MongoDB and much more. It has enabled the developer/me to code in a much easier and kicker way without duplicating efforts.

I also want to thank the Code Institure tutorials especially the Task Manager project for helping me to build and achieve this project. The project was developed around a personal problem of mine and that was a method in storing recipes that my mum would give me. This also became a problem for my sister which enhanced the concept of the site. We needed a way to store and edit, share and delete recipes. 