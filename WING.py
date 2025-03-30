"""Calculating entry and exit angles"""
import math

GRAVITY = 9.80665
RADIANS = 2 * math.pi / 360


def get_input_float(prompt):
    """Getting input"""
    answers = []
    user_inputs = input(prompt).split()
    for user_input in user_inputs:
        answers.append(float(user_input))
    return answers


def calculate_distances(angles, speeds):
    """Calculating Distances"""
    distances = []
    for i in range(len(angles)):
        y_speed = speeds[i] * math.sin(angles[i] * RADIANS)
        x_speed = speeds[i] * math.cos(angles[i] * RADIANS)

        time_of_flight = 2 * y_speed / GRAVITY
        distance = x_speed * time_of_flight

        distances.append(distance)
    return distances


def best_distance(distances):
    """Location of best achieved distance"""
    best_distance_index = 0
    for i in range(len(distances)):
        if distances[i] > distances[best_distance_index]:
            best_distance_index = i
    return best_distance_index


def print_results(distances, best_distance_index):
    """Print the results"""
    n = len(distances)
    print(f"The catapult was fired {n} times.")
    longest_distance = distances[best_distance_index]
    print(f"Shot #{best_distance_index + 1} had the best distance of "
          f"{longest_distance:.2f} m")


def main():
    """Given the exit angles and speeds measured from a catapult over multiple
       firings. Calculates which shot travelled the farthest.
       Input for the angles and speeds should be given in white-space separated
       lists.
    """
    angle_strings = get_input_float("Input release angles (degrees): ")
    initial_speed_strings = get_input_float("Input release speeds (m/s): ")

    distances = calculate_distances(angle_strings, initial_speed_strings)
    best_distance_index = best_distance(distances)
    print_results(distances, best_distance_index)



main()
