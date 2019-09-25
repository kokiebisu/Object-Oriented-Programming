class Team:
    """
    Team the implements 'sized' protocols
    """

    def __init__(self, team_name, team_members):
        """
        Initializes a team with the given name and members
        :param team_name: a string
        :param team_members: a list
        """
        self.name = team_name
        self.members = team_members

    def __str__(self):
        team_list = ""
        for person in self.members:
            team_list += person + " "
        return f"Team: {self.name}\nMembers: {team_list}"

    # Reserved method in Python to return the length
    def __len__(self):
        return len(self.members)

    def __contains__(self, item):
        """Should return true if the name of the person is in the team list"""
        return item in self.members

    def __iter__(self):
        """Implements the iterable protocol"""
        return iter(self.members)


def main():
    x_men = Team("X-Men", ["Professor Xavier", "Cyclops", "Storm",
                           "Jean"])
    print(x_men)
    print(f"Number of members: {len(x_men)}")  # x_men.__len__()
    print(f"Is cyclops part of the X-men? {'cyclops' in x_men}") # x_men.__contains__('cyclops')


if __name__ == '__main__':
    main()
