"""
CP1404 - PRACTICAL 07
"""
import datetime


class Project:
    """a"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """a"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """a"""
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}")

    def __lt__(self, other):
        """a"""
        return self.priority < other.priority

    def update_project(self, priority, completion_percentage):
        """a"""
        self.priority = priority
        self.completion_percentage = completion_percentage

    def is_completed(self):
        """"""
        return self.completion_percentage > 0

if __name__ == "__main__":
    # various tests
    eat_dinner = Project("Eat Dinner", datetime.date(2020, 1, 1), 10, 100, 10)
    clean_room = Project("Clean Room", datetime.date(2020, 1, 1), 1, 0, 10)
    print(eat_dinner)
    print(clean_room)
    eat_dinner.update_project(10,  100)
    print(eat_dinner)
    print(clean_room < eat_dinner)
    print(clean_room.is_completed())