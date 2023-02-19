# 1. return a message with name
def badge_maker(name):
    return f"Hello, my name is {name}."

#  2. takes a list of names as an argument and returns a list of badge messages
def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

#  3. takes the list of speakers and assigns each speaker to a room
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]

#  4. 
def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)
