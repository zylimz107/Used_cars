from user_profile import UserProfile

class ViewProfileController:
    def __init__(self):
        # Initialize the UserProfile entity, which interacts with the database
        self.user_profile_entity = UserProfile()

    def view_profiles(self):
        # Retrieve all user profiles from the entity and display them in the 'profiles.html' template
        return self.user_profile_entity.get_all_profiles()
    
class CreateProfileController:
    def __init__(self):
        self.user_profile_entity = UserProfile()

    def create_profile(self, profile_data):
        # Call entity to create the profile with provided data
        return self.user_profile_entity.create_profile(
            role=profile_data['role'],
            status=profile_data['status'],
            description=profile_data['description']
        )

