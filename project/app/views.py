from django.shortcuts import render

# Create your views here.
def set(request):
    my_list1={'id':1,'name':'himanshi','city':'bhopal'}
    my_list2={'id':2,'name':'vedansh','city':'balaghat'}
    my_list=[my_list1,my_list2]
    request.session['data']=my_list
    return render(request,'set.html')


def get(request):
    data1=request.session.get('data','Guest')    
    return  render(request,'get.html',{'name':data1})


def delete(request):
    if 'data' in request.session:
        del request.session['data']
    #request.session.flush()  #multiple object delete
    return render(request,'delete.html')