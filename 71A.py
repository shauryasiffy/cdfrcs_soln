t = int(input())
for i in range(t):
    inp_str = str(input())
    #print(inp_str)
    if len(inp_str)<=10:
        print(inp_str)
    if len(inp_str)>10:
        count = len(inp_str[0:-2])
        #print(count)
        print("{}{}{}".format(inp_str[0],count,inp_str[-1]))