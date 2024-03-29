#!/usr/bin/python3
"""A script that:
- Importing sys module to access 
- command-line arguments
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as bug:
        print('Error code:', bug.code)
