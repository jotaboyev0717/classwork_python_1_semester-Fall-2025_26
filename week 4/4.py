def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n +1

# def collatz_length(n):
     