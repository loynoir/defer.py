from Defer import Defer
with Defer() as defer:
    print("enter the room")
    defer(lambda: print("leave the room"))

    print("prepare printer")
    defer(lambda: print("close printer"))

    print("start printing")
    defer(lambda: print("end printing"))

    print(3)
    print(4)
    print(5)
    print("LONG LONG TASKS")
