def main():
    # Get user input
    x = input()
    # call convert func
    answer = convert(x)
    # print the result
    print(answer)

def convert(x):
    # replace :) for happy emoji
    x1 = x.replace(":)", '🙂')
    #replace :( for sad emoji
    x2 = x.replace(":(", '☹️')
    #return string
    return x2
main()