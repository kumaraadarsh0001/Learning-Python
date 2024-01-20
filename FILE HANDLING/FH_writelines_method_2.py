file= open('student.txt', mode='w')
lst1=['rahul ','sonam ','sumit ','rani ','raj']
lst2=['\nrahul','\nsonam','\nsumit','\nrani','\nraj']
file.writelines(lst1)
file.writelines(lst2)
file.close()
print('opretion successfully')