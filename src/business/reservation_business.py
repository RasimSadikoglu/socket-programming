from clients.activity_client import ActivityClient
from clients.room_client import RoomClient
from lib.database import Database
from lib.html_result import HTMLResult

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class ReservationBusiness:
    def reserve(self, room: str, activity: str, day: int, hour: int, duration: int):
        activity_check = ActivityClient().check(activity)
        if activity_check.status != 200:
            return activity_check

        reserve_room = RoomClient().reserve(room, day, hour, duration)
        if reserve_room.status != 200:
            return reserve_room

        reservation_id = Database().get_new_id()
        reservation_info = f'Reservation ID: {reservation_id}<br>Room: {room}<br>Activity: {activity}<br>When: {DAYS[day - 1]} {hour}.00 - {hour + duration}.00.'

        Database().set(reservation_id, reservation_info)

        return HTMLResult(200, 'Reservation Successful', f'Room {room} is reserved for activity {activity} on {DAYS[day - 1]} {hour}.00 - {hour + duration}.00. Your Reservation ID is {reservation_id}.')

    def list_availability(self, room: str, day: int = 0):
        results = []

        for d in range(1, 8):
            if day == 0 or day == d:
                results.append(RoomClient().check_availability(room, d))

            if results and results[-1].status != 200:
                return results[-1]
        
        body = ""
        for r in results:
            body += "<li>" + r.body + "</li>"

        return HTMLResult(200, 'Availability', body)

    def display(self, id: int):
        reservation = Database().get(id)
        if reservation is None:
            return HTMLResult(404, 'Error', 'No reservation is found with id {id}.')

        return HTMLResult(200, 'Reservation Info', reservation.decode())