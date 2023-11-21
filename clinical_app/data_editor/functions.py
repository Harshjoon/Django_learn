
def edit_hospitals(model, form, request):
    if form.cleaned_data['add_hospital_name'] != None:
        add_hospital(model, form.cleaned_data['add_hospital_name'])

    if form.cleaned_data['remove_hospital_name'] != None:
        remove_hospital(model, form.cleaned_data['remove_hospital_name'])
    
    '''
    for i,form in enumeate(forms):
        add_name        = form.cleaned_data['add']
        remove_name     = form.cleaned_data['remove']
        if add_name != None:
            add_to_model(models[i], add_name)
        if remove_name != None:
            remove_from_model(models[i], remove_name)
    '''
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

#############################################################

#def edit_models(models, forms, request):
def edit_models(model, form, request):
    # for i,form in enumerate(forms):
    #     add_name        = form.cleaned_data['add']
    #     remove_name     = form.cleaned_data['remove']
    #     if add_name != None:
    #         add_to_model(models[i], add_name)
    #     if remove_name != None:
    #         remove_from_model(models[i], remove_name)

    add_name        = form.cleaned_data['add']
    remove_name     = form.cleaned_data['remove']
    print("addname",add_name)
    print("removename",remove_name)
    if add_name != None:
        add_to_model(model, add_name)
    if remove_name != None:
        remove_from_model(model, remove_name)

def add_to_model(model,name):
    print(model, name)
    new_model       = model(name=name)
    new_model.save()

def remove_from_model(model,name):
    existing_model     = model.objects.all().filter(name=name).first()
    existing_model.delete()