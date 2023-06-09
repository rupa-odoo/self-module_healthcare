{
    'name':"Healthcare",
    'version':'1.0',
    'depends':['base','mail'],
    'author':"Author Name",
    'category':'Category',
    'description':"",
    'data':[
        'security/ir.model.access.csv',
        'views/healthcare_appointment.xml',
        'views/healthcare_tag.xml',
        'views/healthcare_type.xml',
        'views/healthcare_prescription.xml',
        'views/healthcare_medicine.xml',
        'views/healthcare_bedmanage.xml',
        'views/healthcare_docter.xml',
        'report/healthcare_reports.xml',
        'report/healthcare_templates.xml',
        'views/healthcare_menus.xml',

    ],
    'demo':[
        'demo/healthcare_demo.xml',
    ],
    'application':True,
}