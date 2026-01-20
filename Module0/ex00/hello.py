def main():
    ft_list = ["Hello", "tata!"]  # world
    ft_tuple = ("Hello", "toto!")  # country
    ft_set = {"Hello", "tutu!"}  # city
    ft_dict = {"Hello": "titi!"}  # campus

    ft_list[1] = "World!"

    ft_tuple = ("Hello", "France!")

    ft_set.discard("tutu!")
    ft_set.add("Mulhouse!")

    ft_dict["Hello"] = "42Mulhouse!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


main()
