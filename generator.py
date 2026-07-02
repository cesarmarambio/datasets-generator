import argparse
import csv
import random
import uuid
import os
from datetime import datetime, timedelta

def generate_data(file_format, separator, language):
    # Base configuration
    start_date = datetime(2023, 1, 1)
    initial_headcount = 30
    
    # 1. Localization Dictionaries (Data Language)
    if language == 'es':
        departments = ["Tecnologia", "Finanzas", "Recursos Humanos", "Operaciones", "Comercial"]
        first_names = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Claudia", "Diego", "Patricia"]
        last_names = ["Munoz", "Rojas", "Diaz", "Perez", "Soto", "Contreras", "Silva", "Martinez"]
        job_titles = ["Data Engineer", "Analista BI", "Gerente", "Coordinador", "Ejecutivo"]
    else:
        departments = ["Technology", "Finance", "Human Resources", "Operations", "Sales"]
        first_names = ["John", "Mary", "Charles", "Anna", "Peter", "Chloe", "James", "Patricia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        job_titles = ["Data Engineer", "BI Analyst", "Manager", "Coordinator", "Executive"]

    # 2. Data Generation (Simplified for Employees Dimension)
    dim_employees_rows = []
    
    for i in range(1, initial_headcount + 1):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        department = random.choice(departments)
        job_title = random.choice(job_titles)
        salary = random.randint(800000, 3500000)
        
        record = {
            "surrogate_id": str(uuid.uuid4())[:8],
            "natural_employee_id": i,
            "full_name": full_name,
            "department": department,
            "job_title": job_title,
            "base_salary": salary,
            "hire_date": start_date.strftime("%Y-%m-%d")
        }
        dim_employees_rows.append(record)

    # 3. Data Export
    file_name = f"dim_employees_{language}.{file_format}"
    
    # Extract column names for the header
    columns = dim_employees_rows[0].keys()

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=separator)
        writer.writeheader()
        writer.writerows(dim_employees_rows)

    print(f"[*] Success! File generated: {file_name}")
    print(
        f"[*] Records: {len(dim_employees_rows)} "
        f"| Delimiter: '{separator}' "
        f"| Language: '{language}' "
        f"| Format: '{file_format}'"
    )

if __name__ == "__main__":
    # CLI arguments configuration
    parser = argparse.ArgumentParser(description="BI Datasets Generator - Portfolio")
    
    parser.add_argument('--format', type=str, choices=['csv', 'txt'], default='csv',
                        dest='file_format', help="Output file format (csv or txt)")
    
    parser.add_argument('--sep', type=str, default=',',
                        dest='separator', help="Column separator character (e.g. ',' or ';')")
    
    parser.add_argument('--lang', type=str, choices=['es', 'en'], default='en',
                        dest='language', help="Language of the generated data (es or en)")

    args = parser.parse_args()

    print("Starting data generation...")
    generate_data(file_format=args.file_format, separator=args.separator, language=args.language)