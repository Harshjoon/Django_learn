GENDER_CHOICES = [
    ("M","Male"),
    ("F","Female"),
]

DIAGNOSIS_CHOICES = [
    ('000', "diagnosis 1"),
    ('001', "diagnosis 2"),
    ('002', "diagnosis 3"),
    ('003', "diagnosis 4"),
    ('004', "diagnosis 5"),
]

SURGICAL_PROCEDURE_CHOICES = [
    ('000', "surgical procedure 1"),
    ('001', "surgical procedure 2"),
    ('002', "surgical procedure 3"),
    ('003', "surgical procedure 4"),
    ('004', "surgical procedure 5"),
    ('005', "surgical procedure 6"),
]

INSTRUMENT_CHOICES = [
    ("AAA", "instrument 1"),
    ("AAB", "instrument 2"),
    ("AAC", "instrument 3"),
    ("AAD", "instrument 4"),
    ("AAE", "instrument 5"),
    ("AAF", "instrument 6"),
]

CART_ISSUE_CHOICES = [
    ("000", "cart issue 1"),
    ("001", "cart issue 2"),
    ("002", "cart issue 3"),
    ("003", "cart issue 4"),
    ("004", "cart issue 5"),
    ("005", "cart issue 6"),
]

DEVICE_ISSUE_CHOICES = [
    ("000", "device issue 1"),
    ("001", "device issue 2"),
    ("002", "device issue 3"),
    ("003", "device issue 4"),
    ("004", "device issue 5"),
    ("005", "device issue 6"),
]

form_inputs = [
        'hospital_name',
            'patient_id',
            'patient_name',
            'gender',
            'age',
            'height',
            'weight',
            'diagnosis',
            'case_no',
            'date_of_admission',
            'date_of_surgery',
            'surgical_procedure',
            'surgeon_name_1',
            'surgeon_name_2',
            'assistant_surgeon_name_1',
            'assistant_surgeon_name_2',
            #'assistant_surgeon_name_3',
            'patient_in_time',
            'patient_out_time',
            'system_on_time',
            'system_off_time',
            'draping_start_time',
            'draping_end_time',
            'patient_incision_time',
            'patient_skin_closure_time',
            'port_placement_start_time',
            'cart_pos_and_doc_start_timem',
            'cart_pos_and_doc_end_time',
            'console_start_time',
            'console_end_time',
            'console_interruption_time',
            'cart_undock_start_time',
            'cart_undock_end_time',
            'instrument_used_1',
            'instrument_1_id',
            'instrument_used_2',
            'instrument_2_id',
            'instrument_used_3',
            'instrument_3_id',
            'instrument_used_4',
            'instrument_4_id',
            'instrument_used_5',
            'instrument_5_id',
            'cart_issue',
            'device_issue',
            'device_patient_complications',
            'date_of_discharge',
            'length_of_stay',
            'readmission',  
            'post_discharge_complications',  
            'surgical_steps',   
            'total_blood_loss',
            'additional_remark' 
            # FOR TESTING
            #'instrument_test' 
    ]