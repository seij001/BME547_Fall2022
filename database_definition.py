from pymodm import MongoModel, fields


class Patient(MongoModel):
    """Definition of a patient record in the database
    """
    name = fields.CharField()
    id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    test_name = fields.ListField()
    test_result = fields.ListField()