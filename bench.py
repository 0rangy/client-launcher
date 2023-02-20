from timeit import default_timer as timer
import random
import os
class color:
      PURPLE = '\033[95m'
      CYAN = '\033[96m'
      DARKCYAN = '\033[36m'
      BLUE = '\033[94m'
      GREEN = '\033[92m'
      YELLOW = '\033[93m'
      RED = '\033[91m'
      BOLD = '\033[1m'                                                               
      UNDERLINE = '\033[4m'
      END = '\033[0m'
def bubblesort(amt1,len1,debug1,ind1,test1):
  def sortTest(amt,debug,test):
          arr = []
          done = False
          for i in range(amt):
              arr.append(random.randint(0,100))
          maybedone = False
          decided = False
          it = 0
          start = timer()
          if not test:
              while done != True:
                  it += 1
                  decided=False
                  if maybedone == True:
                      done = True
    #        for r in range(len(arr) - 1):
             #   if arr[r] > arr[r + 1]:
            #        done = False
           #         decided = False
          #          temp1 = arr[r]
         #           arr[r] = arr[r+1]
        #            arr[r + 1] = temp1
       #             print(str(arr)  + "\n")
      #          else:
     #               if not decided:
    #                    done = True
                  for i in range(len(arr) - 1):
                      if arr[i] > arr[i+1]:
                          decided = True
                          maybedone = False
                          temp = arr[i]
                          arr[i] = arr[i+1]
                          arr[i+1] = temp
                      if debug:
                          print(color.RED + "\n Iteration: " +color.BOLD +  str(it) + "  "+ color.END + str(arr))
                          os.system("clear")
                      else:
                          if decided != True:
                              maybedone = True
          else:
              length = len(arr) - 1
              while not done:
                  decided=False
                  if maybedone:
                      done = True
                  it +=1
                  for i in range(length):
                      if arr[i] > arr[i+1]:
                          decided = True
                          maybedone = False
                          temp = arr[i]
                          arr[i] = arr[i+1]
                          arr[i+1]=temp
                      else:
                          if not decided:
                              maybedone = True
                  if decided:
                      length -= 1
          end = timer()
          if debug:
              print(color.GREEN +color.BOLD+ "\n\n\nDone!")
              print(color.END + color.GREEN + "Final Array: " +color.BOLD + str(arr) + color.END)
              print(color.DARKCYAN + "In " +color.CYAN + color.BOLD +  str(it) + color.END +color.DARKCYAN + " iteration(s)")
              print("Time Elapsed: " +color.CYAN + color.BOLD + str(end - start) +color.END + color.DARKCYAN+ " second(s)")
              print("Array length: " +color.CYAN +color.BOLD + str(len(arr)) + color.END)
          else:
              print(color.GREEN + "Done! ("+ str(end-start)+"s)")
          print(color.END + color.BLUE + str(arr) + color.END)
          return end-start
  import sys,time,argparse
  #parser = argparse.ArgumentParser()
  
  #parser.add_argument("--debug","-d",action="store_true")
  #parser.add_argument("amt")
  #parser.add_argument("len")
  #parser.add_argument("--test","-t",action="store_true")
  #parser.add_argument("--individual","-i",action="store_true")
  
  #args = parser.parse_args()
  
  print("Sorting " + str(amt1) + " arrays with "+ str(len1) +" numbers... (Test mode : " + str(test1) + ")")
  time.sleep(3)
  
  resultarr = []
  for i in range(int(amt1)):
    resultarr.append(sortTest(int(len1),debug1,test1))
  ttl = 0
  for r in resultarr:
    ttl += r
  os.system("clear")
  print(color.GREEN +color.BOLD+ "Test successful"+color.END)
  print(color.CYAN + "Average: "+color.BOLD + str(ttl/float(str(amt1) + ".0")) + color.END)
  print(color.CYAN + "Minimum: "+color.BOLD + str(min(resultarr)) + color.END)
  print(color.CYAN + "Maximum: "+color.BOLD + str(max(resultarr)) + color.END)
  if ind1:
      print("\nIndividual results: ")
      run = 0
      for result in resultarr:
          run +=1
          print(color.YELLOW +"Run " + str(run) + ": " + str(result) + color.END)


class color:
      PURPLE = '\033[95m'
      CYAN = '\033[96m'
      DARKCYAN = '\033[36m'
      BLUE = '\033[94m'
      GREEN = '\033[92m'
      YELLOW = '\033[93m'
      RED = '\033[91m'
      BOLD = '\033[1m'                                                               
      UNDERLINE = '\033[4m'
      END = '\033[0m'


print(color.GREEN + "Welcome to Benchmark v0.1!"+ color.END)
print(color.YELLOW + "Tests: Bubble sort (bblsrt)")
i = input(color.CYAN +"Enter a test ID: " + color.END)
if i =="bblsrt":
  amtarr = int(input(color.CYAN+"How many arrays?\n"+color.END))
  lenarr = int(input(color.CYAN +"How many numbers in each arrays?\n"+ color.END))
  debugmd = bool(input(color.CYAN +"Debug?(TANKS PERFORMANCE)\n"+ color.END))
  indi = bool(input(color.CYAN +"Have individual results for each array?\n"+ color.END))
  goodal = bool(input(color.CYAN +"Use faster version of the algorithm?\n"+ color.END))
  
  bubblesort(amtarr,lenarr,debugmd,indi,goodal)
