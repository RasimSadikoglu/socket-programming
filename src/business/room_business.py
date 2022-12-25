from lib.database import Database

class RoomBusiness:
    
    def add(self, name: str) -> bool:
        result = Database().set(name, "")
        return (200 if result else 403, {"result": result})
    
    def remove(self, name: str) -> bool:
        result = Database().delete(name)
        return (200 if result else 403, {"result": result})