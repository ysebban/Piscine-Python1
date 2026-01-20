import time as time


def main():
    sinceEpoch = time.time()
    print("Seconds since January 11, 1970:", end="")
    print(f"{sinceEpoch:,.5f}", end="")
    print(" or ", end="")
    print(f"{sinceEpoch:.2e}")
    utc_time = time.gmtime(sinceEpoch)
    print(time.strftime("%b %d %Y", utc_time))


main()
