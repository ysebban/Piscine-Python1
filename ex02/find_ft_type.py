def all_thing_is_obj(object: any) -> int:

    type_map = {
        list: "List :",
        tuple: "Tuple :",
        set: "Set :",
        dict: "Dict :",
        str: f"{object} is in the kitchen"
    }

    for T in type_map:
        if T == type(object):
            print(f"{type_map[T]} {type(object)}")
            return 42
    print("Type not found")
    return 42
