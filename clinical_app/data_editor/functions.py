
def edit_hospitals(model, form, request):
    if form.cleaned_data['add_hospital_name'] != None:
        add_hospital(model, form.cleaned_data['add_hospital_name'])

    if form.cleaned_data['remove_hospital_name'] != None:
        remove_hospital(model, form.cleaned_data['remove_hospital_name'])
        #print("remove hospital name none")

    #print(form.cleaned_data['add_hospital_name'])
    #print(form.cleaned_data['remove_hospital_name'])
    return None


def add_hospital(model, hospital_name):
    
    new_model   = model(hospital_name=hospital_name)
    new_model.save()

    return None


def remove_hospital(model, hospital_name):

    print("------------------------------------")
    existing_model  = model.objects.all().filter( hospital_name=hospital_name ).first()
    #print(existing_model)
    #existing_model.delete()

    return None