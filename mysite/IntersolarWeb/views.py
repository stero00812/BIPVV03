from django.shortcuts import render
from django.http import HttpResponse
from .forms import DateForm
from django.http import HttpResponseRedirect
import Z_Data_Analysis_Django as da

x=30
y=20
z=x+y

import plotly
from plotly.graph_objs import Scatter, Layout

#For plotly, help: https://plot.ly/python/user-guide/
#https://plot.ly/python/getting-started/

#def index(request):
#    #return HttpResponse("Hello, world. You're at the polls index." + str(z))
#
##    template = loader.get_template('test.html')
##    context = {
##        'latest_question_list': latest_question_list,
##    }
##    return HttpResponse(template.render(context, request))
#    
#    return render(request, 'test.html', {'current_name':z})
    
    

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required. Returns true if  all the fields are valid. places the form in its cleaned data mode
            d_from=form.cleaned_data['Date_from']
            d_to=form.cleaned_data['Date_to']
            Meas=form.cleaned_data['select']
            print d_from
            
            if Meas=='1':
                df=da.Thermal(d_from,d_to)
            
                plotly.offline.plot({
                    "data": [Scatter(x=df.index, y=df['Mean Cavity'])],
                    "layout": Layout(title="Mean cavity temperature from "+d_from+" to "+d_to)
                },auto_open=False,filename='Thermal_graph.html')
            # ...
            # redirect to a new URL:
            #return HttpResponse(test2)
            #return HttpResponseRedirect('')
                return render(request, 'Thermal.html', {'form': form})
                
            if Meas=='2':
                df=da.Electrical(d_from,d_to)
            
                plotly.offline.plot({
                    "data": [Scatter(x=df.index, y=df['Pin[W]'])],
                    "layout": Layout(title="Power [W] from BIPV V0.3 from "+d_from+" to "+d_to)
                },auto_open=False,filename='Electrical_graph.html')
            # ...
            # redirect to a new URL:
            #return HttpResponse(test2)
            #return HttpResponseRedirect('')
                return render(request, 'Electrical.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DateForm()

        return render(request, 'Main.html', {'form': form})

