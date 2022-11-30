from typing import Dict, List, ClassVar, Tuple
from project.user import User


class Library:
    user_records: ClassVar[List[User]] = []
    books_available: ClassVar[Dict[str, List[str]]] = {}
    rented_books: ClassVar[Dict[str, Dict[str, int]]] = {}
    rented_books_by_book_name: ClassVar[Dict[str, Tuple[str, int]]] = {}

    def add_user(self, user: User):
        if user in self.user_records: #NOTE
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)
        # else:
        #     self.user_records.remove(user.username)


    def change_username(self, user_id: int, new_username: str):
        # usernames = [name.username for name in self.user_records]
        users_ids = [u.user_id for u in self.user_records]
        if user_id not in users_ids:
            return f"There is no user with id = {user_id}!"

        user = self.user_records[users_ids.index(user_id)]
        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        # NOTE: should we update other collections
        user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"