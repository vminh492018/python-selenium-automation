
import os
def get_base_url():
    env = os.environ.get("ENV","test")
    if env.lower() == "test":
        return "http://vuminhutc.local/"
    elif env.lower() == "prod":
        return "http://vuminhutc.local/homepage/"
    else:
        raise Exception(f"Unknown enviroment: {env}")