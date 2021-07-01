from termcolor import colored

def debug(where,info=None,error=None,ret=None,t='-'):
    # print colored type
    if t=='i':
        print(colored('[i] ','yellow'),end='')
    elif t=='+':
        print(colored('[+] ','green'),end='')
    else:
        print(colored('[-] ','red'),end='')
    # now the real info
    print(f'{where} says ', end='')
    if not ret is None:
        if t=='i':
            print(colored(f'{ret}:','yellow'), end='')
        elif t=='+':
            print(colored(f'{ret}:', 'green'), end='')
        else:
            print(colored(f'{ret}:', 'red'), end='')
    print(info, end='')
    if not error is None:
        print(f' <- error: {error}')
    else: print()
