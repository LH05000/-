import pandas as pd

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.df = self.load_users_from_excel()

    def load_users_from_excel(self):
        try:
            # 使用openpyxl作为引擎读取.xlsx文件
            return pd.read_excel(self.filename, engine='openpyxl')
        except FileNotFoundError:
            # 如果文件不存在，创建一个空的DataFrame
            return pd.DataFrame(columns=["ID", "Name", "Age"])
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame(columns=["ID", "Name", "Age"])

    def save_users_to_excel(self):
        # 使用openpyxl作为引擎保存.xlsx文件
        self.df.to_excel(self.filename, index=False, engine='openpyxl')

    def add_user(self, user):
        # 使用concat函数将新用户添加到现有的DataFrame中
        new_row = pd.DataFrame([user], columns=["ID", "Name", "Age"])
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        print(f"Added user: {user}")
        self.save_users_to_excel()

    def remove_user(self, user_id):
        self.df = self.df[self.df['ID'] != user_id]
        print(f"Removed user with ID: {user_id}")
        self.save_users_to_excel()

    def update_user(self, user_id, new_name=None, new_age=None):
        index = self.df.index[self.df['ID'] == user_id].tolist()
        if index:
            if new_name:
                self.df.at[index[0], 'Name'] = new_name
            if new_age:
                self.df.at[index[0], 'Age'] = new_age
            print(f"Updated user with ID: {user_id}")
            self.save_users_to_excel()
        else:
            print("User not found.")

    def get_user(self, user_id):
        user = self.df[self.df['ID'] == user_id]
        if not user.empty:
            print(f"Found user:\n{user}")
            return user
        else:
            print("User not found.")
            return None

    def display_all_users(self):
        if not self.df.empty:
            print("All Users:")
            print(self.df)
        else:
            print("No users to display.")


def main():
    manager = UserManager("users.xlsx")

    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Remove User")
        print("3. Update User")
        print("4. Get User")
        print("5. Display All Users")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter user ID: ")
            name = input("Enter user name: ")
            age = int(input("Enter user age: "))
            manager.add_user({'ID': id, 'Name': name, 'Age': age})

        elif choice == "2":
            id = input("Enter user ID to remove: ")
            manager.remove_user(id)

        elif choice == "3":
            id = input("Enter user ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            manager.update_user(id, name if name else None, age if age else None)

        elif choice == "4":
            id = input("Enter user ID to get: ")
            manager.get_user(id)

        elif choice == "5":
            manager.display_all_users()

        elif choice == "6":
            manager.save_users_to_excel()  # 确保退出前保存数据
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()