# TODO

* [X] **Landing Page** :heavy_check_mark:
  * [ ] If user is logged in show the "to home page button"
  * [ ] If user is not logged in show the "login / sign up buttons"

* [X] **Register**
* *- frontend*
  * [X] create a vue view as a form in frontend
  * [X] validate the user entries with a schema created in Joi
    * [X] if error show user
    * [X] else make a post request to backend
* *- backend*
  * [X] create POST request route to get the form entries from frontend
  * [X] validate the user according to entries with some library in python
    * [X] if error send status 406
    * [X] else check if username or email is already taken
    * [X] if error send status 406 show "this username or email already taken"
    * [X] else create the user, hash the password and record it to the database
      * [X] generate the token and send it to the user as a record in localStorage
      * [X] redirect the user to the "/home" route

* [ ] **Login**
* *- frontend*
  * [X] create a vue view as a form in frontend
  * [X] make a POST request to backend with username and password
* *- backend*
  * [X] Check the username and password
    * [X] if error send status 422(Unprocessable)
    * [X] else generate the token and send it to the user as a record in localStorage
    * [X] redirect the user to the "/home" route

* [ ] **Home**
* *-frontend*
  * [ ] if user not logged in redirect to login page
  * [ ] create a vue view showing the all events and players

---

* [ ] **General**
  * [ ] Create the isLoggedIn middleware
  * [ ] Set public or private pages and control the access according to user credentials
