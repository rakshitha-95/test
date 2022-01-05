def subjest(fun):
    def greet():
        return "hai"+fun
    return greet()
print(subjest("rakshitha"))