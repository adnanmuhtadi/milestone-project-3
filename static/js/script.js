$(document).ready(function () {
    //for the Navbar
    $(".sidenav").sidenav({ edge: "right" });
    //for the carousel
    $(".carousel").carousel();
    //for the recipes 
    $('.collapsible').collapsible();
    //for the drop down option when choosing the type of meal
    //also for the drop in the add_recipe.html
    $('select').formSelect();
    //dropdown for the menu bar
    $(".dropdown-trigger").dropdown();
    //modal built for the contact form
    $('.modal').modal();

    //Carousel function which would go round on a set timer
    setInterval(function () {
        $('.carousel').carousel('next');
    }, 3000);

});