//The sendEmail.js file was created utilising the following links to assist with the built of the site
//  https://dashboard.emailjs.com/admin
//  https://dashboard.emailjs.com/admin/integration/browser
//  https://www.emailjs.com/docs/sdk/send/

//Creating a variable to associate the button
let btn = document.getElementById('send-modal-button');

//This section of the code listens to the events happening within the contact form and change
//the text inside the button from 'Send' to 'Sending...'
document.getElementById('contactForm')
    .addEventListener('submit', function (event) {
        event.preventDefault();

        //Informing the user that the email is sending.
        btn.textContent = 'Sending...';

        // Variables which stores the details which connect the service and template associated within the EmailJS
        let serviceID = 'personal-gmail';
        let templateID = 'home-cooking';

        /* The two variables mentioned above are used within the template parameters. The template parameters
        are used in the email template that has been set up within EmailJS along with side my input fields
        of the contact form within the HTML file.*/
        emailjs.send(serviceID, templateID, {
            "from_fullname": this.from_fullname.value,
            "from_useremail": this.from_useremail.value,
            "message_subject": this.message_subject.value,
            "message_summary": this.message_summary.value,
        })

            /*The object which would contain the text which would be changed if successful as well as the message
            within the console log within the browser and the status in a text format as well as an alert box which
            would notify the user once the message has been sent. */
            .then((response) => {
                btn.textContent = 'Sent!';
                console.log("Message Sent!", response.statusText);
                alert('Message sent. Someone will reach out to you shortly.');

                /* The object which would contain the text which would be changed if unsuccessful as well as the message
                within the console log within the browser and the status in a text format as well as an alert box which
                would notify the user if the message was not sent. */
            }, (error) => {
                btn.textContent = 'Error!';
                console.log("Message did not send!", response.statusText);
                alert(`Unfortunately, the message was not sent. Please trying again later.`);
            });
    });