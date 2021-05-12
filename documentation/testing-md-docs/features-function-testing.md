<h1 align="center">Feature, Functional & Useability Testing</h1>

I will be testing all my functions and features within each section of my site and ensuring that it is useable across different browsers which are as follows: Chrome, Edge and Firefox. The devices I would be using to run the tests are as follows: 13inch Macbook Pro, 10.2 inch iPad and 6.5 inch iPhone Pro Max.

A pass would mean that the feature that I am testing has been run on the said browsers and devices, in a situation one of the browsers and/or devices has an issue, it would be considered as a fail.

## Navigation Bar

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Navigation bar | When hovering over the navigation, a box shadow is displayed | :heavy_check_mark: |
My Profile link | When you click on 'My Profile' a drop down open appears with other navigation options | :heavy_check_mark: |
The layout on mobile view | A hamburger menu option would be visible and when clicked, options to other pages woudl be available| :heavy_check_mark: |
Navigation for Admin | When logged in as admin, an open to 'Create Meal Type' is visibale | :heavy_check_mark: |

## Footer

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Social links | Wheen clicked, to be directed to the social media web pages | :heavy_check_mark: |

## Contact Modal

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Pop-up | When you click on 'Contact Us', a center modal appears | :heavy_check_mark: |
Email clear | If form is filed and the clear button is clicked, all information on the form will be cleared. | :heavy_check_mark: |
Form 'Full Name' | Cannot enter more than 3 characters in that field
Form 'Full Name' | Cannot enter more than 50 characters in that field
Form 'Email' | Cannot enter more than 5 characters in that field
Form 'Email' | Cannot enter more than 50 characters in that field
Form 'Message Subject' | Cannot enter more than 5 characters in that field
Form 'Message Subject' | Cannot enter more than 50 characters in that field
Send Email | Error message appear, input filed highlighted red if the field has incorrect requirements and email not sent | :heavy_check_mark: |
Send Email | Error message appear, input filed highlighted red if the field has been left out and email not sent | :heavy_check_mark: |
Close Modal | When outside of the modal is clicked, modal would close | :heavy_check_mark: |

## Home Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
carousel | Images to rotate every 3 seconds | :heavy_check_mark: |
Search | Search by recipe name | :heavy_check_mark: |
Search | Search by ingredients | :heavy_check_mark: |
Search | Search for a recipe and no results appear, error message to appear | :heavy_check_mark: |
Reset | Clear all search results and return all shared recipes to the main screen | :heavy_check_mark: |
View Full Recipe | Direct you to another page with all details of the recipe | :heavy_check_mark: |
Edit Recipe | Only for registered users can a user see the edit option on their own recipes | :heavy_check_mark: |
Delete Recipe | Only for registered users can a user see the delete option on their own recipes | :heavy_check_mark: |
Colour scheme of recipe cards | Registered user would only be able to see their recipes in a different colour | :heavy_check_mark: |
Recipes | When it exceeds 3 recipes, pagination would provide the recipes on another page | :heavy_check_mark: |

## Registration Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Form | To be able to enter information on the form | :heavy_check_mark: |
Username | If the field is missed, a helper text would appear in red | :heavy_check_mark: |
Username | If username already exists, a flash message would appear to submit
Username | If entered less than 5 or more than 25 characters, an error would appear | :heavy_check_mark: |
Password | If the field is missed, a helper text would appear in red | :heavy_check_mark: |
Confirm Password | If the field is missed, a helper text would appear in red | :heavy_check_mark: |
Password/Confirm Password | If entered less than 5 or more than 25 characters, an error would appear | :heavy_check_mark: |
Other fields | Can still register without having them filled | :heavy_check_mark: |
Confirm Password | If the field is missed, a helper text would appear in red | :heavy_check_mark: |
Password/Confirm password | If confirm password and current password do not match, flash message to appear | :heavy_check_mark: |

## Login Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Username | If username does not exist in the database, a flash error message would appear | :heavy_check_mark: |
Username | If the field is missed, a helper text would appear in red | :heavy_check_mark: |
Password | If the password is wrong, a flash error message would appear | :heavy_check_mark: |
Username/Password | If entered less than 5 or more than 25 characters, an error would appear | :heavy_check_mark: |
Username/Password | If username and password is correct, user to be directed to the 'My Recipe' page | :heavy_check_mark: |

## Add Recipe Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Form | To be able to fill out the form | :heavy_check_mark: |
Recipe Name | If field missed, a helper text appears under the field | :heavy_check_mark: |
Recipe Name | Cannot enter less than 5 characters | :heavy_check_mark: |
Recipe Name | Cannot enter more than 25 characters | :heavy_check_mark: |
Prep Time | Only numbers to be entered | :heavy_check_mark: |
Cooking Time | Only numbers to be entered | :heavy_check_mark: |
Number of Serving | Only numbers to be entered | :heavy_check_mark: |
Ingredients | If field missed, a helper text appears under the field | :heavy_check_mark: |
Steps | If field missed, a helper text appears under the field | :heavy_check_mark: |
Is Veg | default set to false | :heavy_check_mark: |
Is Veg | If Activated, to display a 'V' logo next to the recipe name in the 'My recipe' page and home page | :heavy_check_mark: |
To Share | Default set be false | :heavy_check_mark: |
To share | If activated, to be be displayed in the home page | :heavy_check_mark: |
Clear button | To clear the form | :heavy_check_mark: |
Go back button | To go to the previous page | :heavy_check_mark: |
Add recipe button | To be redirected to the 'My Recipe' page with the recipe being displayed part of the list of recipes | :heavy_check_mark: |
Add recipe | A flash message to confirm the creation of the recipe | :heavy_check_mark: |

## Edit Recipe Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Form | All information to be displayed in their appropriate fields | :heavy_check_mark: |
Form 'Recipe Name' | Cannot enter less 5 and/or more than 25 characters | :heavy_check_mark: |
Form | To be able to amend the form from any field | :heavy_check_mark: |
Clear button | To clear the from from exisiting data | | :x:
Go Back button | To go back to the previous page | :heavy_check_mark: |
Update Recipe button | To svae the recipe and be directed to the 'My Recipe' page | :heavy_check_mark: |
Update Recipe | A flash message to inform user the recipe has been updated | :heavy_check_mark: |

## View Recipe Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Recipe Details | All information being pulled from the DB | :heavy_check_mark: |
Recipe Image | Imaging being pull from an external URL | :heavy_check_mark: |
Recipe Image | If no image URL has been provided, then an alternative image will be uploaded in its place. | :heavy_check_mark: |
Ingredients Accordin | Display list of ingredients in an ordered list | :heavy_check_mark: |
Steps Accordin | Display a list of steps in an ordered list | :heavy_check_mark: |
Go Back button | To go back to the previous page | :heavy_check_mark: |
Delete button | Remove current recipe | :heavy_check_mark: |
Edit button | Get redirected to that recipe edit page | :heavy_check_mark: |

## My Recipe Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Recipe | To be able to see 6 recipes on a page | :heavy_check_mark: |
Recipe | Pagination once it exceeds 6 recipes | :heavy_check_mark: |
Recipe | Missing information within the recipe would be displayed with a '-' | :heavy_check_mark: |
Search | Search by recipe name | :heavy_check_mark: |
Search | Search by ingredients | :heavy_check_mark: |
Search | Search for a recipe and no results appear, error message to appear | :heavy_check_mark: |
Reset | Clear all search results and return all shared recipes to the main screen | :heavy_check_mark: |
View Full Recipe | Direct you to another page with all details of the recipe | :heavy_check_mark: |
Edit Recipe | Edit option available when clicked on the "^" within the recipe | :heavy_check_mark: |
Delete Recipe | Delete option available when clicked on the "^" within the recipe | :heavy_check_mark: |
Delete Recipe | When recipe is deleted, a flash message would appear confirming the removal of the recipe | :heavy_check_mark: |
vegetarian logo | If recipe is considered vegetarian, to have a 'V' image next to the title | :heavy_check_mark: |

## My Profile Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
User first name | Welcome the user first name when entering the page | :heavy_check_mark: |
Edit username | once button 'Edit Username', to be directed to said page | :heavy_check_mark: |
Edit password | once button 'Edit Password', to be directed to said page | :heavy_check_mark: |

## Edit Username Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Current username | User current username displayed on page | :heavy_check_mark: |
New Username | If less than 5  or more than 25 characters are entered, error message to appear on the bottom of the field | :heavy_check_mark: |
Created-by | Created by field on all recipes | :heavy_check_mark: |
Username/created-by update | When updating Username, it updates the created-by as well which where associated to the previous username | :heavy_check_mark: |
Username Update | When updating username to be logged out and redirected to the login page with a flash message | :heavy_check_mark: |

## Edit Password Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Current password | Required to enter current password to proceed | :heavy_check_mark: |
Current password | If missed, a help error message would appear | :heavy_check_mark: |
Current password | If less than 5 or more than 25 characters are entered, error message to appear on the bottom of the field | :heavy_check_mark: |
Current password | If current password is incorrect, flash message to appear | :heavy_check_mark: |
New password | If less than 5 or more than 25 characters are entered, error message to appear on the bottom of the field | :heavy_check_mark: |
New password | If missed, a help error message would appear | :heavy_check_mark: |
Confirm password | If less than 5 or more than 25 characters are entered, error message to appear on the bottom of the field | :heavy_check_mark: |
Confirm password | If missed, a help error message would appear | :heavy_check_mark: |
Password/Confirm password | If confirm password and current password do not match, flash message to appear | :heavy_check_mark: |

## Logout

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Avilable Logout Option | when you click on the drop down 'My Profile' Select 'Logout' | :heavy_check_mark: |
Logout | To be directed to the login page with a flash message | :heavy_check_mark: |

## Admin Access

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Manage Meal Type | View 'Manage Meal Type' in the navigation bar | :heavy_check_mark: |
Manage Meal Type | Only available to Admin user | :heavy_check_mark: |
Navigation bar | To view all the navigation options available | :heavy_check_mark: |

## Manage Meal Type

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Meal Types | View all meal types available in card view | :heavy_check_mark: |
Add Meal button | Direct admin user to add_meal.html to add meal type | :heavy_check_mark: |
Delete button | Delete the meal type | :heavy_check_mark: |
Delete button | A flash message that meal type has been deleted | :heavy_check_mark: |
Edit button | Direct admin user to edit_mel.html | :heavy_check_mark: |

## Add Meal Type

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Form | Available to input within the form | :heavy_check_mark: |
Form | Cannot add less than 3 characters | :heavy_check_mark: |
Form | Cannot add more than 50 characters | :heavy_check_mark: |
Form | If field missed, a helper text appears under the field | :heavy_check_mark: |
Go Back button | Takes user to the previous page | :heavy_check_mark: |
Clear button | Clear the form |  | :x:
Add Meal button | Add the meal type to the database which becomes visible in the Manage Meal Type page | :heavy_check_mark: |

## Edit Meal Type

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Form | The name of the meal type to be visible on the form | :heavy_check_mark: |
Go Back button | Takes user to the previous page | :heavy_check_mark: |
Clear button | Clear the form |  | :x:
Update Meal button | Updates the Meal Type | :heavy_check_mark: |
Update Meal button | Redirects user back to the Manage Meal Type | :heavy_check_mark: |

## Error Page

Feature/Function | Description | Pass | Fail
------------ | ------------- | ------------- | -------------
Error 404 | Change the end of the URL, a new page for the 404 error appear | :heavy_check_mark: |
Error 500 | When an internal server occurs, a new page for the 500 error appear | :heavy_check_mark: |


[Return to main README.md](https://github.com/adnanmuhtadi/milestone-project-3)