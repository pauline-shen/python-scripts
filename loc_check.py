import pandas as pd

def compare_excel_files(file1_path, file2_path, column_name):
    # Read the Excel files into DataFrames
    df1 = pd.read_excel(file1_path, engine='openpyxl')
    df2 = pd.read_excel(file2_path, engine='openpyxl')

    # Create sets of unique values from both columns
    set1 = set(df1[column_name].dropna())
    set2 = set(df2[column_name].dropna())

    # Find values in set1 that are not in set2
    diff_values_file1 = set1 - set2

    # Find values in set2 that are not in set1
    diff_values_file2 = set2 - set1

    # Filter rows with differences from both DataFrames
    diff_df_file1 = df1[df1[column_name].isin(diff_values_file1)]
    diff_df_file2 = df2[df2[column_name].isin(diff_values_file2)]

    return diff_df_file1, diff_df_file2

def generate_report(diff_df_file1, diff_df_file2, report_filename):
    # Write the results to a new Excel file
    with pd.ExcelWriter(report_filename, engine='openpyxl') as writer:
        diff_df_file1.to_excel(writer, sheet_name='Differences in File 1', 
index=False)
        diff_df_file2.to_excel(writer, sheet_name='Differences in File 2', 
index=False)

if __name__ == '__main__':
    file1_path = 'path/to/file1.xlsx'
    file2_path = 'path/to/file2.xlsx'
    column_name = 'column_name_to_compare'

    diff_df_file1, diff_df_file2 = compare_excel_files(file1_path, 
file2_path, column_name)

    report_filename = 'differences_report.xlsx'
    generate_report(diff_df_file1, diff_df_file2, report_filename)

