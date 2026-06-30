# test_metapulse.py
"""
Tests for MetaPulse module.
"""

import unittest
from metapulse import MetaPulse

class TestMetaPulse(unittest.TestCase):
    """Test cases for MetaPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaPulse()
        self.assertIsInstance(instance, MetaPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
