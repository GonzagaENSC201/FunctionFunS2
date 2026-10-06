import numpy as np
from jump import calculate_jump_distance, calculate_required_speed

def test_calculate_jump_distance():
    assert np.isclose(calculate_jump_distance(6.0, 0.8), 4.8) # shopping cart test case
    assert np.isclose(calculate_jump_distance(15.5, 1.4), 21.7) # dirt bike test case

def test_calculate_required_speed():
    actual_speed = calculate_required_speed(12, 1.5)
    assert np.isclose(actual_speed, 8.0)
    assert np.isclose(calculate_required_speed(20, 2), 10.0)
    assert np.isclose(calculate_required_speed(0, 3), 0.0)