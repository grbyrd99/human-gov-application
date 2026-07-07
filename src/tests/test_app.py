import pytest
from app import home_page, calculate_bonus

class TestHomePage:
    def test_home_page_valid_state(self):
        """Tests the home page with a valid state"""
        assert home_page('California') == 'Human Resources Management System - State of California'        

    def test_home_page_empty_state(self):
        """Tests the home page with an empty state"""
        with pytest.raises(ValueError, match="State cannot be empty"):
            home_page('')

class TestCalculateBonus:
    def test_valid_inputs(self):
        """Tests bonus calculation with valid inputs"""
        assert calculate_bonus(1000, 1) == 0
        assert calculate_bonus(1000, 2) == 50
        assert calculate_bonus(1000, 3) == 100
        assert calculate_bonus(1000, 4) == 150
        assert calculate_bonus(1000, 5) == 200
        assert calculate_bonus(5000, 5) == 1000

    def test_invalid_salary(self):
        """Tests bonus calculation with invalid salary"""
        with pytest.raises(ValueError, match="Salary must be positive"):
            calculate_bonus(-1000, 3)
        with pytest.raises(ValueError, match="Salary must be positive"):
            calculate_bonus(0, 3)

    def test_invalid_performance_rating(self):
        """Tests bonus calculation with invalid performance rating"""
        with pytest.raises(ValueError, match="Performance rating must be between 1 and 5"):
            calculate_bonus(1000, 0)
        with pytest.raises(ValueError, match="Performance rating must be between 1 and 5"):
            calculate_bonus(1000, 6)
