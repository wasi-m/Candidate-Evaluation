# Candidate Evaluation System

Candidate Evaluation System is an web based platform that allows candidates to be evaluated by multiple people.

Candidate who wants to apply needs to fillout the folrm on http://wasimtamboli.pythonanywhere.com/
Once the form is filed the Admin evaluator, evaluates the candidate.

Users who wants to evaluate the profiles submitted by the candidates, needs to signup on http://wasimtamboli.pythonanywhere.com/user/signup/
Once signup and login is done users can evaluate the Candidate profiles.<br> Next Step is to make the email approval when users signup.

Users can view all Candiadte profiles on http://wasimtamboli.pythonanywhere.com/user/dashboard/<br>
Users can Evaluate the candidate by clicking on candidate email<br>
Users can view all Candiadte Evaluated Results on http://wasimtamboli.pythonanywhere.com/user/allresults/<br>
Users can view all 5 Star Candiadte Evaluated Results on http://wasimtamboli.pythonanywhere.com/user/topresults/<br>


Project Details
--------------------------------------------
- Backend - Python/Django
- Database - SQLite3
- Frontend - Bootstrap, HTML, CSS, JavaScript, Jquery
- Template used from CreativeTim 
- Hosted on - pythonanywhere.com
- website - http://wasimtamboli.pythonanywhere.com/


Setup Project
--------------------------------------------
1. Create a virtual environmnet and activate
```
$ virtualenv venv
$ source venv/bin/activate
```
2. Clone Project from https://github.com/wasi-m/Candidate-Evaluation.git
```
$ git clone https://github.com/wasi-m/Candidate-Evaluation.git
```
3. Install all project dependency from requirements.txt file
```
$ pip install -r requirements.txt
```
4. Go to project folder and run the Django makemigrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5. Go to project folder and run Django development server
```
$ python manage.py runserver
```
6. Opne http://127.0.0.1:8000 in browser

~ Volla ~
