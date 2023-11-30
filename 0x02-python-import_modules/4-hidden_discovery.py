#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    get_name = dir(hidden_4)
    for get in get_name:
        if get[:2] != "__":
            print(get)
