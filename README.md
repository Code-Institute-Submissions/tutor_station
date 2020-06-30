# Tutor Station

<a href="https://jh-tutor-station.herokuapp.com/" target="_blank">Hosted website</a>

A one stop shop for tutor hires. I work at a school with a lot of kids that need special attention and something like this would be handy for many parents. 
An open market where users can offer their services at a price they dictate. Where the service will process payments, pay taxes, and forward payment to the tutor for a nominal percentage.
 
## UX
 
What I envision is two sperate personalized profiles, one being the user profile, and one being the tutor. The user profile is not optional, but also can be left blank, where the tutor profile is optional. Once created you go into the pool of avaible users who are availbe to be rented.
The user profile will have a standard configuration. Where the tutor profile will include things like the Krona per hour (I live in Sweden), education, description, and a picture (headshot).

I would like to develop a time confirmation system that would allow both parties to agree on a mutual time before payment is processed.

- As a user type, I want to perform an action, so that I can achieve a goal.

<a href="https://docs.google.com/spreadsheets/d/1xQu8-Sik9xZ30X8uSA1TUd0WgebbZ9QiLu0bxyl3Png/edit?usp=sharing" target="_blank">User Stories</a>

## Features

Picture adoption into user profiles was something I wanted but I had it upload into another userprofile form. I had the image display beside the form, but I discovered that it took an additional refresh to make the image appear. Just using a onerror="imgError(this) to refresh the page would not do because there existed a possibility of an infinite refresh loop, so I split the url and used that to make sure it was correct.

Making the tutor profiles only editable by the creating user but availble for everyone to see in the marketplace was challenging. I ended up pushing their unique username into the form in a field that was not shown on the HTML render. Using that logic and a context processor I managed to make that work.
 
### Existing Features
- Feature 1 - Account Creation with email confirmation. Full allauth intregration
- Editable User profiles with a picture.
- Tutor Profiles that are public, but only editable by their creators.
- Client request a tutoring time (did not complete).
- AWS S3 bucket intregration for filestorage.
- Stripe checkouts with webhooks.

### Features Left to Implement
- Tutor confirms/reschedules tutoring time.
- Client confirms and processes payment for the agreed amount of hours. 

## Technologies Used

- [Javascript](https://www.javascript.com)
    - The project uses **Javascript** for DOM manipulation.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Bootstrap](https://getbootstrap.com)
    - The project uses **Bootstrap** for easy formatting and website design

- [Django](https://www.djangoproject.com)
    - The project uses **Django**. For their diverse database integrated web framework.

- [Python 3.8.3](https://www.python.org)
    - The project uses **Python**. To operate Django.

- [Heroku](https://www.heroku.com)
    - The project uses **Heroku**. For Web Hosting and Postgres database.

- [Amazon.AWS - S3](https://aws.amazon.com)
    - The project uses **Amazon.AWS - S3**. For static file hosting.

- [Github](https://github.com)
    - The project uses **Github**. For version control.

- [Gitpod](https://gitpod.io)
    - The project uses **Gitpod**. As the creating IDE.

- [Gmail](https://www.google.com/gmail)
    - The project uses **Gmail**. App Password to send automatic emails.

- [Stripe](https://stripe.com/)
    - The project uses **Stripe**. For credit card processing.


## Testing

We tested by constant use and perfection until it worked, after it was hosted I had several people look it over to find bugs. There were few. I also did a flake8 review to try and locate any critical issues.


## Deployment

Gitpod for version control connected to Heroku.

- Gitpod Deployment uses a SQLite3 database and heroku is using a postgres with global vars secured there.
- Heroku deployment is also utilizing an amazon S3 bucket for storage of static files, with all vars secured on Heroku.

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

Ckz8780 and his Boutique Ado Project. His videos on the current version of django and his project where outstanding. I relied heavily on his design and code. and it's influence is heavily noticeable with my site. I view this project as a starting point and even though his videos were good, I needed to manipulate his work in order to figure out how Django really worked.
Stackoverflow, because they are a great community who can often shelp you get unstuck.
My Wife, Sofia for drawing pictures for me to use.

