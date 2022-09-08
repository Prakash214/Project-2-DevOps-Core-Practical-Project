from flask import url_for
from flask_testing import TestCase
import pytest
import requests_mock
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestFrontend(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://fruit:5000/get-fruit', json={'fruit':'Fish-Fish Fruit'})
            m.get('http://friend:5000/get-friend', json={'friend':'jimbei'})
            m.post('http://characters:5000/get-characters', json={'character':'kaidou'})
            response = self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'You will be hunting kaidou for the Fish-Fish Fruit with jimbei', response.data)