filename = "data.bin"


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

format_maps = {
                "phone": "any ukrainian number",
                "email": "any email format",
                "birthday": "any data format in this sequence: dd,mm, yyyy",
                "address": "free",
            }

available_options = {
    "add":
        {
            "contact": True, 
            "phone": True, 
            "email": True, 
            "birthday": True, 
            "address": True, 
            "note": True,
            "tags": True
        },
    "edit":
        {
            "contact": False, 
            "phone": True,  
            "email": True,  
            "birthday": True,  
            "address": True,  
            "note": True, 
            "tags": False
        },
    "delete": 
        {
            "contact": True, 
            "phone": True,  
            "email": True,  
            "birthday": True,  
            "address": True,  
            "note": True, 
            "tags": False
        }
    }

