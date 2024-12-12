# A university tracks course enrollments in a tuple of 
# Courses = ("math", "physics", "chemistry", "Bio", "history").
# Pereform the following tasks:
# a. Check if the course 'Economics" is offered.
# b. Reverse the tuple and print it.
# c. Create a new tuple thats adds "Computer Science" and "Statistics" to the course tuple.
sum=0
def sum_recursive(n):
    if n<=0:
        sum+=1
        return sum_recursive(n-1)+ sum_recursive(n-2)
print(sum_recursive(2))
    