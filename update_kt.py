import os
import re

base_names = ['CCorePluginResources', 'CertPathReviewerMessages', 'ChangeGeneratorMessages', 'commonMessages', 'ComposePreviewBundle', 'CoreModelMessages', 'DfsText', 'ErrorPane', 'FastPreview', 'GlancePreviewBundle', 'GoogleLoginBundle', 'JGitText', 'LiveEdit', 'LoginPane', 'message', 'Messages', 'MessagesBundle', 'plugin', 'PreviewBundle', 'RepoText', 'SearchField', 'SettingsModelMessages', 'SshdText', 'strings', 'swingx', 'SWTMessages', 'Texts', 'TipOfTheDay', 'UtilMessages', 'WearBundle']

kt_path = r'androidstudio_koreanlanguagepack\src\main\kotlin\org\jetbrains\plugins\koreanlanguagepack\KoreanLanguagePackBundle.kt'

with open(kt_path, 'r', encoding='utf-8') as f:
    kt_content = f.read()

lines_to_add = []
for name in base_names:
    if f'internal object {name} ' not in kt_content and f'internal object {name}{{ ' not in kt_content and f'internal object {name}\n' not in kt_content:
        # Generate upper snake case securely
        # Make CCore -> C_CORE, but just use simple regex for now
        # Actually a standard camel to snake:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        upper_snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()
        
        lines_to_add.append('\n')
        lines_to_add.append('// ' + '='*76)
        lines_to_add.append(f'// {name}')
        lines_to_add.append('// ' + '='*76)
        lines_to_add.append('@NonNls')
        lines_to_add.append(f'private const val {upper_snake}_BUNDLE = "messages.{name}"')
        lines_to_add.append('')
        lines_to_add.append(f'internal object {name} {{')
        lines_to_add.append('    @JvmStatic')
        lines_to_add.append(f'    fun message(@PropertyKey(resourceBundle = {upper_snake}_BUNDLE) key: String, vararg params: Any): @Nls String {{')
        lines_to_add.append(f'        return DynamicBundle.getMessage({upper_snake}_BUNDLE, key, *params)')
        lines_to_add.append('    }')
        lines_to_add.append('')
        lines_to_add.append('    @JvmStatic')
        lines_to_add.append(f'    fun messagePointer(@PropertyKey(resourceBundle = {upper_snake}_BUNDLE) key: String, vararg params: Any): Supplier<@Nls String> {{')
        lines_to_add.append(f'        return DynamicBundle.getLazyMessage({upper_snake}_BUNDLE, key, *params)')
        lines_to_add.append('    }')
        lines_to_add.append('}')

if lines_to_add:
    with open(kt_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(lines_to_add) + '\n')
    print("Kotlin file successfully updated!")

# Also do plugin.xml
xml_path = r'androidstudio_koreanlanguagepack\src\main\resources\META-INF\plugin.xml'
with open(xml_path, 'r', encoding='utf-8') as f:
    xml_lines = f.readlines()

new_xml_lines = []
for name in base_names:
    found = any(f'<resource-bundle>messages.{name}</resource-bundle>' in line for line in xml_lines)
    if not found:
        new_xml_lines.append(f'        <resource-bundle>messages.{name}</resource-bundle>\n')

if new_xml_lines:
    # Find </extensions> to insert before it
    insert_idx = -1
    for i, line in enumerate(xml_lines):
        if '</extensions>' in line:
            insert_idx = i
            # if we have multiple </extensions>, we probably want the first one that has resource-bundle
            # let's just insert at the last one.
    if insert_idx > -1:
        xml_lines = xml_lines[:insert_idx] + new_xml_lines + xml_lines[insert_idx:]
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.writelines(xml_lines)
        print("XML file successfully updated!")

