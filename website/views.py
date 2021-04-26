from django.shortcuts import render

def home(request):
    return render(request, "home.html" , {})



def add(request):
    from random import randint 

    num_1 = randint(0,10)
    num_2 = randint(0,10 )
        


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        #error handling
        if not answer :
            my_answer = 'HEY , You forgot to type your answer '
            color='info'
            return render(request,'add.html',{
                'color': color ,
                'my_answer':my_answer,
                'num_1': num_1 ,
                'num_2': num_2,
                })
        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer)  == correct_answer :
           my_answer = ' correct !   ' + str(old_num_1)  + "  +  "  + str(old_num_2) + "   is   :    " +  str(correct_answer)
           color = 'success'
        else :
           my_answer = '   Ooops !!!!    ' + str(old_num_1) + "  +  " +  str(old_num_2) + "    is   :  " + str(correct_answer)  + '    ; and  not    :    ' +  str(answer)
           color = 'danger' 
        return render(request, "add.html" , {
        'color': color ,
        'answer' : answer,
        'my_answer': my_answer , 
        'num_1' :  num_1 , 
        'num_2':  num_2  , })
        
        

    return render(request, "add.html" , {
        'num_1' :  num_1 , 
        'num_2':  num_2  , })







##########################################################################################################

def substract(request):
    from random import randint 

    num_1 = randint(0,10)
    num_2 = randint(0,10 )
        


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        ## error handling 
        if not answer :
            my_answer = 'HEY , You forgot to type your answer '
            color='info'
            return render(request,'substract.html',{
                'color': color ,
                'my_answer':my_answer,
                'num_1': num_1 ,
                'num_2': num_2,
                })
        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer)  == correct_answer :
           my_answer = ' correct !   ' + str(old_num_1)  + "  -  "  + str(old_num_2) + "   is   :    " +  str(correct_answer)
           color = 'success'
        else :
           my_answer = '   Ooops !!!!    ' + str(old_num_1) + "  -  " +  str(old_num_2) + "    is   :  " + str(correct_answer)  + '    ; and  not    :    ' +  str(answer)
           color = 'danger' 
        return render(request, "substract.html" , {
        'color': color ,
        'answer' : answer,
        'my_answer': my_answer , 
        'num_1' :  num_1 , 
        'num_2':  num_2  , })
        
        

    return render(request, "substract.html" , {
        'num_1' :  num_1 , 
        'num_2':  num_2  , })

###########################################################################################################
def  divide(request):
    from random import randint 

    num_1 = randint(0,10)
    num_2 = randint(1,10 )
        
    

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        # error handling
        if not answer :
            my_answer = 'HEY , You forgot to type your answer '
            color='info'
            return render(request,'divide.html',{
                'color': color ,
                'my_answer':my_answer,
                'num_1': num_1 ,
                'num_2': num_2,
                })

        correct_answer = int(old_num_1) / int(old_num_2)
        if float(answer)  == correct_answer :
           my_answer = ' correct !   ' + str(old_num_1)  + "  /  "  + str(old_num_2) + "   is   :    " +  str(correct_answer)
           color = 'success'
        else :
           my_answer = '   Ooops !!!!    ' + str(old_num_1) + "  /  " +  str(old_num_2) + "    is   :  " + str(correct_answer)  + '    ; and  not    :    ' +  str(answer)
           color = 'danger' 
        return render(request, "divide.html" , {
        'color': color ,
        'answer' : answer,
        'my_answer': my_answer , 
        'num_1' :  num_1 , 
        'num_2':  num_2  , })
        
        

    return render(request, "divide.html" , {
        'num_1' :  num_1 , 
        'num_2':  num_2  , })



##########################################################################################################

def multiply(request):
    from random import randint 

    num_1 = randint(0,10)
    num_2 = randint(0,10 )
        


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        #error handling 
        if not answer :
            my_answer = 'HEY , You forgot to type your answer '
            color='info'
            return render(request,'multiply.html',{
                'color': color ,
                'my_answer':my_answer,
                'num_1': num_1 ,
                'num_2': num_2,
                })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer)  == correct_answer :
           my_answer = ' correct !   ' + str(old_num_1)  + "  x  "  + str(old_num_2) + "   is   :    " +  str(correct_answer)
           color = 'success'
        else :
           my_answer = '   Ooops !!!!    ' + str(old_num_1) + "  x  " +  str(old_num_2) + "    is   :  " + str(correct_answer)  + '    ; and  not    :    ' +  str(answer)
           color = 'danger' 
        return render(request, "multiply.html" , {
        'color': color ,
        'answer' : answer,
        'my_answer': my_answer , 
        'num_1' :  num_1 , 
        'num_2':  num_2  , })
        
        

    return render(request, "multiply.html" , {
        'num_1' :  num_1 , 
        'num_2':  num_2  , })








##########################################################################################################



