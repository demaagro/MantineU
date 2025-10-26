# test_mantineui.py
"""
Tests for MantineUI module.
"""

import unittest
from mantineui import MantineUI

class TestMantineUI(unittest.TestCase):
    """Test cases for MantineUI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MantineUI()
        self.assertIsInstance(instance, MantineUI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MantineUI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
