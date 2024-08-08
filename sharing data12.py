import multiprocessing

result=[]

def calc_square(numbers):
    global result 
    for n in numbers:
        result.append(n*n)

    print('inside process' + str(result))
 

if __name__ == "__main__":
    arr = [2,3,8,9]
    p1= multiprocessing.Process(target = calc_square, args=(arr,))
    p1.start()
    p1.join()

    print("result" + str(result))
