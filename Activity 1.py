student_data = {"id1" :{"name" : ["Sara"], "class" : ["A"], "subject_integration" : ["English" , "Math" , "Science" ]} , 
                "id2" :{"name" : ["David"], "class" : ["A"], "subject_integration" : ["English" , "Math" , "Science" ] } , 
                "id3" :{"name" : ["Avanthika"], "class" : ["A"], "subject_integration" : ["English" , "Math" , "Science" ] } ,
                  "id4" :{"name" : ["Avanthika"], "class" : ["A"], "subject_integration" : ["English" , "Math" , "Science" ] } ,
}
result = {}
for key,value in student_data.items():
    if value not in  result.values():
        result[key] = value
print(result)           