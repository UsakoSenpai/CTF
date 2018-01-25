def main():
    print("starting...")
    n=10000000 
    max_ch_starter = 0 
    max_ch_size = 0

    for i in range (0, n):
        num = i
        print ""
        print ("Starting number: " + str(num))
        current_ch_starter = i
        current_ch_size = 0
        i += 1
        while (num > 1):
           current_ch_size += 1
           # print(" > " + str(num)),
           if (num % 2 == 0):
               # even
               num = num / 2
           else:
                # odd
                num = 3 * num + 1
        if (current_ch_size > max_ch_size):
            max_ch_size = current_ch_size
            max_ch_starter = current_ch_starter

    print("Max Chain Size is: " + str(max_ch_size))
    print("Starting with: " + str(max_ch_starter))


if __name__ == '__main__':
    main()
