import requests
import unittest

class TestCitiesRoute(unittest.TestCase):

    def test_get_cities_in_spain(self):
        # Test case for the endpoint /cities/Spain
        response = requests.get('http://localhost:5000/cities/Spain')  # Adjust the URL accordingly
        self.assertEqual(response.status_code, 200)
        cities = response.json()
        self.assertIsInstance(cities, list)  # Check if the response is a list
        # Add your expected cities in Spain for further assertions
        expected_cities = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']  # Example expected cities
        for city in expected_cities:
            self.assertIn(city, cities)

if __name__ == '__main__':
    unittest.main()