from base_repository import BaseRepository

class UserProfile(BaseRepository):
    def get_all_profiles(self):
        query = 'SELECT * FROM user_profiles'
        return self.fetch_all(query)

    def create_profile(self, role, status, description):
        # Check if a profile with the same role already exists
        check_query = 'SELECT * FROM user_profiles WHERE role = ?'
        existing_profile = self.fetch_one(check_query, (role,))
        if existing_profile:
            return False  # Role already exists

        # Proceed with profile creation
        query = 'INSERT INTO user_profiles (role, status, description) VALUES (?, ?,?)'
        self.execute_query(query, (role, status, description))
        return True

