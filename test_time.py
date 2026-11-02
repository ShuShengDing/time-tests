from times import time_range, compute_overlap_time
import pytest
import datetime
import yaml

# def test_given_input():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected


# def test_completely_separate(): # two time ranges that do not overlap
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    
#     result = compute_overlap_time(range1, range2)
    
#     assert result == [] 

# def test_freedom(): # two time ranges that both contain several intervals each
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00",5, 60)
#     print(range1)
#     range2 = time_range("2010-01-12 10:30:00", "2010-01-12 13:00:00",10, 30)
#     print(range2)
#     result = compute_overlap_time(range1, range2)
#     print(result)

#     expected = ('2010-01-12 10:30:00', '2010-01-12 10:35:36')
#     assert result[0] == expected

# def test_same_end_start(): # two time ranges that end exactly at the same time when the other starts
#     range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#     range2 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00")
#     result = compute_overlap_time(range1, range2)
    
#     assert result == [] 

# def test_start_end_afterwards():
#     start_time = "2010-01-12 12:00:00"
#     end_time = "2010-01-12 10:00:00"
    
#     with pytest.raises(ValueError, match="Start time must be less than or equal to end time."):
#         time_range(start_time, end_time)

with open("fixture.yaml", "r") as f:
    fixture_data = yaml.safe_load(f)
    print(fixture_data)

@pytest.mark.parametrize("test_case", fixture_data)
def test_compute_overlap_time(test_case):
    properties = list(test_case.values())[0]
    range1 = time_range(*properties["time_range_1"])
    range2 = time_range(*properties["time_range_2"])
    result = compute_overlap_time(range1, range2)
    if type(properties["expected"]) == list:
        expected_overlap = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(range1, range2) == expected_overlap
