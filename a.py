import pandas as pd

# Read the data from the TXT files into lists
with open('names.txt', 'r') as f:
    names = f.read().splitlines()

with open('number.txt', 'r') as f:
    phone_numbers = f.read().splitlines()

with open('jobs.txt', 'r') as f:
    jobs = f.read().splitlines()

with open('address.txt', 'r') as f:
    addresses = f.read().splitlines()

# Create a DataFrame using the data
data = {
    'Person Name': names,
    'Phone Number': phone_numbers,
    'Job': jobs,
    'Address': addresses
}

df = pd.DataFrame(data)

# Create a new Excel file
excel_file = 'person_data.xlsx'
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# Write the DataFrame to the Excel sheet
df.to_excel(writer, sheet_name='Person Data', index=False)

# Customize the column headers
workbook = writer.book
worksheet = writer.sheets['Person Data']

header_format = workbook.add_format({'bold': True, 'border': 1})

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Save the Excel file
writer.save()
