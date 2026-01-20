def NULL_not_found(obj: any) -> int:
    type_map = {
        type(None): lambda x: (print(f"Nothing: None {type(x)}") or True),
        float: lambda x: (print(f"Cheese: nan {type(x)}") or True)
        if x != x else False,
        int: lambda x: (print(f"Zero: 0 {type(x)}") or True)
        if x == 0 else False,
        str: lambda x: (print(f"Empty: {type(x)}") or True)
        if x == "" else False,
        bool: lambda x: (print(f"Fake: False {type(x)}") or True)
        if x is False else False,
    }

    obj_type = type(obj)

    for T in type_map:
        if T == obj_type:
            if type_map[T](obj):
                return 0
            break

    print("Type not Found")
    return 1
