# Kemi një hotel me n dhoma (rooms). Dhomat pëfaqësohen nga një varg 2D i tipit integer me emrin rooms
# ku rooms[i] = [roomIdi, sizei] tregon se ka një dhomë me numrin e
# dhomës roomId dhe madhësinë e barabartë me size. Secila roomId është unike.
# Gjithashtu kemi k pyetje/kerkesa (queries) në një varg 2D me emrin queries ku
# queries[j] = [preferredj, minSizej]. Përgjigjja për kërkesen/pyetjen (query) e jth
# është numri i dhomës id të një dhome të tillë që:
# Dhoma ka një madhësi prej të paktën minSizej, dhe abs(id - preferredj) është
# minimizuar, ku abs(x) është vlera absolute e x. Nëse ka një barazim në diferencën
# absolute, atëherë përdorni dhomën me më të voglën id. Nëse nuk ka dhomë të tillë,
# përgjigjja është -1.
# Ktheni një varg answer të gjatësisë k ku answer[j] ka/përmban pëgjigjjen e pyetjes
# (query) jth.

def closest_room(rooms, queries):
    # Rendit dhomat sipas roomId
    rooms.sort()

    # Përgatit përgjigjet
    answer = []

    for preferred, min_size in queries:
        # Filtro dhomat që kanë madhësi të paktën min_size
        filtered_rooms = [room for room in rooms if room[1] >= min_size]

        if not filtered_rooms:
            # Nëse nuk ka dhoma të përshtatshme, shto -1
            answer.append(-1)
        else:
            # Gjej dhomën më të afërt në terma të |roomId - preferred|
            min_diff = float('inf')
            best_room = -1

            for room in filtered_rooms:
                room_id, size = room
                diff = abs(room_id - preferred)

                if diff < min_diff or (diff == min_diff and room_id < best_room):
                    min_diff = diff
                    best_room = room_id

            answer.append(best_room)

    return answer


# Shembull përdorimi
rooms = [[2, 2], [1, 4], [3, 3], [5, 6]]
queries = [[3, 2], [4, 3], [6, 5]]
print(closest_room(rooms, queries))  # Output: [3, 3, 5]