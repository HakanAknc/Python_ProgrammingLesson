for count in range(6):
    print("Iteration no. {}".format(count))
else:
    print("for loop over. Now in else block")
print ("End of for loop")

print("********************")


for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print ("{:3d}".format(k), end=' ')  # 3d aradaki boşluk uzunluğunu temsil eder
   print()