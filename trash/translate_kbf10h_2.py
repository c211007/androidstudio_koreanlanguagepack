import json

ko_dict = {
  "html.setter.parameter.type.must.be.equal.to.the.type.of.the.property.table.tr.td.expected.td.td.0.td.tr.tr.td.found.td.td.1.td.tr.table.html": "Setter 매개변수 유형은 속성의 유형과 같아야 합니다.<table><tr><td>예상:</td><td>{0}</td></tr><tr><td>발견:</td><td>{1}</td></tr></table>",
  "html.property.type.is.0.which.is.not.a.subtype.type.of.overridden.br.1.html": "속성 유형이 {0}이고 재정의된 <br/>{1}의 하위 유형이 아닙니다.",
  "html.return.types.of.inherited.members.are.incompatible.br.0.br.1.html": "상속된 멤버의 반환 유형이 호환되지 않습니다.<br/>{0},<br/>{1}",
  "html.return.type.is.0.which.is.not.a.subtype.of.overridden.br.1.html": "반환 유형이 ''{0}''이고 재정의된 <br/>{1}의 하위 유형이 아닙니다.",
  "html.loop.parameter.type.mismatch.table.tr.td.iterated.values.td.td.0.td.tr.tr.td.parameter.td.td.1.td.tr.table.html": "루프 매개변수 유형 불일치<table><tr><td>반복되는 값:</td><td>{0}</td></tr><tr><td>매개변수:</td><td>{1}</td></tr></table>",
  "html.type.argument.is.not.within.its.bounds.table.tr.td.expected.td.td.0.td.tr.tr.td.found.td.td.1.td.tr.table.html": "유형 인수가 범위를 벗어났습니다.<table><tr><td>예상:</td><td>{0}</td></tr><tr><td>발견:</td><td>{1}</td></tr></table>",
  "html.method.iterator.is.ambiguous.for.this.expression.ul.0.ul.html": "이 표현식에 대한 ''iterator()'' 메서드가 모호합니다.<ul>{0}</ul>",
  "html.getter.return.type.must.be.equal.to.the.type.of.the.property.table.tr.td.expected.td.td.0.td.tr.tr.td.found.td.td.1.td.tr.table.html": "Getter 반환 유형은 속성의 유형과 같아야 합니다.<table><tr><td>예상:</td><td>{0}</td></tr><tr><td>발견:</td><td>{1}</td></tr></table>",
  "html.type.inference.failed.0.html": "유형 유추 실패: {0}",
  "html.assignment.operators.ambiguity.all.these.functions.match.ul.0.ul.table.html": "할당 연산자가 모호합니다. 다음 함수가 모두 일치합니다.<ul>{0}</ul></table>",
  "html.type.mismatch.table.tr.td.required.td.td.0.td.tr.tr.td.found.td.td.1.td.tr.table.br.projected.type.2.restricts.use.of.br.3.html": "유형 불일치.<table><tr><td>필요:</td><td>{0}</td></tr><tr><td>발견:</td><td>{1}</td></tr></table><br />\\n프로젝트된 유형 {2}에서 <br />\\n{3}\\n의 사용을 제한합니다.",
  "html.type.mismatch.table.tr.td.required.td.td.0.td.tr.tr.td.found.td.td.1.td.tr.table.html": "유형이 일치하지 않습니다.<table><tr><td>필요:</td><td>{0}</td></tr><tr><td>발견:</td><td>{1}</td></tr></table>",
  "found.space": "발견:\\u0020",
  "required.space": "필요:\\u0020",
  "type.inference.failed.expected.type.mismatch": "유형을 유추하지 못했습니다. 예상 유형 불일치:\\u0020",
  "gutter.name.suspend.call": "호출 일시 중단",
  "the.feature.0.is.not.supported.in.k1.mode": "{0} 기능은 K1 모드에서 지원되지 않습니다."
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBaseFe10HighlightingBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 41-57)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
