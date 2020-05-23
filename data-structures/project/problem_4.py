import unittest

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
    if user in group.get_users():
        return True
    
    for internal_group in group.get_groups():
        if is_user_in_group(user, internal_group):
            return True
    
    return False

class problem_4_tests(unittest.TestCase):

    def test1(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)
        self.assertTrue(is_user_in_group("sub_child_user", parent))
        self.assertFalse(is_user_in_group("not_sub_child_user", parent))

    def test2(self):
        """
        A (1 2 3)
            B (4 5 6)
                C (7 8 9)
                D (10 11 12)
                    E (13 14 15)
            F (16 17 18)
        """
        a = Group("A")
        a.add_user("1")
        a.add_user("2")
        a.add_user("3")
        b = Group("B")
        a.add_group(b)
        b.add_user("4")
        b.add_user("5")
        b.add_user("6")
        c = Group("C")
        b.add_group(c)
        c.add_user("7")
        c.add_user("8")
        c.add_user("9")
        d = Group("D")
        b.add_group(d)
        d.add_user("10")
        d.add_user("11")
        d.add_user("12")
        e = Group("E")
        d.add_group(e)
        e.add_user("13")
        e.add_user("14")
        e.add_user("15")
        f = Group("F")
        a.add_group(f)
        f.add_user("16")
        f.add_user("17")
        f.add_user("18")
        for i in range(1, 19):
            self.assertTrue(is_user_in_group(str(i), a))
        self.assertFalse(is_user_in_group("0", a))
        for i in range(4, 16):
            self.assertTrue(is_user_in_group(str(i), b))
        self.assertFalse(is_user_in_group("1", b))
        self.assertFalse(is_user_in_group("2", b))
        self.assertFalse(is_user_in_group("3", b))

    def test3(self):
        parent = Group("A")
        self.assertFalse(is_user_in_group("not_sub_child_user", parent))

if __name__ == '__main__':
    unittest.main()