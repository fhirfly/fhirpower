import unittest
from fhirpower import flatten_fhir

class TestFlattenFHIR(unittest.TestCase):

    def test_flatten_simple_resource(self):
        nested_json = {
            "resourceType": "Patient",
            "name": [
                {
                    "given": "John",
                    "family": "Doe"
                }
            ]
        }
        
        expected_output = {
            "resourceType": "Patient",
            "name_0_given": "John",
            "name_0_family": "Doe"
        }
        
        flattened_dict = flatten_fhir(nested_json)
        
        self.assertDictEqual(flattened_dict, expected_output)

if __name__ == '__main__':
    unittest.main()
