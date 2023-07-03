#!/usr/bin/env python3

import upperlower.lib.clipboard as cb


def main():
    text = input("Text to uppercase: ")
    text = text.upper()
    print(text)
    cb.set_text(text)
    print("# copied to clipboard")


##############################################################################

if __name__ == "__main__":
    main()
