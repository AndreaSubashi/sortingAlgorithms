import pandas as pd

def save_txt_to_excel(txt_filename, excel_filename):
    """
    Read data from a .txt file and save it to an Excel file.
    """
    # Read data from .txt file into a pandas DataFrame
    with open(txt_filename, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        parts = line.strip().split(', ')
        m = int(parts[0].split(': ')[1])
        n = int(parts[1].split(': ')[1])
        comparisons = int(parts[2].split(': ')[1])
        data.append((m, n, comparisons))
    df = pd.DataFrame(data, columns=['M', 'N', 'Comparisons'])

    # Write DataFrame to Excel file
    df.to_excel(excel_filename, index=False)

# Example usage
save_txt_to_excel('test_im_results.txt', 'Book2.xlsx')

