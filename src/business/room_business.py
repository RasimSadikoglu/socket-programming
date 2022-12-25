from lib.database import Database

class RoomBusiness:
    
    def add(self, name: str) -> bool:
        return Database().set(name, "")