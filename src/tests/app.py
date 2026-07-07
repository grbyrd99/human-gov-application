def home_page(state):
    """Returns the home page of the HR system for a specific state"""
    if not state:
        raise ValueError("State cannot be empty")
    return 'Human Resources Management System - State of ' + state

def calculate_bonus(salary, performance_rating):
    """Calculates an employee's bonus based on salary and performance rating"""
    if salary <= 0:
        raise ValueError("Salary must be positive")
    if performance_rating not in [1, 2, 3, 4, 5]:
        raise ValueError("Performance rating must be between 1 and 5")
    
    bonus_rates = {1: 0, 2: 0.05, 3: 0.1, 4: 0.15, 5: 0.2}
    return salary * bonus_rates[performance_rating]
