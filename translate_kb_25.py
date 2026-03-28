import json

ko_dict = {
  "introduce.0.as.subject.0.when": "''{0}''을(를) ''when''의 주체로 도입",
  "convert.call.chain.into.sequence.fix.text": "호출 체인을 'Sequence'로 변환",
  "call.chain.length.to.transform": "변환할 호출 체인 길이:",
  "call.chain.on.collection.could.be.converted.into.sequence.to.improve.performance": "컬렉션에 대한 호출 체인은 성능을 향상시키기 위해 'Sequence'로 변환할 수 있습니다.",
  "remove.redundant.call.fix.text": "중복 호출 제거",
  "rename.redundant.call.fix.text": "호출을 ''{0}''(으)로 변경",
  "call.chain.on.collection.type.may.be.simplified": "컬렉션 유형에 대한 호출 체인을 간소화할 수 있습니다.",
  "0.call.could.be.simplified.to.1": "{0} 호출을 {1}(으)로 간소화할 수 있습니다.",
  "simplify.call.fix.text": "''{0}'' 호출을 ''{1}''(으)로 변환",
  "simplify.call.chain.fix.text": "호출 체인을 ''{0}''(으)로 병합",
  "call.on.collection.type.may.be.reduced": "컬렉션 유형에 대한 호출을 축소할 수 있습니다.",
  "redundant.call.on.collection.type": "컬렉션 유형에 대한 중복 호출",
  "this.call.is.redundant.with": "이 호출은 ?.와 중복됩니다.",
  "redundant.call.on.not.null.type": "null 불가능한 유형에 대한 중복 호출",
  "call.on.not.null.type.may.be.reduced": "null 불가능한 유형에 대한 호출을 축소할 수 있습니다.",
  "replace.total.order.equality.with.ieee.754.equality": "전순서(total order) 동등성을 IEEE 754 동등성으로 바꾸기",
  "replace.with.binary.operator": "이항 연산자로 바꾸기",
  "call.replaceable.with.binary.operator": "호출을 이항 연산자로 바꿀 수 있습니다.",
  "replace.get.or.set.call.with.indexing.operator": "get 또는 set 호출을 인덱싱 연산자로 바꾸기",
  "should.be.replaced.with.indexing": "인덱싱으로 바꿔야 합니다.",
  "explicit.0.call": "명시적인 ''{0}'' 호출",
  "replace.0.call.with.indexing.operator": "''{0}'' 호출을 인덱싱 연산자로 바꾸기",
  "function.returning.0.with.a.name.that.does.not.end.with.1": "이름이 {1}(으)로 끝나지 않는 {0}을(를) 반환하는 함수",
  "add.call.or.unwrap.type.fix.text": "함수 결과에 ''.{0}()'' 추가 (사용 사이트가 손상됨!)",
  "add.call.or.unwrap.type.fix.text1": "''{0}'' 반환 유형 언래핑 (사용 사이트가 손상됨!)",
  "reports.only.function.calls.from.kotlinx.coroutines": "'kotlinx.coroutines'에서 온 함수 호출만 보고",
  "deferred.result.is.never.used": "'Deferred' 결과가 사용되지 않습니다.",
  "function.0.returning.1.without.the.corresponding": "''{3}''을(를) 반환하는 해당 함수 ''{2}'' 없이 ''{1}''을(를) 반환하는 함수 ''{0}''",
  "redundant.async.call.may.be.reduced.to.0": "중복된 ''async'' 호출을 ''{0}''(으)로 축소할 수 있습니다.",
  "redundant.runcatching.call.may.be.reduced.to.0": "중복된 ''runCatching'' 호출을 ''{0}''(으)로 축소할 수 있습니다.",
  "rename.to.fix.text": "''{0}''(으)로 이름 바꾸기",
  "rename.only.current.0": "현재 {0,choice,1#함수|2#속성}만 이름 바꾸기",
  "rename.base.0": "기본 {0,choice,1#함수|2#속성|3#멤버|4#메서드|11#함수|12#속성|13#멤버|14#메서드} 이름 바꾸기",
  "rename.declaration.title.0.implements.1.2.of.3": "{0}이(가) {3}의 {2}을(를) {1,choice,1#구현|2#재정의}합니다.",
  "rename.searching.for.all.overrides": "모든 재정의 검색 중",
  "rename.searching.for.super.declaration": "가장 깊은 상위 선언 검색 중",
  "title.rename.file": "파일 이름 바꾸기",
  "file.entity": "파일",
  "rename.file": "파일 이름 바꾸기",
  "rename.file.0": "파일 이름을 ''{0}''(으)로 변경",
  "title.rename.file.to": "파일 이름 바꾸기:",
  "wrap.with.coroutine.scope.fix.text": "함수 본문을 'coroutineScope { ... }'로 묶기",
  "wrap.with.coroutine.scope.fix.text2": "호출을 'coroutineScope { ... }'로 묶기",
  "wrap.with.coroutine.scope.fix.text3": "수신자를 제거하고 'coroutineScope { ... }'로 묶기",
  "wrap.with.coroutine.scope.fix.family.name": "coroutineScope로 묶기",
  "ambiguous.coroutinecontext.due.to.coroutinescope.receiver.of.suspend.function": "suspend 함수의 CoroutineScope 수신자로 인한 모호한 coroutineContext",
  "replace.with.kotlin.analog.function.family.name": "Kotlin 아날로그로 바꾸기",
  "should.be.replaced.with.kotlin.function": "Kotlin 함수로 대체해야 합니다.",
  "quickfix.text.suffix.may.change.semantics": "\\ (의미가 변경될 수 있음)",
  "replace.with.kotlin.analog.function.text": "''{0}'' 함수로 바꾸기"
}

with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

filename = "KotlinBundle.properties"
found = False
for file_entry in data.get('new_files', []):
    if file_entry['filename'] == filename:
        file_entry['keys'].update(ko_dict)
        found = True
        break
if not found:
    data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

print(f"Updated {filename} (Keys 1091-1140)")

with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
