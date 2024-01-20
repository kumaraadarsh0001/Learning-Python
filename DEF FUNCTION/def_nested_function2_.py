def disp(x):
    def show():
        return "show function "
    result=show()+x+"disp function "
    return result
print(disp("geekyshow "))