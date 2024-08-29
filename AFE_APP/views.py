from django.shortcuts import redirect, render
from .forms import AFE_REQUEST


def main(request):
    
    if request.method == 'POST':       
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        subsidiaries = request.POST.get('subsidiaries')
        category = request.POST.get('category') 
        types = request.POST.get('types')  
        environment = request.POST.get('environment') 
        assets = request.POST.get('assets') 
        start_date = request.POST.get('start_date')  
        ops_duration = request.POST.get('ops_duration')  
        perenco_share = request.POST.get('perenco_share')  
        create_leader = request.POST.get('create_leader')  
        member = request.POST.get('member')  

        # Save the data to the model
        AFE_REQUEST.objects.create(
            name=name,
            description=description,
            subsidiaries=subsidiaries,
            category=category,
            types=types,
            environment=environment,
            assets=assets,
            start_date=start_date,
            ops_duration=ops_duration,
            perenco_share=perenco_share,
            create_leader=create_leader,
            member=member
        )
        
        return redirect('reports')  # Redirect to a success page
    
    return render(request, 'main.html')

def reports(request):
    
    return render(request, 'reports.html')

def resources(request):
    
    return render(request, 'resources.html')


def resources_detail(request):
    
    return render(request, 'resources-detail.html')

