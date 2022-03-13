#if len(some_list) > 0:
    # do something here when the list is not empty
#else:
    # do something else when the list is empty

def check_container_empty(container):
    if container:
        print(f"{container} has elements.")
    else:
        print(f"{container} doesn't have elements.")

check_container_empty([1, 2, 3])
check_container_empty(set())
check_container_empty({"zero": 0, "one": 1})
check_container_empty(tuple())


#OUPUT
#[1, 2, 3] has elements.
#set() doesn't have elements.
#{'zero': 0, 'one': 1} has elements.
#() doesn't have elements.