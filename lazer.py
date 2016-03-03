author__ = 'Shweta Yakkali'
author__ = 'Aishwarya Desai'

def lazerfunc():
    """
    The lazerfunc() function retrieves data from the grid.txt file which contains the grid puzzle.
    the laser data for all possible lasers is entered in the form of row,column,orientation and sum.
    The sorting is done based on the sum of each possible laser.
    The user is prompted to enter the number of lasers, on entering the topmost list of lasers is displayed.
    :return: None
    """

    filename=input("Enter file name :")
    with open(filename) as f:
        elements = []
        x1=()

        for line in f:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                elements.append(line)                                           # adding the grid elements into elements list

        for row in elements:
                for column in row:

                    print(column, " ", end="")
                    length1 = len(elements)
                    length = len(elements[0])

                print(end="\n")
        print("\n")


        for row in range(length1):

                for column in range(length):
                    if (row != 0 or column != 0) and (row != 0 or column != length - 1) and (
                            row != length1 - 1 or column != 0) and (row != length1 - 1 or column != length - 1):
                        x = row, column
                        x1 = x1+(row, column)


                        for i in range(1, length - 1):
                            if x[0] == 0 and x[1] == i:
                                x = x + ('south',)
                                x1 = x1 + ('south',)



                        for i in range(1, length - 1):
                            if x[0] == i and x[1] == 0:
                                x = x + ('east',)
                                x1 = x1 + ('east',)


                        for i in range(1, length - 1):
                            if x[0] == length1 - 1 and x[1] == i:
                                x = x + ('north',)
                                x1 = x1 + ('north',)



                        for i in range(1, length):
                            if x[0] == i and x[1] == length - 1:
                                x = x + ('west',)
                                x1 = x1 + ('west',)





                        if 'south' in x:
                          sum1=elements[row][column-1]+elements[row][column+1]+elements[row+1][column]
                          x1=x1+tuple([sum1])


                        elif 'east' in x:

                         sum1=elements[row][column+1]+elements[row-1][column]+elements[row+1][column]
                         x1=x1+tuple([sum1])

                        elif 'north' in x:
                          sum1=elements[row][column-1]+elements[row][column+1]+elements[row-1][column]
                          x1=x1+tuple([sum1])

                        elif 'west'in x:
                          sum1=elements[row][column-1]+elements[row+1][column]+elements[row-1][column]
                          x1=x1+tuple([sum1])
                        else:

                            sum2n=elements[row][column-1]+elements[row][column+1]+elements[row-1][column]

                            sum2s=elements[row][column-1]+elements[row][column+1]+elements[row+1][column]

                            sum2w=elements[row+1][column]+elements[row-1][column]+elements[row][column-1]

                            sum2e=elements[row-1][column]+elements[row+1][column]+elements[row][column+1]

                            p=(max([int(sum2n),int(sum2s),int(sum2w),int(sum2e)]))
                            if(p==sum2n):
                                x1=x1+('north',)
                            elif(p==sum2s):
                                x1=x1+('south',)
                            elif(p==sum2w):
                                x1=x1+('west',)
                            else:
                                x1=x1+('east',)

                            x1=x1+tuple([p])

        x2=list(x1)
        x3=[]
        for i in range(0,len(x2),4):
            x3.append(x2[i:i+4])

        n=len(x3)
        for c in range(n-1):
            for d in range(n-c-1):
                    if(int(x3[d][3])<int(x3[d+1][3])):
                        x3[d],x3[d+1]=x3[d+1],x3[d]

        laser_no=int(input("Enter number of lasers : "))

        for i in range(laser_no):
            print(x3[i][:3])

def main():
    """
    The main function has a call to the lazerfunc() method
    :return: None
    """
    lazerfunc()

if __name__ == '__main__':
    main()



