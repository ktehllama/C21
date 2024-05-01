from cyml_utils import *
from termcolor import colored, cprint
import os

method_file: str = f"{os.path.abspath(__file__).replace('method_parse.py','')}inventory.yaml"
auto_termination: str = f"AUTO TERMINATION at {__file__}"

class MethodParser:
    def __init__(self) -> None:
        self.METHOD = yml_read(method_file)
        self.all_methods = [key for key in self.METHOD['methods']]
        print(msg('info')+"Loaded Methods ({}): {}".format(colored(len(self.all_methods),'magenta'),colored(self.all_methods,'white','on_magenta')))
    
    def check_method(self, method_name):
        if method_name in self.all_methods:
            pass
        else:
            print(msg('error')+"Method '{}' not found in {}".format(colored(method_name,'magenta'),f"{colored('const','yellow')} {colored('self.METHOD','green')}"))
            raise Exception(auto_termination)

    def get_return_methods(self, nm_flag=None):
        if nm_flag ==  '--nmethods':
            print(msg('notice')+"Returned amount of methods: {} ({})".format(colored(len(self.all_methods),'magenta'),colored('--nmethods flag','green')))
            return len(self.all_methods)
        print(msg('notice')+"Returned {} Methods: {}".format(colored(len(self.all_methods),'light_yellow'),colored(self.all_methods,'magenta')))
        return self.all_methods
      
    def get_card_values(self, method_name):
        self.check_method(method_name)
        print(msg('notice')+"Returned {} of method '{}'".format(colored('card values','light_yellow'),colored(method_name,'magenta')))
        return self.METHOD['methods'][method_name]['card values']

    def get_desc(self, method_name):
        self.check_method(method_name)
        print(msg('notice')+"Returned {} of method '{}'".format(colored('description','light_yellow'),colored(method_name,'magenta')))
        return self.METHOD['methods'][method_name]['description']

    def get_recommendations(self, method_name, scale_type):
        self.check_method(method_name)
        r_types = ['positive','neutral','negative']
        if scale_type in r_types:
            # print(msg('notice')+"Returned {} {} of method '{}'".format(colored(scale_type,'light_cyan'),colored('recommendations','light_yellow'),colored(method_name,'magenta')))
            return self.METHOD['methods'][method_name]['recommendations'][str(scale_type)]
        else:
            print(msg('error')+"Scale type '{}' not found in {}".format(colored(scale_type,'magenta'),f" {colored('dict_keys(','green')}{colored(str(self.METHOD['methods'][method_name]['recommendations'].keys()).replace('dict_keys(','').replace(')',''),'yellow')}{colored(')','green')}"))
            raise Exception(auto_termination)
