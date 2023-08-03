import json

def data_r(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def get_weather(data, date):
    for item in data["list"]:
        if item["dt_txt"].split()[0] == date:
            return item["main"]["temp"]

    return "Data not available"


def get_windspeed(data, date):
    for item in data["list"]:
        if item["dt_txt"].split()[0] == date:
            return item["wind"]["speed"]

    return "Data not available"


def get_pressure(data, date):
    for item in data["list"]:
        if item["dt_txt"].split()[0] == date:
            return item["main"]["pressure"]

    return "Data not available"


def main():
    file_path = "Weather.json"  # Replace with the actual path of your JSON file
    data = data_r(file_path)

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_weather(data, date)
            print(f"Temperature on {date}: {temp}°C")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_windspeed(data, date)
            print(f"Wind Speed on {date}: {wind_speed} km/h")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(data, date)
            print(f"Pressure on {date}: {pressure} hPa")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

