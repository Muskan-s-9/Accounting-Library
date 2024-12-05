import sys
import os
path = os.path.abspath(os.path.join('C:\\Users\\user\\', 'Downloads', 'Convert_pdf_file_into_the_excel_file', 'Rule_Setup', 'Accounting_Library'))
sys.path.append(path)

from A_Rule_Engine.A_2_Sales_Journal_Entry import JournalEntryProcessor
import pandas as pd

entry_df = pd.read_excel(path+'\E_Process_2_Accounting\E_Step_1_Common_Template\Sales_Common_Template.xlsx',engine='openpyxl')
config_df = pd.read_excel(path+'\B_Setup\B_1_Ledger_Setup\Output_Ledger_Library.xlsx',engine='openpyxl')

k  = {
    'J1 - Journal Number':[],
    'J2 - Date' :  [],
    'J3 - Invoice_Ref_Number' : [],
    'J4 - Ledger_Name' : [],
    'J6 - Dr Amount' : [],
    'J7 - Cr Amount' : [],
    'J9 - Description/Narration' : [],
}


journal_entry = JournalEntryProcessor(entry_df,config_df)
journal_entry.process_entries(k)

df = pd.DataFrame(k)
print(df)
