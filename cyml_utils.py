import yaml

auto_termination: str = f"AUTO TERMINATION at {__file__}"
def msg(msg_type):
    brackets_map: list = ['[',']']
    message = ''
    match msg_type:
        case "success":
            message = "\033[92;1msuccess\033[0m"
        case "notice":
            message = "\033[94;1mnotice\033[0m"
        case "info":
            message = "\033[95;1minfo\033[0m"
        case "warning":
            message = "\033[33;1mwarning\033[0m"
        case "error":
            message = "\033[91;1merror\033[0m"
    return(f"\033[90;1m{brackets_map[0]}\033[0m{message}\033[90;1m{brackets_map[1]}\033[0m ")

def yml_read(fn):
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        print(msg("success")+f"{fn} loaded successfully")
        return content
    except Exception as e:
        print(msg("error")+f"There was an error loading {fn}\n Error: {e}")
        raise Exception(auto_termination)
