# Duke pasur parasysh një sërë intervalesh kohore takimesh
# që përbëhen nga orët e fillimit dhe të përfundimit [ [s1 , e1 ] , [ s2 , e2 ] ,... ] (si< ei),
# gjeni numrin minimal të sallave të konferencave të nevojshme.
def minMeetingRooms(intervals):
    events = []  # Lista për të gjitha ngjarjet (fillime dhe mbarime takimesh)

    for start, end in intervals:
        events.append((start, 1))  # Shto fillimin e takimit (+1 sallë)
        events.append((end, -1))  # Shto mbarimin e takimit (-1 sallë)

    events.sort()  # Rendisim ngjarjet sipas kohës

    max_rooms = 0
    current_rooms = 0

    for _, event in events:
        current_rooms += event  # Shtojmë ose heqim sallat aktive
        max_rooms = max(max_rooms, current_rooms)  # Përditësojmë numrin maksimal të sallave

    return max_rooms

intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))


intervals2 = [[7, 10], [2, 4]]
print(minMeetingRooms(intervals2))

intervals3 = [[1, 5], [2, 6], [8, 9]]
print(minMeetingRooms(intervals3))       