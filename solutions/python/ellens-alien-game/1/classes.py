"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    # Class attribute
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3  # default health
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self):
        """Return True if health > 0, else False."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Implementation TBD (should return None for now)."""
        pass  # IMPORTANT: do not return anything


# Function to create multiple Alien objects
def new_aliens_collection(coordinates_list):
    """Create a list of Alien objects from a list of coordinates."""
    aliens = []
    for x, y in coordinates_list:
        aliens.append(Alien(x, y))
    return aliens


# Example usage
if __name__ == "__main__":
    coords = [(1, 2), (3, 4), (5, 6)]
    aliens = new_aliens_collection(coords)

    for alien in aliens:
        print(f"Alien at ({alien.x_coordinate}, {alien.y_coordinate}) with health {alien.health}")

    print("Total aliens created:", Alien.total_aliens_created)