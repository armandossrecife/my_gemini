from datetime import datetime

class Tempo():
    def __init__(self):
        pass
    
    def get_current_date_and_time(self):
        # Get the current date and time
        now = datetime.now()
        # Format the date and time as a string (e.g., "2023-10-25_14-30-45")
        valor = now.strftime("%Y-%m-%d_%H-%M-%S")
        return valor                     