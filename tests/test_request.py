"""This module defines tests for the request class and its methods"""
import unittest
import os

from flask import abort, url_for

from app import create_app
from app.service import Services
from flask_testing import TestCase
from app import create_app
from migrate import migrate

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)

        return app

class RequestTests(TestBase):
    """Define and setup testing class"""

    def setUp(self):
        """ Set up request object before each test"""
        self.request = Services()
        migrate()

    def tearDown(self):
        """ Clear up objects after every test"""
        del self.request

    def test_isuccessful_created(self):
        """Test if request can create sucessfully with correct fields"""
        res = self.request.create("maintenance", "request descriptions", "location", "2018-6-5", "10:20 AM", "1")
        request_d = dict(
            id=1,
            user_id=1,
            category="maintenance",
            location="location",
            date="2018-6-5",
            time="10:20 AM",
            description="request descriptions",
            status="Pending",
            isresolved=False
        )
        self.assertEqual(res, request_d)

    def test_create_existing_request(self):
    	""" Test if a request can be created twice"""
    	
    	self.request.request_list = [{"category" :'maintenance', "description" :'request descriptions',\
         "location":"CBD", "date" : '2018-6-5',\
          "time" : "10:20 AM", "userid":'1'}]
    	res = self.request.create("maintenance", "request descriptions",\
         "location", "2018-6-5", "10:20 AM", "1",)
    	self.assertEqual(res, "Request Already exists")

    def test_request_filter(self):
    	"""Test if filter by userid works"""
    	self.request.create("maintenance", "request descriptions",\
         "location", "2018-6-5", "10:20 AM", "1",)
    	self.request.create("maintenance", "request descriptions",\
         "location", "2018-6-5", "10:20 AM", "2",)
    	res = self.request.view_all("1", "Admin")
    	request_description = res[0]['description']
    	self.assertEqual(request_description, "request descriptions")

    def test_filter_by_id(self):
        """Test if the method finds the exactly specified id"""
        self.request.create("maintenance", "request descriptions", "location", "2018-6-5", "10:20 AM", "1",)
        request_id = self.request.request_list[0]['id']
        requesttype = self.request.request_list[0]['category']
        foundrequest = self.request.find_by_id(request_id)
        self.assertEqual(foundrequest['category'], requesttype)
    
    def test_valid_category(self):
        """Test if the method can detect valid category"""
        res = self.request.valid_category("maintenance")
        self.assertEqual(res, True)

    def test_invalid_category(self):
        """Test if the method can detect invalid category"""
        res = self.request.valid_category("other")
        self.assertEqual(res, False)
     