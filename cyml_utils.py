import yaml
from termcolor import colored, cprint

auto_termination: str = f"AUTO TERMINATION at {__file__}"
def msg(msg_type):
    brackets_map: list = [['[',']'],['light_grey','bold']]
    message = ''
    match msg_type:
        case "success":
            message = colored("success","light_green",attrs=['bold'])
        case "notice":
            message = colored("notice","blue",attrs=['bold'])
        case "info":
            message = colored("info","magenta",attrs=['bold'])
        case "warning":
            message = colored("warning","yellow",attrs=['bold'])
        case "error":
            message = colored("error","red",attrs=['bold'])
    return(f"{colored(brackets_map[0][0],brackets_map[1][0],attrs=[brackets_map[1][1]])}{message}{colored(brackets_map[0][1],brackets_map[1][0],attrs=[brackets_map[1][1]])} ")

def yml_read(fn):
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        cprint(msg("success")+f"{fn} loaded successfully")
        return content
    except Exception as e:
        cprint(msg("error")+f"There was an error loading {fn}\n Error: {e}")
        raise Exception(auto_termination)
