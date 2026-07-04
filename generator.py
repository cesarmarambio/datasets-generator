import argparse
import csv
import random
import uuid
import os
from datetime import datetime, timedelta
from faker import Faker

def generate_data(file_format, separator, language, num_rows):
    # Base configuration
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
    dim_employees_rows = []
    
    for i in range(1, num_rows + 1):
        full_name = fake.name()
        department = random.choice(departments)
        job_title = random.choice(job_titles)
        salary = random.randint(800000, 3500000)
        
        city = fake.city()
        email = fake.ascii_company_email()
        
        record = {
            "surrogate_id": str(uuid.uuid4())[:8],
            "natural_employee_id": i,
            "full_name": full_name,
            "email": email,
            "city": city,
            "department": department,
            "job_title": job_title,
            "base_salary": salary,
            "hire_date": start_date.strftime("%Y-%m-%d")
        }
        dim_employees_rows.append(record)

    # 3. Data Export
    file_name = f"dim_employees_{language}.{file_format}"
    columns = dim_employees_rows[0].keys()

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=separator)
        writer.writeheader()
        writer.writerows(dim_employees_rows)

    print(f"""
    =========================================
    [*] SUCCESS! Dataset generation complete.
    =========================================
    - File Name: {file_name}
    - Format:    {file_format.upper()}
    - Records:   {len(dim_employees_rows)}
    - Delimiter: '{separator}'
    - Language:  '{language}'
    =========================================
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BI Datasets Generator - Portfolio")
    
    parser.add_argument('--format', type=str, choices=['csv', 'txt'], default='csv',
                        dest='file_format', help="Output file format (csv or txt)")
    
    parser.add_argument('--sep', type=str, default=',',
                        dest='separator', help="Column separator character (e.g. ',' or ';')")
    
    parser.add_argument('--lang', type=str, choices=['es', 'en'], default='en',
                        dest='language', help="Language of the generated data (es or en)")
                        
    parser.add_argument('--rows', type=int, default=30,
                        dest='num_rows', help="Number of records to generate")

    args = parser.parse_args()

    print("Starting data generation...")
    generate_data(
        file_format=args.file_format, 
        separator=args.separator, 
        language=args.language,
        num_rows=args.num_rows
    )