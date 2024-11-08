from base_repository import BaseRepository

class Buyer(BaseRepository):
    def view_listing(self, car_id):
        increment_query = 'UPDATE used_cars SET view_count = view_count + 1 WHERE car_id = ?'
        self.execute_query(increment_query, (car_id,))
        query = 'SELECT * FROM used_cars WHERE car_id = ?'
        return self.fetch_one(query, (car_id,))

    def add_to_shortlist(self, buyer_id, car_id):
        check_query = 'SELECT * FROM shortlist WHERE car_id = ?'
        current_car = self.fetch_one(check_query, (car_id,))
        if current_car:
            return False
        query = '''INSERT INTO shortlist (buyer_id, car_id) VALUES (?, ?)'''
        self.execute_query(query, (buyer_id, car_id))
        return True
