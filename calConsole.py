from calCursor import CalCursor
import datetime

class CalConsole:
    help_menu = """
        week|month|day int: alters week, month or day from given on int
        stop: exit console
        get week|month|day: gets data for week, month or day and prints it
        time: prints current cursor time 
    """
    def __init__(self):
        self.cursor = CalCursor()
    

    def run(self):
        print("Enter command")
        command = ""
        while command != "stop":
            command = input().lower()
            tokens = list(command.split())
            if tokens[0] == "week" or tokens[0] == "month" or tokens[0] == "day":
                try:
                    tokens[1] = int(tokens[1])
                except ValueError:
                    print("Please enter correct command")
                    continue
            
            match tokens[0]:
                case "week":
                    self.cursor.alter_week(tokens[1])
                case "month":
                    self.cursor.alter_month(tokens[1])
                case "day":
                    self.cursor.alter_day(tokens[1])
                case "get":
                    if tokens[1] == "week":
                        print(self.cursor.get_data_for_week(), sep='\n')
                    elif tokens[1] == "month":
                        print(self.cursor.get_data_for_month(), sep='\n')
                    elif tokens[1] == "day":
                        print(self.cursor.get_data_for_day(), sep='\n')
                case "time":
                    print(self.cursor)
                case "event":
                    if tokens[1] == "add":
                        self.add_event()
                    elif tokens[1] == "delete":
                        self.delete_event()
                case "stop":
                    print("Shutting down")
                    break
                case _:
                    print(self.help_menu)


    def add_event(self):
        print("Enter name, start datetime, end datetime, location(can be blank)")
        name = input()
        start_datetime = self.accept_datetime_input()
        end_datetime = self.accept_datetime_input()
        loc = input()
        if self.cursor.add_event(name, start_datetime, end_datetime, loc):
            print("Added succesfully")
        else:
            print("Something went wrong")
    

    def delete_event(self):
        pass
    
    def accept_datetime_input(self) -> datetime.datetime:
        while 1:
            input_data = map(int, input().split())
            try:
                result = datetime.datetime(*input_data)
                return result
            except ValueError as VE:
                print(f'Datetime that you have entered isn\' correct because {VE}. Please repeat your input')



cons = CalConsole()
cons.run()

