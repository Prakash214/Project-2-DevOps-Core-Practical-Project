from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app
import application.routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    @patch('application.routes.choice', return_value='blackbeard')
    def test_characters1(self, mock_func):
        response = self.client.post(url_for('characters'), json={'fruits':'Dark-Dark Fruit'})
        self.assert200(response)
        self.assertIn(b'blackbeard',response.data)

    @patch('application.routes.choice', return_value='blackbeard')
    def test_characters2(self, mock_func):
        response = self.client.post(url_for('characters'), json={'fruits':'Soul-Soul Fruit'})
        self.assert200(response)
        self.assertIn(b'blackbeard',response.data)

    @patch('application.routes.choice', return_value='blackbeard')
    def test_characters3(self, mock_func):
        response = self.client.post(url_for('characters'), json={'fruits':'Tremor-Tremor Fruit'})
        self.assert200(response)
        self.assertIn(b'blackbeard',response.data)
    
    @patch('application.routes.choice', return_value='blackbeard')
    def test_characters4(self, mock_func):
        response = self.client.post(url_for('get_characters'), json={'fruits':'Fish-Fish Fruit'})
        self.assert200(response)
        self.assertIn(b'blackbeard',response.data)