$(document).ready(function () {
    //for the Navbar
    $(".sidenav").sidenav({ edge: "right" });
    //for the carousel
    $(".carousel").carousel();

    //Carousel function which would go round on a set timer
    setInterval(function () {
        $('.carousel').carousel('next');

    }, 3000);
});