# Admission Criteria

test_score = int(input("Enter Your Test Score .... "))

if test_score >= 80  :
    interview_score = int(input("Enter Your Interview Score .... "))   
    if interview_score >= 70 :
      print('Congratulation ✨ You are Admitted !!!')
    else:
      print("Failed Interview !")
else :
    print('Failed Test !')