"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)




# Test 1
# ghost does not get eaten because no power pellet active
print("GhostGobbleGame > ghost does not get eaten because no power pellet active")
print(eat_ghost(False, True), "\n")

# Test 2
# GhostGobbleGame > ghost does not get eaten because not touching ghost
print("GhostGobbleGame > ghost does not get eaten because not touching ghost")
print(eat_ghost(True, False), "\n")

# Test 3
# GhostGobbleGame > ghost gets eaten
print("GhostGobbleGame > ghost gets eaten")
print(eat_ghost(True, True), "\n")


# Test 4
# GhostGobbleGame > no score when nothing eaten
print("GhostGobbleGame > no score when nothing eaten")
print(score(False, False), "\n")

# Test 5
# GhostGobbleGame > score when eating dot
print("GhostGobbleGame > score when eating dot")
print(score(False, True), "\n")

# Test 6
# GhostGobbleGame > score when eating power pellet
print("GhostGobbleGame > score when eating power pellet")
print(score(True, False), "\n")


# Test 7
# GhostGobbleGame > dont lose if not touching a ghost
print("GhostGobbleGame > dont lose if not touching a ghost")
print(lose(True, False), "\n")

# Test 8
# GhostGobbleGame > dont lose if touching a ghost with a power pellet active
print("GhostGobbleGame > dont lose if touching a ghost with a power pellet active")
print(lose(True, True), "\n")

# Test 9
# GhostGobbleGame > lose if touching a ghost without a power pellet active
print("GhostGobbleGame > lose if touching a ghost without a power pellet active")
print(lose(False, True), "\n")


# Test 10
# GhostGobbleGame > dont win if all dots eaten but touching a ghost
print("GhostGobbleGame > dont win if all dots eaten but touching a ghost")
print(win(True, False, True), "\n")

# Test 11
# GhostGobbleGame > dont win if not all dots eaten
print("GhostGobbleGame > dont win if not all dots eaten")
print(win(False, True, True), "\n")

# Test 12
# GhostGobbleGame > win if all dots eaten
print("GhostGobbleGame > win if all dots eaten")
print(win(True, False, False), "\n")

# Test 13
# GhostGobbleGame > win if all dots eaten and touching a ghost with a power pellet active
print("GhostGobbleGame > win if all dots eaten and touching a ghost with a power pellet active")
print(win(True, True, True), "\n")