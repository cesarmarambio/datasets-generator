import argparse
import csv

# Importamos nuestra lógica de negocio aislada desde el nuevo paquete
from models.employees import get_employee_data

def export_data(data, file_name, file_format, separator):
    """
    Se encarga exclusivamente de escribir el archivo físico.
    """
    if not data:
        print("[-] Error: No data to export.")
        return

    columns = data[0].keys()

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=separator)
        writer.writeheader()
        writer.writerows(data)

def main():
    parser = argparse.ArgumentParser(description="BI Datasets Generator - Portfolio")
    
    # Nuevo argumento para elegir el dominio de datos
    parser.add_argument('--domain', type=str, choices=['employees'], default='employees',
                        dest='domain', help="Data domain to generate (e.g., employees)")
    
    parser.add_argument('--format', type=str, choices=['csv', 'txt'], default='csv',
                        dest='file_format', help="Output file format (csv or txt)")
    
    parser.add_argument('--sep', type=str, default=',',
                        dest='separator', help="Column separator character (e.g. ',' or ';')")
    
    parser.add_argument('--lang', type=str, choices=['es', 'en'], default='en',
                        dest='language', help="Language of the generated data (es or en)")
                        
    parser.add_argument('--rows', type=int, default=30,
                        dest='num_rows', help="Number of records to generate")

    args = parser.parse_args()

    print(f"[*] Starting data generation for domain: '{args.domain.upper()}'...")

    # 1. Enrutamiento: Elegimos qué modelo llamar según el dominio seleccionado
    if args.domain == 'employees':
        dataset = get_employee_data(language=args.language, num_rows=args.num_rows)
        file_name = f"dim_{args.domain}_{args.language}.{args.file_format}"
    
    # 2. Exportación: Pasamos los datos crudos a la función que crea el archivo
    export_data(dataset, file_name, args.file_format, args.separator)

    print(f"""
    =========================================
    [*] SUCCESS! Dataset generation complete.
    =========================================
    - File Name: {file_name}
    - Format:    {args.file_format.upper()}
    - Records:   {len(dataset)}
    - Delimiter: '{args.separator}'
    - Language:  '{args.language}'
    =========================================
    """)

if __name__ == "__main__":
    main()