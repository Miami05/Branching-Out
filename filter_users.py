import json

def filter_users_by_name(name):
    """Filter users by exact name (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with the name '{name}'.")


def filter_users_by_age(age):
    """Filter users by exact age (integer match)."""
    with open("users.json", "r") as file:
        users = json.load(file)
    
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid number for age.")
        return
    
    filtered_users = [user for user in users if user.get("age") == age]
    
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with the age {age}.")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Options: 'name', 'age'): ").strip().lower()
    
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    else:
        print("Filtering by that option is not yet supported.")
