class hello:
    name = "Hello, World"

class goodbye:
    name = "Goodbye, World"

class here:
    name = "Here I Am, World"


classes_list = {
    "hello": hello,
    "goodbye": goodbye,
    "here": here,
}

selected_option = "goodbye"

selected_class = classes_list.get(selected_option)

print(selected_class.name)