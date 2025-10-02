from pprint import pprint

from dataset import randomuser_data


def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    names = []

    for user in data['results']:
        name = user['name']

        full_name = f"{name['first']} {name['last']}"

        names.append(full_name)

    return names


def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """
    filtered_users = []

    for user in data['results']:
        if user['location']['country'].lower() == country.lower():
            result = {
                "name": f"{user['name']['first']} {user['name']['last']}",
                "email": user['email']
            }
            filtered_users.append(result)
    
    return filtered_users


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    result = {'male': 0, 'female': 0}

    for user in data['results']:
        if user['gender'] == 'male':
            result['male'] += 1
        elif user['gender'] == 'female':
            result['female'] += 1

    return result


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    emails = []

    for user in data['results']:

        if user['dob']['age'] > age:
            emails.append(user['email'])  

    return emails  



# 5- functionni tushunmadim
def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    pass




def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    usernames = []

    for user in data['results']:
        username = user['login']['username']
        if username.lower().startswith(letter.lower()):
            usernames.append(username)

    return usernames


def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    total_age = 0
    count = 0

    for user in data['results']:
        total_age += user['dob']['age']
        count += 1
        
        average_age = total_age / count
        
        if count > 0:
            return average_age
        else:
            return 0.0
        


#  8- functionni tushunmadim
def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    pass




def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    coordinates = []

    for user in data['results']:
        lat = user['location']['coordinates']['latitude']
        lon = user['location']['coordinates']['longitude']

        coordinates.append((lat, lon))

    return coordinates


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    first_user = data['results'][0]
    max_age = first_user['dob']['age']
    oldest_user = None

    for user in data['results'][1:]:
        age = user['dob']['age']
        if age > max_age:
            max_age = age
            oldest_user = {
                "name": f"{user['name']['first']} {user['name']['last']}",
                "age": age,
                "email": user['email']
            }

    return oldest_user


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    users_in_timezone = []
    
    for user in data['results']:
        if user['location']['timezone']['offset'] == offset:
            users_in_timezone.append({
                "name": f"{user['name']['first']} {user['name']['last']}",
                "city": user['location']['city']
            })

    return users_in_timezone




# 12 - functionni tushunmadim
def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    pass
