from base_repository import BaseRepository

class UsedCar(BaseRepository):
    def get_all_cars(self):
        query = 'SELECT * FROM used_cars'
        return self.fetch_all(query)

# Entity
    def create_car(self, make, model, year, price, description, agent_id, seller_id):
        query = '''
            INSERT INTO used_cars (make, model, year, price, description, agent_id, seller_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.execute_query(query, (make, model, year, price, description, agent_id, seller_id))
        return True  # Return True to indicate success


    def update_car(self, car_id, make, model, year, price, description, seller_id):
        query = '''
            UPDATE used_cars 
            SET make = ?, model = ?, year = ?, price = ?, description = ?, seller_id = ? 
            WHERE car_id = ?
        '''
        self.execute_query(query, (make, model, year, price, description, seller_id, car_id))
        return True

