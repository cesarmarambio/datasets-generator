import random
import uuid
from datetime import datetime
from faker import Faker

def get_employee_data(language, num_rows):
    """
    Generates a list of dictionaries containing synthetic employee data.
    """
    start_date = datetime(2023, 1, 1)
    
    # 1. Localization Dictionaries & Faker Initialization
    if language == 'es':
        fake = Faker('es_CL')
        departments = ["Tecnologia", "Finanzas", "Recursos Humanos", "Operaciones", "Comercial"]
        job_titles = ["Data Engineer", "Analista BI", "Gerente", "Coordinador", "Ejecutivo"]
    else:
        fake = Faker('en_US')
        departments = ["Technology", "Finance", "Human Resources", "Operations", "Sales"]
        job_titles = ["Data Engineer", "BI Analyst", "Manager", "Coordinator", "Executive"]

    # 2. Data Generation
    rows = []
    
    for i in range(1, num_rows + 1):
        record = {
            "surrogate_id": str(uuid.uuid4())[:8],
            "natural_employee_id": i,
            "full_name": fake.name(),
            "email": fake.ascii_company_email(),
            "city": fake.city(),
            "department": random.choice(departments),
            "job_title": random.choice(job_titles),
            "base_salary": random.randint(800000, 3500000),
            "hire_date": start_date.strftime("%Y-%m-%d")
        }
        rows.append(record)
        
    return rows