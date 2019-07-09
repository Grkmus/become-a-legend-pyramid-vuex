# TODO

## Frontend

* [X] **Landing Page** :heavy_check_mark:
  * [ ] If user is logged in show the "to home page button"
  * [ ] If user is not logged in show the "login / sign up buttons"

* [X] **Register**
* *- frontend*
  * [ ] create a vue view as a form in frontend
  * [ ] validate the user entries with a schema created in Joi
    * [ ] if error show user
    * [ ] else make a post request to backend
* *- backend*
  * [ ] create POST request route to get the form entries from frontend
  * [ ] validate the user according to entries with some library in python
    * [ ] if error send status 406
    * [ ] else check if username or email is already taken
    * [ ] if error send status 406 show "this username or email already taken"
    * [ ] else create the user, hash the password and record it to the database
      * [ ] generate the token and send it to the user as a record in localStorage
      * [ ] redirect the user to the "/home" route

* [ ] **Login**
* *- frontend*
  * [ ] create a vue view as a form in frontend
  * [ ] make a POST request to backend with username and password
* *- backend*
  * [ ] Check the username and password
    * [ ] if error send status 422(Unprocessable)
    * [ ] else generate the token and send it to the user as a record in localStorage
    * [ ] redirect the user to the "/home" route

* [ ] **Home**
* *-frontend*
  * [ ] if user not logged in redirect to login page
  * [ ] create a vue view showing the all events and players

---

* [ ] **General**
  * [ ] Create the isLoggedIn middleware
