class CustomException(Exception):
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)


events_list = [
    (2001, "Запуск Wikipedia"),
    (2000, "Винахід смартфонів"),
    (2004, "Запуск Facebook"),
    (2007, "Запуск iPhone"),
    (2010, "Запуск Instagram"),
    (2011, "Запуск Snapchat"),
    (2012, "Запуск SpaceX"),
    (2015, "Запуск Airbnb"),
    (2020, "Пандемія COVID-19"),
    (2021, "Запуск Perseverance на Марс")
]

visited_years = {}


def find_event_by_year(events_list, year):
    for event_year, event in events_list:
        if event_year == year:
            return event
    return None


def travel(selected_year):
    try:
        selected_year = int(selected_year)
        if selected_year in visited_years:
            raise CustomException(f"You've already visited the year {selected_year}")

        event_found = find_event_by_year(events_list, selected_year)
        if event_found:
            print(f"Event that happened in {selected_year}: {event_found}")
            visited_years[selected_year] = event_found
            print(visited_years)
        else:
            raise CustomException(f"No event found for the year {selected_year}")
    except ValueError:
        print("Invalid input. Please enter a valid year as a number.")
    except CustomException as e:
        print(f"Caught an exception: {e}")


print("Time Travel Machine Ready")

while True:
    selected_year = input("Choose a year to travel (or 'q' to quit): ")
    if selected_year.lower() == 'q':
        break
    travel(selected_year)
