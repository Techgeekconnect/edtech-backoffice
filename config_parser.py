import json
import os


def parse_file(file_name):
    try:
        with open(file_name,"r",encoding="utf-8") as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            return data
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    directory=os.path.abspath("server_config.json")
    config = parse_file(directory)
    print(config)
    if not config:
        raise RuntimeError("Unable to find server_config.json file")