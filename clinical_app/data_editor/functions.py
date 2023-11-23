def edit_models(model, form, request):
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
    print("-----------------------------------",model.objects.all())
    existing_model     = model.objects.all().filter(name=name).first()
    existing_model.delete()