#! /usr/bin/env python3

def is_prime(n):
    """ Return True if number is prime """
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def main():
    is_prime(20996011)


if __name__ == "__main__":
    main()
    
