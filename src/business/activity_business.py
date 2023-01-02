from lib.database import Database
from lib.html_result import HTMLResult

class ActivityBusiness:
    def add(self, name: str):
        if name == "":
            return HTMLResult(400, 'Error', 'Please enter a activity name.')

        result = Database().get(f'{name}_activity')
        if result is not None:
            return HTMLResult(403, 'Error', 'Activity already exists.')
        
        Database().set(f'{name}_activity', "")

        return HTMLResult(200, 'Activity Added', f'Activity with name "{name}" is successfully added.')

    def remove(self, name: str):
        result = Database().get(f'{name}_activity')
        if result is None:
            return HTMLResult(403, 'Error', 'Activity does not exist.')

        Database().delete(f'{name}_activity')
        
        return HTMLResult(200, 'Activity Removed', f'Activity with name "{name}" is successfully removed.')

    def check(self, name: str):
        result = Database().get(f'{name}_activity')

        if result is None:
            return HTMLResult(403, 'Error', 'Activity does not exist.')

        return HTMLResult(200, 'Activity', f'Activity with name "{name}" does exist.')