from lib.database import Database

class RoomBusiness:
    
    def add(self, name: str) -> bool:
        result = Database().set(name, "")
        return (200 if result else 403, {"message": f"Room with name {name} is added." if result else "Room already exists."})
    
    def remove(self, name: str) -> bool:
        result = Database().delete(name)
        return (200 if result else 403, {"message": f"Room with name {name} is removed." if result else "Room with the given name does not exist."})
    
    def reserve(self, name: str, day: int, hour: int, duration: int):
        if not (1 <= day <= 7):
            return (400, {"message": "Day value should be between 1 and 7."})
        if not (9 <= hour <= 17):
            return (400, {"message": "Hour value should be between 9 and 17."})
        if Database().get(name) is None:
            return (404, {"message": f"Room with name {name} does not exist."})