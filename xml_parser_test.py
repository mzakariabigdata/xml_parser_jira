# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
import xml.etree.ElementTree as etree
from io import BytesIO

k = []

"""
root = ET.parse(file).getroot()
    for elem in root.findall(tag):
        root.remove(elem)
    tree = ET.ElementTree(root)
    tree.write("out.xml")
"""

def iterparse_and_decode_n1():
    events = "start", "start-ns", "end-ns"
    root = None
    ns_map = []
    for event, elem in etree.iterparse('a_b.xml', events):
        print(elem.tag)
        if event == "start-ns":
            ns_map.append(elem)
    print(ns_map)

#iterparse_and_decode_n1()
def iterparse_and_decode_n():
    f = BytesIO()
    #et.write(f, encoding='utf-8', xml_declaration=True) 
    #print(f.getvalue())  # your XML file, encoded as UTF-8
    for event, elem in etree.iterparse('a_b.xml', events=('start', 'end')):
        #v = etree.tostring(elem, sys.stdout.encoding, xml_declaration=False, method="xml", short_empty_elements=False).decode(sys.stdout.encoding)
        et = ET.ElementTree(elem)
        et.write(f, encoding='utf-8', xml_declaration=False) 
        print(f.getvalue())
        elem.clear()
        #print("---------", v)

#iterparse_and_decode_n()

def iterparse_and_decode():
    #i = 0
    for event, elem in etree.iterparse('entities_pddf.xml', events=('start', 'end', 'start-ns', 'end-ns')):
        if elem.tag == 'Action' and event == 'start' :
            #i = i +1
            #if i==4 : return
            #print(elem.tag, elem.attrib)
            v = etree.tostring(elem, sys.stdout.encoding, xml_declaration=False, method="xml", short_empty_elements=False).decode(sys.stdout.encoding)
            print(v)
#root = ET.parse('entities_pddf.xml').getroot()
#print (len(root.findall('Action')))
iterparse_and_decode()

"""
for elem in root.findall('ChangeItem'):
    root.remove(elem)

(root)
"""

"""
for elem in root.findall('ChangeItem'):
    root.remove(elem)
tree = ET.ElementTree(root)
# And write to file!
tree.write("out.xml")
"""

"""
return all tag
"""
"""
elemList_type = []

root_pddf = ET.parse('entities_mini.xml').getroot()

for elem in root_pddf.iter():
    elemList_type.append(elem.tag)

# print len of list
print(len(elemList_type))

# now I remove duplicities - by convertion to set and back to list
elemList_type = list(set(elemList_type))

# Just printing out the result
print(elemList_type)
"""

"""
project
"""
"""
def return_elem_prod(tag):
    root_prod = ET.parse('entities_mini.xml').getroot()
    for elem in root_prod.iter():
        if elem.tag == tag:
            print ('prod : {}\n{}'.format(tag, elem.attrib))
            return

def return_elem_pddf(tag):
    root_pddf = ET.parse('entities_pddf.xml').getroot()
    for elem in root_pddf.iter():
        if elem.tag == tag:

            print ('pddf : {}\n{}'.format(tag, elem.attrib))
            return

return_elem_prod('Project')

return_elem_pddf('Project')
"""

"""
Get defference betwen two files
"""
"""
def get_list_tag(file): 
    elemList_type = []

    root = ET.parse(file).getroot()

    for elem in root.iter():
        elemList_type.append(elem.tag)

    # now I remove duplicities - by convertion to set and back to list
    elemList_type = list(set(elemList_type))

    # Just printing out the result
    return len(elemList_type), elemList_type


n_prod, l_prod = get_list_tag('entities_mini.xml')
n_pddf , l_pddf = get_list_tag('entities_pddf.xml')

print (n_pddf, l_pddf)
print ('\n\n', n_prod, l_prod)

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

print ('\n\n',sorted(Diff(l_prod, l_pddf) + Diff(l_pddf, l_prod)))
"""

"""
Number of tag
"""
"""
def number_tag(file, tag):
    elemList_type = []

    root_pddf = ET.parse(file).getroot()

    for elem in root_pddf.iter():
        if elem.tag == tag:
            elemList_type.append(elem.tag)

    # print len of list
    return len(elemList_type)

print ('Tag : {} : {}'.format( 'project' ,number_tag('entities_mini.xml', 'Project')))
"""

"""
remove tag and save to out.xml
"""
"""
def remove_tag(file, tag):
    root = ET.parse(file).getroot()
    for elem in root.findall(tag):
        root.remove(elem)
    tree = ET.ElementTree(root)
    tree.write("out.xml")

remove_tag('entities_pddf_test.xml', 'Project')
"""
def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

def save_tag_to_file(in_file, out_file, tag):
    root = ET.parse(in_file).getroot()
    list_tag = root.findall(tag)
    print(len(list_tag))
    # #list_tag = root.findall(tag)
    # for elem in root.iter():
    #     #print("elem = ", elem.tag)
    #     if elem.tag == tag:
    #         #print("delete it", elem)
    #         root.remove(elem)
    # tree = ET.ElementTree(root)
    # # And write to file!
    # #print ( tag, len(list_tag))
    # tree.write(out_file)

def save_tag_to_file_v1(in_file, out_file, tag):
    #root = ET.iterparse(in_file).getroot()
    root = ET.iterparse(in_file)
    for event, elem in root:
        print(f"event = {event}, element = {elem}")
        if elem.tag == tag:
            print(elem.tag)
            #root.remove(elem)
    # tree = ET.ElementTree(root)
    # tree.write(root)
#save_tag_to_file_v1("a_b.xml", "b.xml", "b")
#save_tag_to_file("entities_pddf.xml", "entities_pddf_to_prod.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod.xml", "entities_pddf_to_prod_v1.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v1.xml", "entities_pddf_to_prod_v2.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v2.xml", "entities_pddf_to_prod_v3.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v3.xml", "entities_pddf_to_prod_v4.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v4.xml", "entities_pddf_to_prod_v5.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v5.xml", "entities_pddf_to_prod_v6.xml", 'Action')
#save_tag_to_file("entities_pddf_to_prod_v6.xml", "entities_pddf_to_prod_v7.xml", 'action')



def number_tag(file, tag):
    elemList_type = []

    root_pddf = ET.parse(file).getroot()

    for elem in root_pddf.iter():
        if elem.tag == tag:
            elemList_type.append(elem.tag)

    # print len of list
    return len(elemList_type)

def return_elem_pddf(tag):
    root_pddf = ET.parse('entities_pddf.xml').getroot()
    for elem in root_pddf.iter():
        if elem.tag.lower() == tag:

            print ('pddf : {}\n{}'.format(tag, elem.attrib))
            return

def return_elem_prod(tag):
    tag = tag.lower()
    root_prod = ET.parse('entities_mini.xml').getroot()
    for elem in root_prod.iter():
        if elem.tag.lower() == tag:
            print ('prod : {}\n{}'.format(tag, elem.attrib))
            return
        


def get_list_tag(file): 
    elemList_type = []

    root = ET.parse(file).getroot()

    for elem in root.iter():
        elemList_type.append(elem.tag)

    # now I remove duplicities - by convertion to set and back to list
    elemList_type = list(set(elemList_type))

    # Just printing out the result
    return len(elemList_type), elemList_type

def get_list_tag_has_attrib(file, attri): 
    elemList_type = []

    root = ET.parse(file).getroot()

    for elem in root.iter():
        if elem.tag not in elemList_type:
            res = dict(filter(lambda item: attri in item[0], elem.attrib.items()))
            if bool(res) or (attri in elem.tag.lower()):
                elemList_type.append(elem.tag)
            #     print (elemList_type, elem.attrib, res, not res, type(res))
            # return

    # now I remove duplicities - by convertion to set and back to list
    elemList_type = list(set(elemList_type))

    # Just printing out the result
    return len(elemList_type), attri, sorted(elemList_type) 


def get_valur_of_attri_for_a_apesific_tag_(file, tag, attri): 
    elemList_type = []

    root = ET.parse(file).getroot()

    list_tag = root.findall(tag)
    n=1
    for elem in list_tag:
        elemList_type.append(elem.attrib.get(attri))

    # Just printing out the result
    return len(elemList_type), tag, attri, sorted(elemList_type)

def get_one_valur_of_attri_for_a_apesific_tag_(file, tag, attri, val): 
    elemList_type = []

    root = ET.parse(file).getroot()

    list_tag = root.findall(tag)
    for elem in list_tag:
        if elem.attrib.get(attri) == val:
            return tag, elem.attrib


# 18800

#print (get_one_valur_of_attri_for_a_apesific_tag_('entities_pddf.xml', 'User', 'id', '275238'))
#print (get_one_valur_of_attri_for_a_apesific_tag_('entities_mini.xml', 'Project', 'id', '10000'))

#n, p, id, ll = get_valur_of_attri_for_a_apesific_tag_('entities_pddf.xml', 'Project', 'id')
#n1, p1, id1, ll1 = get_valur_of_attri_for_a_apesific_tag_('entities_mini.xml', 'Project', 'id')

#r = Diff(ll, ll1)
#print (len(ll1), len(set(ll1)))

#print (get_list_tag_has_attrib('entities_pddf.xml', 'body'))
#return_elem_prod('action')
#return_elem_pddf('action')

#save_tag_to_file('entities_mini.xml', 'out_directory.xml','directory')