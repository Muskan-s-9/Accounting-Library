# Accounting Library 


### 1. A_Rule_Engine

- Contains Python scripts implementing rule-based logic for accounting processes.

**Key Files:**
- [`A_3_Debit_Credit_Rule.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_3_Debit_Credit_Rule.py): Applies the Debit and Credit Rule to Journal Entries.
  
- [`A_1_Ledger_Library.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_1_Ledger_Library.py): Creates ledgers and saves them to CSV files. You can add new ledgers in the configuration dictionary.
  
- [`A_2_Credit_Note_Journal_Entry.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_2_Credit_Note_Journal_Entry.py): Processes Credit Note Journal Entries using ledgers and credit note data in CSV format.
  
- [`A_2_Debit_Notes_Journal_Entry.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_2_Debit_Notes_Journal_Entry.py): Processes Debit Note Journal Entries using ledgers and debit note data in CSV format.
  
- [`A_2_Purchase_Journal_Entry.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_2_Purchase_Journal_Entry.py): Processes Purchase Journal Entries using ledgers and purchase data in CSV format.

- [`A_2_Sales_Journal_Entry.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/A_Rule_Engine/A_2_Sales_Journal_Entry.py): Processes Sales Journal Entries using ledgers and sales data in CSV format.

     

---

### 2. B_Setup

- Includes setup scripts and templates.

**Key Files:**
- [`Customize_Ledger_Library.py`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_1_Ledger_Setup/Customize_Ledger_Library.py): Adds any new ledgers encountered while passing journal entries
-  [`Sales_Ledger_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_3_Sales_Codes/Sales_Ledger_Entry.ipynb): Import all necessary modules and libraries to pass the sales journal entry and generate the report in CSV format

- [`Purchase_Ledger_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_4_Purchase_Codes/Purchase_Ledger_Entry.ipynb): Import all necessary modules and libraries to pass the Purchase journal entry and generate the report in CSV format
  
- [`Income_Ledger_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_5_Income_Codes/Income_Ledger_Entry.ipynb):Import all necessary modules and libraries to pass the Income journal entry and generate the report in CSV format
  
- [`Expense_Ledger_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_6_Expense_Code/Expense_Ledger_Entry.ipynb): Import all necessary modules and libraries to pass the Expense journal entry and generate the report in CSV format
  
- [`Credit_Notes_Journal_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_7_Credit_Notes_Code/Credit_Notes_Journal_Entry.ipynb): Import all necessary modules and libraries to pass the credit notes journal entry and generate the report in CSV format
  
- [`Debit_Note_Ledger_Entry.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_8_Debit_Notes_Code/Debit_Note_Ledger_Entry.ipynb):
  Import all necessary modules and libraries to pass the debit notes journal entry and generate the report in CSV format

  **Reporting:**
  - [`Balance_Sheet.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_9_Reporting_Codes/Balance_Sheet.ipynb)
  - [`Detail_Balance_Sheet.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_9_Reporting_Codes/Detail_Balance_Sheet.ipynb)
  - [`PNL.ipynb`](https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/B_Setup/B_9_Reporting_Codes/PNL.ipynb)
---


### 3.  D_Process_1_Data_Processing

- Templates and references for processing data related to expenses, income, and capital invoices.

**Key Files:**
 - `Expense`: Folder that contains  Expense invoices data in excel format.
   -  sample expense data: https://docs.google.com/spreadsheets/d/1aKeKkcJGzM-FCYh_v8WybbpOK4byrimV/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
 
 - `Income`: Folder that contains  Income invoices data in excel format.
    - sample income  data: https://docs.google.com/spreadsheets/d/12WYOOM48cMxvuHGMdp6who2ygX07Hngn/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
 
 - `Purchase`: Folder that contains  Purchase invoices data in excel format.
    - sample purchase data: https://docs.google.com/spreadsheets/d/14eH3a0Wxp6o2mLHyytZJYomckySOWWI0/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
 
 - `Sales`: Folder that contains  Sales invoices data in excel format.
    - sample sales data: https://docs.google.com/spreadsheets/d/1PKT9Ga4qDfH6nWk-4O61vOeqmSGxhrLg/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
 
 - `Capital`: Folder that contains  Capital invoices data in excel format.
    - sample Capital data: https://docs.google.com/spreadsheets/d/1sac4d3kWTNMQ81WuDPi6acKs6yVWGPEl/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
---

### 4. E_Process_2_Accounting

- Contains all the Excel outputs of accounting data

  **E_Step_2_Journal_Entry**
    - `Purchase_Notes_Journal_Entry_Output` :https://docs.google.com/spreadsheets/d/1bWTpM98AaSmtQrJ-avAq9HXmZ176a7oc/edit?    usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
      
    - `Sales_Notes_Journal_Entry_Output` : https://docs.google.com/spreadsheets/d/1RIfZ-zFtqGhkZwRxjMCCDetnbAr_4XNw/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
      
    - `Credit_Notes_Journal_Entry_Output` :https://docs.google.com/spreadsheets/d/17b2lF_h5upRlOgPu2k6VmjZO7F3b4BlX/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
  
    - `Debit_Notes_Journal_Entry_Output` :https://docs.google.com/spreadsheets/d/1qxD8hp_afhMNPnAP9lnKjl1_Z2TO3kdx/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
 
  **E_Step_3_Consolidation**
   - [`Merge_all_journal_entry_excel.ipynb`]('https://github.com/Muskan-s-9/Accounting-Library/blob/main/Accounting_Library/E_Process_2_Accounting/E_Step_3_Consolidation/Merge_all_journal_entry_excel.ipynb') : It will take all the Excel files and generate a consolidated Excel file.
     -  https://docs.google.com/spreadsheets/d/1VdYkSqf0eIai1yFuELKtKyOyUn9_f8NY/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true
    


    
---



### 5.  J_Organization_Output

- Contains  Balance sheet, Ledgers, PNL , Trail Balcance

**Key Files:**
- [`J_1_Balance_Sheet`](https://github.com/Muskan-s-9/Accounting-Library/tree/main/Accounting_Library/J_Organization_Output/J_1_Balance_Sheet):
    - https://docs.google.com/spreadsheets/d/1n37D9PpMHLNjBpFErkLoqnzL-AREfFOJ/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true

- [`J_2_PNL`](https://github.com/Muskan-s-9/Accounting-Library/tree/main/Accounting_Library/J_Organization_Output/J_2_PNL)
    - https://docs.google.com/spreadsheets/d/1Rn9f0vg-GI_AIRIyR3X_AkvVO7LdU4Hz/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true

- [`J_3_Ledger`](https://github.com/Muskan-s-9/Accounting-Library/tree/main/Accounting_Library/J_Organization_Output/J_3_Ledger)
    - https://docs.google.com/spreadsheets/d/1_IzQS7_XPa9DXt0160PF1GqT342JjKBB/edit?usp=sharing&ouid=102056670822337622463&rtpof=true&sd=true

- [`J_4_TB`](https://github.com/Muskan-s-9/Accounting-Library/tree/main/Accounting_Library/J_Organization_Output/J_4_TB)
    - https://drive.google.com/drive/folders/1Xk5EeMk9fQJsBin0-JfOufDQUcwWcX-3?usp=sharing





