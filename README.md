# [Vegan Recipes](https://cookbook-jw.herokuapp.com/)

This app has been developed as part of my Full Stack Developer Diploma Data Centric Development Project.

## UX

### User Stories

- Visitors to the website will want to clearly see a list of recipes to choose from.
- Visitors to the website will want to view the recipes ingredients and instructions.
- Visitors to the website will want to filter the recipe's from a dropdown selection to suit their requirements.
- Visitors to the website will want the ability to edit a recipe.
- Visitors to the website will want the ability to add a new recipe.
- Visitors to the website will want the ability to delete a recipe.

## Features

### Existing Features

This is a web application which that allows visitors to the website to access, add, modify and delete vegan cooking recipes. It is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted on the Heroku platform.
1. The [index page](templates/index.html) introduces the visitor to the website, and displays the list of recipes. Each recipe has a button link to edit or delete the recipe. Links are provided in the navbar to the homepage and to add new recipe to the database.
1. The [add recipe page](templates/addrecipe.html) allows the visitor to add their own recipe to the database by completing the form. The recipe is then added to and stored in the mLab MongoDB database.
1. The [edit recipe page](templates/editrecipe.html) allows the visitor to edit the existing recipes in the database. The recipe data is pre-filled from the database. Once the visitor has updated the recipe, the "update recipe button" once clicked will send the updated recipe to the database.

## Technologies Used

The app was built using [Python](https://www.python.org/) code.

Other technologies used in this project are:

- [Flask](http://flask.pocoo.org/), a Python Microframework
  - for routing
  - for redirecting and rendering templates
  - for requesting methods
- [Jinja2](http://jinja.pocoo.org/docs/2.10/), a templating language
  - for rendering data in the html templates, communicating between front-end and back-end.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), the most basic building block of the Web
  - for writing the basic front-end content
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), a stylesheet language
  - for styling the page
- [JQuery](https://jquery.com)
  - for allowing the Javascript functionality in Bootstrap to work.
- [Bootstrap](http://getbootstrap.com/), a front-end framework
  - for general responsiveness.
  - for inegral components and mobile friendly pages. 
- [Materialize](http://archives.materializecss.com/0.100.2/), a modern responsive front-end framework based on Material Design.
  - for general responsiveness.
  - for inegral components such as navbar and mobile friendly pages.
- [MongoDB](https://mlab.com/), MongoDB is a cross-platform document-oriented database program. 
  - for storing and accessing the recipe database.

## Testing

The app has been manually tested. each recipe has been checked against the database to ensure it is requesting the correct information from the database.

Each recipe dropdown has been manually checked to ensure it is working correctly.

The filter recipe feature has been tested to ensure it is filtering correctly. A number of different filtering options have been tested to ensure they are displaying the correctly filtered recipes in the webpage.

The edit recipe feature has been performed on number of recipes, with the recipe being edited on the webpage. The edits made have then been checked back to the database to ensure they are being correctly stored in the database.

The delete recipe feature has been performed on a number of recipes and checked back to the database to ensure they are being correctly stored in the database.

The add recipe feature has been tested with new recipes added to the database through the add recipe webpage. The database has been checked to ensure new recipes are being added and stored in the database correctly. 

Navbar links have been checked to ensure they are linking correctly.

## Deployment

This app is hosted on Heroku. To be able to run the code on Heroku, a Procfile was added to tell Heroku it's a Python project (web: python app.py), as were the Config vars for IP (0.0.0.0) and PORT (5000).