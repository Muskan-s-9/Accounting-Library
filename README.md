# Accounting Library Repository

## Folder Structure

### 1. A_Rule_Engine
**Purpose:**
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
**Purpose:**
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

### 3. C_Organization_data
**Purpose:**
- Stores organized templates for purchase and sales data, along with sample invoice files

**Key Files:**
- `Purchases_template.xlsx`: Template for recording purchase data in a structured format.
- `Sales_template.xlsx` : Template for recording sales data
- `Invoice_1.pdf`: Example invoices for purchases or sales, used for validation or reference.
  
---

### 3.  D_Process_1_Data_Processing
**Purpose:**
- Templates and references for processing data related to expenses, income, and capital invoices.

**Key Files:**
- `Expense_Template.xlsx`: Template for capturing expense details.
- `Income_Template.xlsx` : Template for recording income transactions.
- `Capital_Invoice.pdf`: Template for documenting capital-related invoices.

---

### 3.  F_Process_3_Reporting
**Purpose:**
- Contains templates for generating accounting reports and dashboards..

**Key Files:**
- `Profit_Loss_Template.xlsx`: Template for profit and loss statements.
- `Balance_Sheet_Template.xlsx` : Template for creating balance sheets.






