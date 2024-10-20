"""
CP1404 PRAC 05
Wimbledon exercise
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Program that reads, processes and displays data from csv file"""
    print("Wimbledon Champions:")
    champion_records = get_records(FILENAME)
    champion_to_win_count, countries = process_data(champion_records)
    display(champion_to_win_count, countries)


def get_records(filename):
    """Creates a list of records from a CSV file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """Creates a dictionary of champions and set of winning countries"""
    winner_to_win_data = {}
    countries = set()
    for record in records:
        try:
            winner_to_win_data[record[CHAMPION_INDEX]] += 1
        except KeyError:
            winner_to_win_data[record[CHAMPION_INDEX]] = 1
        countries.add(record[COUNTRY_INDEX])
    return winner_to_win_data, countries


def display(champion_to_win_count, countries):
    """Displays formatted information"""
    for champion, wins in champion_to_win_count.items():
        print(f"{champion} {wins}")
    print() # Add blank space for readability
    print("These countries have won wimbledon:")
    print(", ".join(country for country in countries))


main()
