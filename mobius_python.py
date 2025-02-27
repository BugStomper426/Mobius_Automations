import pandas as pd
import time as time

def mobius_txt_automation():
    # --- Step 1. Read the Excel file with DOC# values ---
    input_excel = 'Example_Input_Doc.xlsx'
    # input_excel = 'Input_Doc.xlsx'
    df_input = pd.read_excel(input_excel)
    doc_list = df_input['DOC#'].astype(str).tolist()
    # print(doc_list)

    # --- Step 2. Read the raw text file and prepare to parse it ---
    # with open('Raw_TXT_File.TXT', 'r') as f:
    with open('RAW_TXT_TEST.TXT', 'r') as f:
        lines = f.readlines()

    doc_rel_map = {}
    header_found = False
    doc_index = None
    rel_index = None


    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:
            continue

        tokens = line.split()  # Split the line into tokens based on whitespace

        # Check if this line is the header row by looking for both "DOC#" and "REL#"
        if "DOC#" in tokens and "REL#" in tokens:
            header_found = True
            doc_index = tokens.index("DOC#")
            rel_index = tokens.index("REL#")
            continue  # Skip processing the header row itself

        # Once the header is found, process subsequent lines as data rows
        if header_found and len(tokens) > max(doc_index, rel_index):
            # print(f"doc_index: {doc_index}, rel_index: {rel_index}")
            doc_value = tokens[doc_index - 1] #TKG98PJ each row following header row is not of equal length
            # print(f"doc_value: {doc_value}")
            rel_value = tokens[rel_index - 1] #TKG98PJ each row following header row is not of equal length
            # print(f"rel_value: {rel_value}")
            # Only record the mapping if the DOC# is in our input list
            # if doc_value == 'R858001337SHTG':
                # print(f"Found: {doc_value}")
            if doc_value in doc_list:
                doc_rel_map[doc_value] = rel_value

    # --- Step 3. Create and write the output ---
    output_df = pd.DataFrame(list(doc_rel_map.items()), columns=['DOC#', 'REL#'])
    output_df.to_excel('Example_Output_Doc.xlsx', index=False)

if __name__ == '__main__':
    start_time = time.time()
    mobius_txt_automation()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: ", elapsed_time)