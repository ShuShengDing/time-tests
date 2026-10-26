from times import time_range, compute_overlap_time
import pytest
import datetime

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    print(large)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(short)
    print(compute_overlap_time(large, short))
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_completely_separate():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    
    result = compute_overlap_time(range1, range2)
    
    assert result == [] 




def test_freedom():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00",2, 60)
    print(range1)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 13:00:00",10, 30)
    print(range2)
    result = compute_overlap_time(range1, range2)
    
    expected = [None]
    expected[0] = ('2010-01-12 10:30:30', '2010-01-12 10:44:33')
    assert result[0] == expected[0]