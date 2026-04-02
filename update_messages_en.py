import os
import re

kt_path = r'androidstudio_koreanlanguagepack\src\main\kotlin\org\jetbrains\plugins\koreanlanguagepack\KoreanLanguagePackBundle.kt'

with open(kt_path, 'r', encoding='utf-8') as f:
    kt_content = f.read()

name = 'MessagesBundle_en'

if f'internal object {name} ' not in kt_content and f'internal object {name}: ' not in kt_content:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    upper_snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()
    bundle_val_name = upper_snake + '_BUNDLE'
    
    # Needs to handle _EN special naming
    bundle_val_name = bundle_val_name.replace('_EN_BUNDLE', '_EN_BUNDLE')
    
    lines_to_add = []
    lines_to_add.append('')
    lines_to_add.append('// ' + '='*76)
    lines_to_add.append(f'// {name}')
    lines_to_add.append('// ' + '='*76)
    lines_to_add.append('@NonNls')
    lines_to_add.append(f'private const val {bundle_val_name} = "messages.{name}"')
    lines_to_add.append('')
    lines_to_add.append(f'internal object {name} : DynamicBundle({bundle_val_name}) {{')
    lines_to_add.append('    @JvmStatic')
    lines_to_add.append(f'    fun message(@PropertyKey(resourceBundle = {bundle_val_name}) key: String, vararg params: Any): @Nls String {{')
    lines_to_add.append('        return getMessage(key, *params)')
    lines_to_add.append('    }')
    lines_to_add.append('')
    lines_to_add.append('    @JvmStatic')
    lines_to_add.append(f'    fun messagePointer(@PropertyKey(resourceBundle = {bundle_val_name}) key: String, vararg params: Any): Supplier<@Nls String> {{')
    lines_to_add.append('        return getLazyMessage(key, *params)')
    lines_to_add.append('    }')
    lines_to_add.append('}')

    # Find the last closing brace in the file
    with open(kt_path, 'w', encoding='utf-8') as f:
         f.write(kt_content + '\n'.join(lines_to_add) + '\n')
    print("KT successfully rewritten!")


xml_path = r'androidstudio_koreanlanguagepack\src\main\resources\META-INF\plugin.xml'
with open(xml_path, 'r', encoding='utf-8') as f:
    xml_lines = f.readlines()

new_xml_lines = []
if f'<resource-bundle>messages.{name}</resource-bundle>' not in "".join(xml_lines):
    new_xml_lines.append(f'        <resource-bundle>messages.{name}</resource-bundle>\n')

if new_xml_lines:
    idx_ext = -1
    for i, line in enumerate(xml_lines):
        if '</extensions>' in line:
            idx_ext = i
    if idx_ext > -1:
        xml_lines = xml_lines[:idx_ext] + new_xml_lines + xml_lines[idx_ext:]
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.writelines(xml_lines)
        print("XML successfully rewritten!")
