from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_seconds_for_meter = float(input())
base_time = distance_meters * time_seconds_for_meter
added_time = floor(distance_meters / 15) * 12.5
time_needed = base_time + added_time
if time_needed < record_seconds:
    print(f'Yes, he succeeded! The new world record is {time_needed:.2f} seconds.')
else:
    print(f'No, he failed! He was {(time_needed - record_seconds):.2f} seconds slower.')
