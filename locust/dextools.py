import os, json

def read_file():
    try:
        with open((os.environ['PYTHONPATH'].split(os.pathsep))[-1] + '/tests/settings/config.json', "r") as data_file:
            datas = data_file.read()
            data_file.close()
            return datas
    except Exception as err:
        print(err)
        return False

def write_file(stringJSON):
    try:
        with open((os.environ['PYTHONPATH'].split(os.pathsep))[-1] + '/tests/settings/config.json', "w") as data_file:
            datas = data_file.write(stringJSON)
            return True, 'JSON saved'
    except Exception as err:
        print(err)
        return False, err
