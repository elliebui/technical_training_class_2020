class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():  # Time complexity: O(N)
        return True
    for sub_group in group.get_groups():  # Time complexity: O(N)
        if is_user_in_group(user, sub_group):   # Time complexity: O(N)
            return True

    return False

# Total time complexity: O(N^2)


group_1 = Group("g1")
group_2 = Group("g2")
group_3 = Group("g3")

user_3 = "u3"
group_3.add_user(user_3)

user_2 = "u2"

user_1 = "u1"
group_1.add_user(user_1)

group_1.add_group(group_2)
group_1.add_group(group_3)

print(is_user_in_group(user_1, group_1))  # True
print(is_user_in_group(user_2, group_1))  # False
print(is_user_in_group(user_3, group_1))  # True
