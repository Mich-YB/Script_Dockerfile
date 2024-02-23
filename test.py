import datetime
def main():
    print("Hello world")
    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")
    print("Current date:", formatted_date)
    print("Current time:", formatted_time)
if __name__ == "__main__":
    main()
