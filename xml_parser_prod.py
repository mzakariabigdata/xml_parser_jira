# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys

def iterparse_and_decode():
    for event, elem in ET.iterparse('entities_pddf.xml', events=('start', 'end', 'start-ns', 'end-ns')):
        if elem.tag == 'Action' and event == 'start' :

            v = ET.tostring(elem, sys.stdout.encoding, xml_declaration=False, method="xml", short_empty_elements=False).decode(sys.stdout.encoding)
            print(v)

iterparse_and_decode()