from times import time_range, compute_overlap_time, iss_passes
import pytest
import datetime
import yaml
import requests
from unittest.mock import patch

# with open("fixture.yaml", "r") as f:
#     fixture_data = yaml.safe_load(f)

# @pytest.mark.parametrize("test_case", fixture_data)
# def test_compute_overlap_time(test_case):
#     properties = list(test_case.values())[0]
#     range1 = time_range(*properties["time_range_1"])
#     range2 = time_range(*properties["time_range_2"])
#     result = compute_overlap_time(range1, range2)
#     if type(properties["expected"]) == list:
#         expected_overlap = [(start, stop) for start, stop in properties['expected']]
#     assert compute_overlap_time(range1, range2) == expected_overlap

with patch.object(requests,'get') as mock_get:
    time_range_for_mock = iss_passes(51.5074, -0.1278, apikey="8Z9NBU-ERH6Q8-SR3BDX-5VOK")
    print(mock_get.mock_calls)

def test_build_default_params():
    lat = 51.5074
    lon = -0.1278
    days=5
    visibility_seconds=0
    alt=0
    apikey="8Z9NBU-ERH6Q8-SR3BDX-5VOK"
    with patch.object(requests,'get') as mock_get:
        default_range = iss_passes(51.5074, -0.1278, apikey="8Z9NBU-ERH6Q8-SR3BDX-5VOK")
        mock_get.assert_called_with(
        f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{lon}/{alt}/{days}/{visibility_seconds}",
                            params={
                                "apiKey": apikey,
                            }
    )
test_build_default_params()