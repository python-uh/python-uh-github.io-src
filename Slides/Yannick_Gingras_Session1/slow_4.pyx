cpdef cyis_prime(int n):
    """ Return True if number is prime """
    cdef int i, top
    top = n//2
    for i in range(2, top):
        if n % i == 0:
            return False
    return True


def main():
    is_prime(20996011)


if __name__ == "__main__":
    main()
    
