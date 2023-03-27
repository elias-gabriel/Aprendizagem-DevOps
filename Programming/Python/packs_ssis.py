import os
import xml.etree.ElementTree as ET
import csv
import re

def extract_schema_and_filetype(component):
    open_rowset_property = component.find('./properties/property[@name="OpenRowset"]')
    connection_string_property = component.find('./properties/property[@name="ConnectionString"]')
    if open_rowset_property is not None:
        open_rowset_value = open_rowset_property.text
        if open_rowset_value:
            schema_match = re.match(r"^(.+?)[\s\.](?=[^\.]+?$)", open_rowset_value)
            if schema_match:
                schema = schema_match.group(1)
            else:
                schema = None
        else:
            schema = None
    else:
        schema = None

    if connection_string_property is not None:
        connection_string = connection_string_property.text
        file_type_match = re.search(r"\.(\w+);?", connection_string)
        if file_type_match:
            file_type = file_type_match.group(1)
        else:
            file_type = None
    else:
        file_type = None

    return schema, file_type

def extract_sources_and_destinations(tree):
    sources = []
    destinations = []

    for component in tree.findall('.//component'):
        component_name = component.get('name')
        component_classID = component.get('componentClassID')
        schema, file_type = extract_schema_and_filetype(component)

        if 'Source' in component_classID:
            sources.append((file_type, component_name))  # Set schema to file_type for sources
        elif 'Destination' in component_classID:
            destinations.append((schema, component_name))

    return sources, destinations

def get_dtsx_info(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    subpackages = []

    for execute_package_task in root.findall('.//ExecutePackageTask'):
        package_name = execute_package_task.find('PackageName').text
        subpackages.append(package_name)

    return subpackages

folder_path = r''
dtsx_files = [file for file in os.listdir(folder_path) if file.endswith('.dtsx')]

csv_output_file = 'dtsx_info.csv'
with open(csv_output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['DTSX_File', 'Referenced_Package', 'Source/Destination', 'Schema', 'Component_Name', 'Full_Name'])

    for dtsx_file in dtsx_files:
        file_path = os.path.join(folder_path, dtsx_file)
        subpackages = get_dtsx_info(file_path)

        for package in subpackages:
            subpackage_path = os.path.join(folder_path, package)
            if os.path.exists(subpackage_path):
                tree = ET.parse(subpackage_path)
                sources, destinations = extract_sources_and_destinations(tree)

                for schema, source in sources:
                    full_name = f"{source}.{schema}" if schema else source
                    csv_writer.writerow([dtsx_file, package, 'Source', schema, source, full_name])

                for schema, destination in destinations:
                    full_name = f"[{schema}].[{destination}]" if schema else destination
                    full_name = full_name.replace("[[", "[").replace("]]", "]")
                    csv_writer.writerow([dtsx_file, package, 'Destination', schema, destination, full_name])
            else:
                csv_writer.writerow([dtsx_file, package, 'Subpackage not found', '', '', ''])
