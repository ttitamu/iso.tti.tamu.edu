import glob
import json
import os, os.path, shutil
import xmltodict
import xml.etree
import xml.etree.ElementTree as ET

context = ET.iterparse('SearchResults.xml', events=('end', ))
ns = {'ns0': 'http://archertech.com/Print/Export'}

if os.path.exists("controls"):
	shutil.rmtree("controls")

if os.path.exists("_data/controls"):
	shutil.rmtree("_data/controls")

os.makedirs("controls")
os.makedirs("_data/controls")
for event, elem in context:
	procedure_ID = elem.find('ns0:Procedure_ID', ns)
	if procedure_ID != None:
		procedure_Name = elem.find('ns0:Procedure_Name', ns)
		xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
		xml += ET.tostring(elem)

		filename = format("_data/controls/" + procedure_ID.text + ".json")
		jsonString = json.dumps(xmltodict.parse(xml), indent=4)
		jsonString = jsonString.replace('ns0:', '')

		with open(filename, 'wb') as f:
			f.write(jsonString)

		filename = format("controls/" + procedure_ID.text) 
		htmlString = "---\nlayout: control\ntitle: " + procedure_ID.text + " " + procedure_Name.text + "\n---"
		with open(filename, 'wb') as f:
			f.write(htmlString)
