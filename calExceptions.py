class ServiceIsNoneError(Exception):
    def __str__(self):
        return "Auth had never been completed"

    def __repr__(self):
        return "Auth had never been completed"

class ServiceAuthFailedError(Exception):

    def __str__(self):
        return "Failed to connect to Google Calendar"
    
    def __repr__(self):
        return "Failed to connect to Google Calendar"