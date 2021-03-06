import importlib
import pkgutil
from pathlib import Path
import argparse
import importlib.util
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_json_schema import JsonSchema, JsonValidationError

# import scripts

####################################################################################
# config
####################################################################################
PORT = 5000
HOST = '127.0.0.1'

app = Flask(__name__)
####################################################################################
# Cors
####################################################################################
# Allows access to fetch at 'http://localhost:5000/' from origin 'app://obsidian.md'
obsidian_origin = "app://obsidian.md"
cors = CORS(app, origins=obsidian_origin)
app.config['CORS_HEADERS'] = 'Content-Type'

####################################################################################
# Schema
####################################################################################
# Input schema example:
# {
#   vaultPath: "/home/cvasquez/obsidian/development", 
#   notePath: "snippets-plugin/Test1.md"
#   text: "Some selected text", 
# }
validator = JsonSchema(app)
input_schema = {
    'required': ['vaultPath'],
    'properties': {
        'vaultPath': {'type': 'string'},
        'notePath': {'type': 'string'},
        'text': {'type': 'string'},
        'script': {'type': 'string'},
    }
}


@app.errorhandler(JsonValidationError)
def validation_error(e):
    error = {
        'message': e.message,
        'status': 400,
        'errors': [validation_error.message for validation_error in e.errors]
    }
    return jsonify(error)

####################################################################################
# Routers
####################################################################################
'''Return a list of all detected plugins'''

@app.route('/', methods=['GET'])
def root():

    urls = []

    for path in Path(scripts_path).glob('*.py'):
        module_name = str(path.name)[:-3]
        urls.append(f'http://{HOST}:{PORT}/{module_name}')

    return {
        'scripts': urls
    }


'''Exposes a script present in the scripts folder

The url corresponds to the path to the file, without the 'py' part.

For example, if there is a script:

./scripts/hello_world.py, 

It will be exposed in without the py part at:

http://{HOST}:{PORT}/{SCRIPTS_FOLDER}/hello_world

'''

@app.route('/<plugin>', methods=['POST'])
@validator.validate(input_schema)
def execute_script(plugin):
    vault_path = request.json['vaultPath'] if 'vaultPath' in request.json else None

    absolute_path = os.path.join(scripts_path, f'{plugin}.py')

    def exec_spec(spec):
        plugin = spec.Plugin(vault_path=vault_path)
        return plugin.execute(request.json)

    try:
        spec = load_spec(plugin, absolute_path)
        return exec_spec(spec)
    except Exception as e:
        return {
            'message': str(e),
            'status': 500,
            'errors': [str(e)]
        }


@app.route('/<plugin>', methods=['GET'])
def get_code(plugin):

    absolute_path = os.path.join(scripts_path, f'{plugin}.py')

    return {
        "supportedOperation": [
            {
                "@type": "Operation",
                "method": "POST",

            }
        ],
        'absolute': absolute_path
    }


# The specs of the plugins, to be instantiated

def load_spec(module_name, absolute_path):
    spec = importlib.util.spec_from_file_location(module_name, absolute_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def main():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


    description =  '''
Starts a server for obsidian-lab. Requires a directory with scripts.

Example scripts: https://github.com/cristianvasquez/obsidian-lab-py/tree/main/examples

'''

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("directory", type=str, help="directory containing the scripts")
    parser.add_argument("--host", type=str, help="host", default=HOST)
    parser.add_argument("-p", "--port", type=int, help="port", default=PORT)
    parser.add_argument("-v", "--verbosity", help="verbose mode")

    args = parser.parse_args()
    
    global scripts_path
    scripts_path = str(Path(args.directory).absolute())

    print(f'running on {scripts_path}')

    files = Path(scripts_path).glob('*.py')
    something_found = False
    for path in files:
        print(f'{bcolors.OKGREEN}Found: {path.absolute()}{bcolors.ENDC}')
        something_found = True

    if not something_found:
        print(f'''{bcolors.WARNING}Warning: No scripts found in {scripts_path}.{bcolors.ENDC}''')

    app.run(port=args.port, host=args.host)
    
if __name__ == '__main__':
    main()