from firebase import firebase


def get_timetable_plawecki(direction):
    timetable = firebase.FirebaseApplication(
        'https://timetable-plawecki-default-rtdb.europe-west1.firebasedatabase.app/', None)
    if direction == '3':
        return timetable.get('/', None)
    else:
        return timetable.get('/', direction)

