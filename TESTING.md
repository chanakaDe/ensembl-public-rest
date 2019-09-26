# Ensembl Python REST API Testing.

There are 3 main testing methodologies to test this REST API.

  - Manual testing with REST clients like POSTMAN or Insomnia ( [www.insomnia.rest](https://insomnia.rest/) )
  - Unit tests and integration tests. (pytest and Nose2)
  - Test automation using Travis CI.

### Manual testing using REST Clients (POSTMAN and Insomnia)
To test this REST API, you can use following REST API testing interfaces. The reasons for selecting these REST clients are,

  - Its's easy to customize objects and customize reqest headers.
  - Ability to select different type of requesting methods including multi part ( images and files.)
  - Free and open source.

### Unit tests and integration tests. (pytest and Nose2)

When working with REST APIs, it's necessary to test request and response with providing different test cases. Specially the response code and required output values are critical.

I prefer to use pytest and Nose2. The main advantage is we can simply use pytest test cases with Node2 environment. For example, if we need to test a REST end point, we can use something like this : 

```
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_example(client):
    response = client.get("/")
    assert response.status_code == 200
```
And to check login and logout systenms, we can use something like this : 
(Before using test cases, if we want to double check our end points are working fine without any errors,we can use a REST API client such as  POSTMAN to test.)

```
def test_login_logout(client):

    rv = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data

    rv = logout(client)
    assert b'You were logged out' in rv.data

    rv = login(client, flaskr.app.config['USERNAME'] + 'x', flaskr.app.config['PASSWORD'])
    assert b'Invalid username' in rv.data

    rv = login(client, flaskr.app.config['USERNAME'], flaskr.app.config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data
```
I have experience with both pytest and Nose2. But we can do the same using `unittest` module too. But when it comes to automations and flexibility and compatibility, I personally prefer pytest and Nose2.

### Test automation using Travis CI.

There are many test automation system like Team Foundation Server, Jenkins, Buildbot, CircleCI and TravisCI. I prefer TravisCI because it's lightweight, available free for open source projects and specially no dedicated server needed.

In the previos chapter, we created all the test cases using pytest/unittest and Nose2. Now using Travis CI, we can run them automatically each time we are adding them to GitHub account.

We need to visit Travis CI web site and configure our repository with Travis CI. It's a GUI based system and very easy to setup.


For example, we can a test file named `app-test.py`.
This is our `.travis.yml` file.
```
language: python
python:
  - "3.5"
# command to install dependencies
install:
  - pip install -r requirements.txt
# command to run tests
script:
  - export PYTHONPATH=$PYTHONPATH:$(pwd)
  - python app/tests/app-test.py
```
The export python path here is not necessary but it's a failsafe method. 

After a successful run of all the tests, if we need to have a coverage report of all the test, we can use `coveralls`. It's free for open source projects. (https://coveralls.io/)

To use `coveralls` we need to modily our `.travis.yml` like in the following example :

```
language: python
python:
  - "3.5"
# command to install dependencies
install:
  - pip install -r requirements.txt
  - pip install coveralls
# command to run tests
script:
  - export PYTHONPATH=$PYTHONPATH:$(pwd)
  - python app/tests/app-test.py
after_success:
  - coveralls
```

After a successful testing, you can include Travis CI build Badge into your README.md file.