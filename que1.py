def checks():
    try:
        user=int(input("Enter a amount: "))
        if user<10000:
            raise ValueError("Please enter a amount more than 10000")
    except ValueError as e:
        print(e)
checks()
        