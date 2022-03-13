
#create a file hello_world.txt and writes in hello python.
#if we execute again it will return hello python, is this file close? True. etc

with open("hello_world.txt", "a") as file:
    file.write("Hello Python!")

with open("hello_world.txt") as file:
    print(file.read())
 
print("Is file close?", file.closed)


#OUTPUT
#Hello World!Hello Python!Hello Python!
#Is file close? True