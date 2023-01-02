from lib.database import Database
from lib.html_result import HTMLResult

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class RoomBusiness:
    
    def add(self, name: str) -> HTMLResult:
        if name == "":
            return HTMLResult(400, 'Error', 'Please enter a room name.')

        result = Database().get(f'{name}_room')
        if result is not None:
            return HTMLResult(403, 'Error', 'Room already exists.')
        
        Database().set(f'{name}_room', "")
        for i in range(1, 8):
            Database().set(f'{name}_room_day{i}', "000000000")

        return HTMLResult(200, 'Room Added', f'Room with name "{name}" is successfully added.')
    
    def remove(self, name: str) -> HTMLResult:
        result = Database().get(f'{name}_room')
        if result is None:
            return HTMLResult(403, 'Error', 'Room does not exist.')

        Database().delete(f'{name}_room')
        for i in range(1, 8):
            Database().delete(f'{name}_room_day{i}')
        
        return HTMLResult(200, 'Room Removed', f'Room with name "{name}" is successfully removed.')
    
    def reserve(self, name: str, day: int, hour: int, duration: int):
        if Database().get(f'{name}_room') is None:
            return HTMLResult(404, 'Error', f'Room with name "{name}" does not exist.')
        if not (1 <= day <= 7):
            return HTMLResult(400, 'Error', 'Day value should be between 1 and 7.')
        if not (9 <= hour <= 17):
            return HTMLResult(400, 'Error', 'Hour value should be between 9 and 17.')
        if duration < 1:
            return HTMLResult(400, 'Error', 'Duration has to be positive.')
        if hour + duration > 18:
            return HTMLResult(403, 'Error', 'Reservations cannot be made after 18.00.')

        availability = list(Database().get(f'{name}_room_day{day}').decode())

        if availability[hour - 9: hour - 9 + duration] != ['0'] * duration:
            return HTMLResult(403, 'Error', 'Room already reserved.')

        availability[hour - 9: hour - 9 + duration] = ['1'] + (['2'] * (duration - 1))

        Database().set(f'{name}_room_day{day}', ''.join(availability))
        
        return HTMLResult(200, 'Room Reserved', f'Room {name} is reserved on {DAYS[day - 1]} hours between {hour}.00 and {hour + duration}.00.')

    def check_availability(self, name: str, day: int):
        if Database().get(f'{name}_room') is None:
            return HTMLResult(404, 'Error', f'Room with name "{name}" does not exist.')
        if not (1 <= day <= 7):
            return HTMLResult(400, 'Error', 'Day value should be between 1 and 7.')
        
        availability = list(zip(Database().get(f'{name}_room_day{day}').decode(), range(9, 18)))
        availability = list(filter(lambda x: x[0] == '0', availability))
        availability = map(lambda x: str(x[1]), availability)

        return HTMLResult(200, 'Available Hours', f'On {DAYS[day - 1]} Room {name} is available for the following hours: {" ".join(availability)}')