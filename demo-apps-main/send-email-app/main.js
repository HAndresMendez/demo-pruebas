// Check out more at: https://www.twilio.com/blog/how-to-send-emails-in-javascript-with-sendgrid
const sgMail = require('@sendgrid/mail');

// Load environment variables
require('dotenv').config();

sgMail.setApiKey(process.env.SENDGRID_API_KEY);
const msg = {
   to: process.env.EMAIL_ADDRESS_TO,
   from: process.env.EMAIL_ADDRESS_FROM,
   subject: 'It works!!!',
   text: 'Hey there! It works!! Congrats! :D',
   html: '<strong>and easy to do anywhere, even with Node.js</strong>',
};

console.log(msg)

sgMail.send(msg).then(() => {
   console.log('Message sent')
}).catch((error) => {
   console.log(error.response.body)
   // console.log(error.response.body.errors[0].message)
})