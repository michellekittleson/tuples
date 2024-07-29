'''
1. Tuple Mastery in Python

Task 1: Formatting Flight Itineraries

Create a Python function that takes a list of tuples as an argument. Each tuple contains information abouta flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is '[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]', the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
Itinerary 2: Bob - From Tokyo to San Francisco"

'''

itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

def formatted_itineraries(itineraries):
    for index, itinerary in enumerate(itineraries):
        traveler, origin, destination = itinerary
        print(f"Itinerary {index + 1}: {traveler} - From {origin} to {destination}")

formatted_itineraries(itineraries)

