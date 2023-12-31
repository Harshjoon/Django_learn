
def set_models(model, form, request):
    
    print("Setting model values from forms.")    

    # check if patient ID already exists
    post        = model.objects.all().filter(patient_id=form.cleaned_data["patient_id"])

    print("--------------------------------------------------------------")

    if len(post) != 0:
        # data already exists have to replace it.
        print("post deleted")
        post.delete()

    # form_inputs     = [
    #     'hospital_name',
    #         'patient_id',
    #         'patient_name',
    #         'gender',
    #         'age',
    #         'height',
    #         'weight',
    #         'diagnosis',
    #         'case_no',
    #         'date_of_admission',
    #         'date_of_surgery',
    #         'surgical_procedure',
    #         'surgeon_name_1',
    #         'surgeon_name_2',
    #         'assistant_surgeon_name_1',
    #         'assistant_surgeon_name_2',
    #         #'assistant_surgeon_name_3',
    #         'patient_in_time',
    #         'patient_out_time',
    #         'system_on_time',
    #         'system_off_time',
    #         'draping_start_time',
    #         'draping_end_time',
    #         'patient_incision_time',
    #         'patient_skin_closure_time',
    #         'port_placement_start_time',
    #         'cart_pos_and_doc_start_timem',
    #         'cart_pos_and_doc_end_time',
    #         'console_start_time',
    #         'console_end_time',
    #         'console_interruption_time',
    #         'cart_undock_start_time',
    #         'cart_undock_end_time',
    #         'instrument_used_1',
    #         'instrument_1_id',
    #         'instrument_used_2',
    #         'instrument_2_id',
    #         'instrument_used_3',
    #         'instrument_3_id',
    #         'instrument_used_4',
    #         'instrument_4_id',
    #         'instrument_used_5',
    #         'instrument_5_id',
    #         'cart_issue',
    #         'device_issue',
    #         'device_patient_complications',
    #         'date_of_discharge',
    #         'length_of_stay',
    #         'readmission',  
    #         'post_discharge_complications',  
    #         'surgical_steps',   
    #         'total_blood_loss', 
    #         # FOR TESTING
    #         #'instrument_test' 
    # ]

    model_arguments = {}

    import os
    
    print("--------os list", os.listdir())

    from form.form_choices  import form_inputs


    print("form inputs ------------------- ",form_inputs)

    for input_ in form_inputs:
        model_arguments[input_] = form.cleaned_data[input_]

    print("--DONE--")

    post        = model(**model_arguments)
    post.author = request.user
    post.save()

def set_forms(form, post):
    print("Setting form values from database.")    

    # form_inputs     = [
    #     'hospital_name',
    #     'patient_id',
    #     'patient_name',
    #     'gender',
    #     'age',
    #     'height',
    #     'weight',
    #     'diagnosis',
    #     'case_no',
    #     'date_of_admission',
    #     'date_of_surgery',
    #     'surgical_procedure',
    #     'surgeon_name_1',
    #     'surgeon_name_2',
    #     'assistant_surgeon_name_1',
    #     'assistant_surgeon_name_2',
    #     'assistant_surgeon_name_3',
    #     'patient_in_time',
    #     'patient_out_time',
    #     'system_on_time',
    #     'system_off_time',
    #     'draping_start_time',
    #     'draping_end_time',
    #     'patient_incision_time',
    #     'patient_skin_closure_time',
    #     'port_placement_start_time',
    #     'cart_pos_and_doc_start_timem',
    #     'cart_pos_and_doc_end_time',
    #     'console_start_time',
    #     'console_end_time',
    #     'console_interruption_time',
    #     'cart_undock_start_time',
    #     'cart_undock_end_time',
    #     'instrument_used_1',
    #     'instrument_used_2',
    #     'instrument_used_3',
    #     'instrument_used_4',
    #     'instrument_used_5',
    #     'cart_issue',
    #     'device_issue',
    #     'device_patient_complications',
    #     'date_of_discharge',
    #     'length_of_stay',
    #     'readmission',
    #     'post_discharge_complications',
    #     'surgical_steps',
    #     'total_blood_loss',
    # ]

    out_form   = form()

    from form.form_choices  import from_inputs

    form_arguments = {}
    for input_ in form_inputs:
        #form_arguments[input_] = post[0].__dict__[input_]
        out_form.fields[input_] = post[0].__dict__[input_]
        print(post[0].__dict__[input_])

    #print(form_arguments)
    #out_form = form(**form_arguments)
    #print("----------------------------------------------------------")

    return out_form
