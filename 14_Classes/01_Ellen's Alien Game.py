from helper import display_task_name, display_example

"""
Solution to Ellen's Alien Game exercise.
https://exercism.org/tracks/python/exercises/ellens-alien-game
"""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    x_coordinate: int
    y_coordinate: int
    health: int = 3

    total_aliens_created: int = 0

    def __init__(self, x_coordinates: int, y_coordinates: int):
        self.x_coordinate = x_coordinates
        self.y_coordinate = y_coordinates
        Alien.total_aliens_created += 1

    
    def hit(self):
        if self.health != 0:
            self.health -= 1
    

    def is_alive(self) -> bool:
        return self.health > 0

    
    def teleport(self, new_x_coordinates: int, new_y_coordinates: int) -> None:
        self.x_coordinate += new_x_coordinates
        self.y_coordinate += new_y_coordinates

    
    def collision_detection(self, object: object):
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(positions: list) -> list:
    return (Alien(position[0], position[1]) for position in positions)


# Task 1
display_task_name("I", "Create the Alien Class")

alien = Alien(2, 0)

print(alien.x_coordinate)
print(alien.y_coordinate)
print(alien.health, "\n")


# Task 2
display_task_name("II", "The hit Method")
alien.hit()
alien.hit()
print(alien.health, "\n")



# Task 3
display_task_name("III", "The is_alive Method")

print(alien.is_alive())
alien.hit()
alien.hit()
print(alien.health)
print(alien.is_alive(), "\n")



# Task 4
display_task_name("IV", "The teleport Method")
alien.teleport(5, -4)
print(alien.x_coordinate)
print(alien.y_coordinate, "\n")



# Task 5
display_task_name("V", "The collision_detection Method")
print(alien.collision_detection(object))



# Task 6
display_task_name("VI", "Alien Counter")
alien_one = Alien(5, 1)
print(alien_one.total_aliens_created)

alien_two = Alien(3, 0)
print(alien_two.total_aliens_created)

print(alien_one.total_aliens_created)

print(Alien.total_aliens_created)



# Task 7
display_task_name("VII", "Creating a List of Aliens")
alien_start_positions = [(4, 7), (-1, 0)]

aliens = new_aliens_collection(alien_start_positions)

for alien in aliens:
    	print(alien.x_coordinate, alien.y_coordinate)