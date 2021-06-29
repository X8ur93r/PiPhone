from termcolor import colored

def debug(where,error,info=None,ret=None):
    print(colored('[-]','red',attrs=['bold']) + f' {where} says {ret}:{info} <- error: {error}')
def info(info,where):
    print(colored('[i]','yellow',attrs=['bold']) + f' {where} says: {info}')