#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4
    prop = dir(hidden_4)
    for name in prop:
        if name[:2] != "__":
            print(name)
