import xml.etree.ElementTree as ET
import os

# Salesforceのメタデータタイプのリスト
metadata_types = ['ApexClass',    'ApexTrigger',    'CustomObject' ]

# マニフェストファイルのルート要素を作成する
root= ET.Element('Package')
root.set('xmlns', 'http://soap.sforce.com/2006/04/metadata')

# メタデータタイプごとにファイル名を取得し、マニフェストファイルに追加する
for metadata_type in metadata_types:
    directory= metadata_type + 's'
    for filename in os.listdir(directory):
        if filename.endswith('.cls') or filename.endswith('.trigger') or filename.endswith('.object'):
            member= filename[:-4]
            member_element= ET.SubElement(root, 'types')
            member_element.append(ET.Element('members'))
            member_element.find('members').text= member
            member_element.append(ET.Element('name'))
            member_element.find('name').text= metadata_type

# バージョン情報を追加する
version_element= ET.SubElement(root, 'version')
version_element.text= '53.0'

# マニフェストファイルを保存する
tree= ET.ElementTree(root)
tree.write('package.xml', encoding='UTF-8', xml_declaration=True)
