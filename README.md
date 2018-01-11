# TTI ISO Website

This is the public website of the TTI Information Security Office, which includes the TTI security control catalog.

To update the controls in the catalog:

- Download the export report from TxDIR Archer GRC as an XML file and save the file (should be named `SearchResults.xml`) to the root site directory
- Run the `createData.py` script in Python; this will break the XML into individual JSON data files for each control
- Run the `createPages.sh` script in Bash; this will create individual HTML files for each control
- Serve content on a local Jekyll server to ensure the content rendered properly
- Commit the changes to the origin repository
