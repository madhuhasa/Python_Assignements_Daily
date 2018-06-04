import pandas as pd

exam_result = {'name':["A","B","C","X","Y","Z","P"],'score':[75,78,90,85,56,33,95],'No_of_attempts':[1,2,1,3,1,2,3],'qualify':["No","Yes","Yes","Yes","Yes","No","Yes"]}

result = pd.DataFrame(exam_result)
print("\n")
print("data from dictionary without index labels -")
print(result)

index_labels = ['a','b','c','d','e','f','g']

result.index = index_labels

print("\n")
print("After giving index labels")
print(result)

print(result[['name','qualify']])
#score_35 = (result['score']>20) & (result['score']<=35)
print(result[(result['score']>20) & (result['score']<=35)])
print("Sum of attempts of all students is %d " %(sum(result['No_of_attempts'])))

