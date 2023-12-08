# Manufacturing Data Tracker

This application allows the creation of a Pandas dataset and the generation of a CSV file with the dataset. If the file doesn't exist, it will create a new `data.csv` file in the folder. If it's a subsequent insertion, it will only add the newly entered values to the existing `data.csv` file.

### Data Input Fields:

1. **Role**: Selectable through a dropdown menu.
2. **Shift**: Selectable through a dropdown menu.
3. **KG-00000000000 (Job Name)**: Accepts various input formats, converts to "KG-00000000000."
   - Example Formats: 00000000, kG00000000, kG-00000000, Kg-00000000, g-00000000, k-00000000.
4. **Sales Order**: Accepts input with 3 letters followed by numbers.
   - Example: aal123456789, apl123456789.
5. **Marcatura KG (a job may consist of multiple markings)**: Accepts specific formats.
   - Example Formats: AB-302bc, aB302, AB-302, AB302, A-302bc, a-302bc, 302bc, 302.
6. **Pieces**: Accepts 4 digits for pieces.
7. **Surname**: Accepts a capitalized format for single words or capitalizes the initials for two-word surnames.
   - Example: Smith, Johnson, McQueen.
  
### Additional Features:

- **Checkbox Locks**: Allow locking the cell with the text present in it. When pressing the "Asporta" button to transform the data into a dataset in the CSV, the input data will be deleted. A pop-up will confirm the successful data upload.

### Input Validation:

- **Popup Errors**: In case of incorrect input formats, pop-up errors will guide the user, ensuring correct data entry.

This Manufacturing Data Tracker facilitates data entry for manufacturing processes, ensuring consistency and accuracy in data storage.
