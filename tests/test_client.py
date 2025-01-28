"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import client
from email_validator import validate_email, EmailNotValidError

class TestClient(unittest.TestCase):
    def setUp(self):
        """
        This def is for the setup of the tests
        """
        self.client = client(7, "Beerdavinder" ,"singh", "beerdavinder@pixel.com")

    def test_client_number_invalid(self):
        """
        this def is for the invalid client number
        it will raise a error if the client number is not integar
        """
        with self.assertRaises(ValueError):
            self.client = client("bd", "Beerdavinder", "singh" , "beerdavinder@pixel.com")

    def test_client_number_valid(self):
        """
        this def is for valid client number
        """
        self.assertEqual(self.client.client_number, 7)

    def test_first_name_invalid(self):
        """
        this def is for the invalid first name
        it will raise a error if the first name in empty
        """
        with self.assertRaises(ValueError):
            self.client = client(7, "", "singh", "beerdavinder@pixel.com")

    def test_first_name_valid(self):
        """
        this def is for the valid first name
        """
        self.assertEqual(self.client.first_name, "Beerdavinder")

    def test_last_name_invalid(self):
        """
        this def is for the invalid last name 
        it will raise a error if the last name is empty
        """
        with self.assertRaises(ValueError):
            self.client = client(7, "Beerdavinder", "", "beerdavinder@pixel.com")
    
    def test_last_name_valid(self):
        """
        this def is for the valid last name
        """
        self.assertEqual(self.client.last_name, "singh")

    def test_invalid_email_address(self):
        """
        this def is for the invalid email address 
        it will raise a error if the email address is invalid
        """
        self.client = client(7, "Beerdavinder", "Singh", "beerdavinder@pixel.com")
        self.assertEqual(self.client._email_address, "beerdavinder@pixel.com") 

    def test_email_address_valid(self):
        """
        this def is for the valid email address
        """
        self.cleint = client(7,"Beerdavinder" , "singh", "beerdavinder@pixel.com")

    def test__str__(self):
        """
        this def is for the str representation
        """
        expected_output = "singh, Beerdavinder [7] - beerdavinder@pixel.com"
        self.assertEqual(str(self.client),expected_output)

    