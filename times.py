import datetime
import requests

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if start_time_s > end_time_s:
        raise ValueError("Start time must be less than or equal to end time.")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if low < high:
                overlap_time.append((low, high))
    return overlap_time





def iss_passes(lat, lon, days=5, visibility_seconds=0, alt=0, apikey=None):
    """
    Returns a time_range-like output for intervals of time when the International Space Station
    passes at a given location and for a number of days from today.
    """
    iss_request = requests.get(f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{lon}/{alt}/{days}/{visibility_seconds}",
                               params={
                                   "apiKey": apikey,
                               })

    if iss_request.status_code != 200:
        # if the request failed for some reason
        return []
    response = iss_request.json()
    return [(datetime.datetime.fromtimestamp(x['startUTC']).strftime("%Y-%m-%d %H:%M:%S"),
             (datetime.datetime.fromtimestamp(x['startUTC'] + x['duration'])).strftime("%Y-%m-%d %H:%M:%S"))
            for x in response['passes']]


if __name__ == "__main__":
    print(iss_passes(51.5074, -0.1278, apikey="8Z9NBU-ERH6Q8-SR3BDX-5VOK")) # ISS passes over London