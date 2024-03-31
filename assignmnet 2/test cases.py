from person import Person
from visitor import Visitor, VisitorType
from employee import Employee
from ticket import Ticket
from event import Event, EventType
from exhibition import Exhibition
from artwork import Artwork
from location import Location, LocationType
from datetime import date,timedelta
import random



def main():
    print("Welcome to the Museum Interactive System")
    user_type = input("Are you a visitor or an employee? (1) visitor / (2) employee): ").lower()

    if user_type in ["visitor", "1"]:
        handle_visitor_scenario()
    elif user_type in ["employee", "2"]:
        handle_employee_scenario()
    else:
        print("Invalid option selected. Exiting.")
def handle_visitor_scenario():
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        national_id = input("Please enter your national ID: ")
        email_id = input("Please enter your email ID: ")

        visitor = Visitor(name, age, national_id, email_id, VisitorType.ADULT)  # Default to ADULT for initial creation

        purchase_ticket = input("Do you want to purchase a ticket? (yes/no): ").lower()
        if purchase_ticket == "yes":
            num_tickets = int(input("How many tickets do you want to purchase? "))

            print("Please select the event:")
            for event_type in EventType:
                print(f"{event_type.name[0]}: {event_type.value}")
            event_letter = input().upper()
            event = {'A': EventType.ART_EXHIBITION, 'M': EventType.MUSIC_FESTIVAL, 'S': EventType.SCIENCE_CONFERENCE,
                     'F': EventType.FOOD_FAIR}.get(event_letter)

            if event is None:
                raise ValueError("Invalid event selected.")

            total_price = 0
            for i in range(num_tickets):
                print(f"Ticket {i + 1}: Please select the type of visitor:")
                for visitor_type in VisitorType:
                    print(f"{visitor_type.value[0]}: {visitor_type.value[1]}")
                type_of_visitor_input = int(input())
                if type_of_visitor_input not in range(1, 6):
                    raise ValueError("Invalid visitor type selected.")
                type_of_visitor = \
                {1: VisitorType.ADULT, 2: VisitorType.CHILD, 3: VisitorType.SENIOR, 4: VisitorType.TEACHER_STUDENT,
                 5: VisitorType.GROUP}[type_of_visitor_input]

                location = Location(
                    random.choice(list(LocationType)))  # Assuming location is selected randomly or predefined
                duration = random.randint(1, 5)  # Assuming duration is selected randomly or predefined

                ticket = Ticket(type_of_visitor, event, location.get_name(), duration)
                visitor.assign_ticket(ticket)
                total_price += ticket.get_price()

                event_object = Event(event)
                start_date = event_object.get_start_date()
                end_date = event_object.get_end_date()

             # Example dates, assuming Event class handles these parameters
            print(f"The total price for {num_tickets} tickets is {total_price} AED.")
            print(f"The event {event.value} will be held at {location.get_name()} from {event_object.start_date} to {event_object.end_date} for {duration} hours.")
            # Ticket Purchase Summary
            print("--- Ticket Purchase Summary ---")
            print(f"Name: {name}")
            print(f"Email: {email_id}")
            print(f"Number of Tickets: {num_tickets}")
            print(f"Event: {event.value}")
            print(f"Location: {location.get_name()}")
            print(f"Total Price: {total_price} AED")
        else:
            print("Thank you for visiting!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError:
        print("Invalid option selected. Exiting.")



added_artworks = []  # Initialize an empty list to store added artworks
def add_artwork_to_exhibition():
    try:
        global added_artworks  # Access the global list of added artworks

        print("Please select the event type:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None

        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return

        title = input("Please enter the artwork title: ")
        artist = input("Please enter the artist: ")
        year_of_creation = input("Please enter the year of creation: ")

        location_type = random.choice(list(LocationType))
        location = Location(location_type)

        historical_significance = input("Please enter the historical significance: ")

        artwork = Artwork(title, artist, year_of_creation, location, historical_significance)

        exhibition = Exhibition(event, location, date.today(), date.today())
        exhibition.add_artwork(artwork)
        added_artworks.append(artwork)  # Add the artwork to the list of added artworks
        print(f"Artwork {title} by {artist} created in {year_of_creation} added to {event.value} exhibition.")

    except Exception as e:
        print(f"An error occurred: {e}")


def remove_artwork_from_exhibition():
    try:
        global added_artworks  # Access the global list of added artworks

        print("Please select the event:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None

        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return

        title = input("Please enter the artwork title: ")

        location_type = random.choice(list(LocationType))
        location = Location(location_type)

        exhibition = Exhibition(event, location, date.today(), date.today())

        # Find and remove the artwork by title from the list of added artworks
        removed = False
        for artwork in added_artworks:
            if artwork.title == title:
                exhibition.remove_artwork(artwork)
                added_artworks.remove(artwork)
                removed = True
                break

        if removed:
            print(f"Artwork {title} removed from {event.value} exhibition.")
        else:
            print(f"No such artwork with title '{title}' found in the {event.value} exhibition.")

    except Exception as e:
        print(f"An error occurred: {e}")


def create_new_exhibition():
    try:
        print("Please select the event type:")
        print("(A) Art Exhibition")
        print("(M) Music Festival")
        print("(S) Science Conference")
        print("(F) Food Fair")

        event_letter = input().upper()
        event = None

        if event_letter == 'A':
            event = EventType.ART_EXHIBITION
        elif event_letter == 'M':
            event = EventType.MUSIC_FESTIVAL
        elif event_letter == 'S':
            event = EventType.SCIENCE_CONFERENCE
        elif event_letter == 'F':
            event = EventType.FOOD_FAIR
        else:
            print("Invalid option selected. Exiting.")
            return

        location_type = random.choice(list(LocationType))
        location = Location(location_type)

        start_date = date.today()
        end_date = date.today() + timedelta(days=30)

        exhibition = Exhibition(event, location, start_date, end_date)
        print(f"New {event.value} exhibition opened at {location.get_name()} from {start_date} to {end_date}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def display_added_artworks():
    if added_artworks:  # Check if there are any artworks added
        print("List of added artworks:")
        for artwork in added_artworks:
            print(f"Title: {artwork.title}, Artist: {artwork.artist}, Year: {artwork.year_of_creation}, Historical Significance: {artwork.historical_significance}")
    else:
        print("No artworks have been added yet.")

def handle_employee_scenario():
    try:
        employee_id = input("Please enter your Employee ID: ")
        employee_name = input("Please enter your name: ")

        continue_working = True

        while continue_working:
            print(f"\nEmployee ID: {employee_id}, Employee Name: {employee_name}")
            print("What would you like to do?")
            print("(1) Add artwork to an exhibition")
            print("(2) Remove artwork from an exhibition")
            print("(3) Open a new exhibition or event at the museum")
            print("(4) Display added artworks")  # New option to display artworks
            action = input()

            if action == "1":
                add_artwork_to_exhibition()
            elif action == "2":
                remove_artwork_from_exhibition()
            elif action == "3":
                create_new_exhibition()
            elif action == "4":
                display_added_artworks()  # Call the new function to display artworks
            else:
                print("Invalid option selected. Exiting.")
                break  # Exiting the loop

            # Ask the employee if they want to continue
            continue_choice = input("Do you want to continue? (yes/no): ").lower()
            continue_working = continue_choice == "yes"

        print("Thank you for your work today!")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()