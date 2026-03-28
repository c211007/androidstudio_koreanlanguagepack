import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sh.invalid.path": "잘못된 경로입니다.",
        "find.usages.type.function": "함수",
        "sh.run.configuration.description.0.configuration": "{0} 구성",
        "error.message.cannot.determine.shell.script.parent.directory": "셸 스크립트 상위 디렉토리를 확인할 수 없습니다.",
        "check1000.is.not.used.specially.and.should.therefore.be.escaped": "$는 이스케이프해야 합니다.",
        "check1001.this.o.will.be.a.regular.o.in.this.context": "이 \\\\o는 이 컨텍스트에서 일반 'o'가 됩니다.",
        "check1003.want.to.escape.a.single.quote.echo.this.is.how.it.s.done": "작은따옴표를 이스케이프하려면 echo 'This is how it'\\\\''s done'과 같이 사용하세요.",
        "check1004.this.backslash.linefeed.is.literal.break.outside.single.quotes.if.you.just.want.to.break.the.line": "이 백슬래시+줄바꿈은 리터럴입니다. 줄을 나누려면 작은따옴표 밖에서 나누세요.",
        "check1007.remove.space.after.if.trying.to.assign.a.value.or.for.empty.string.use.var": "값을 할당하려면 '=' 뒤의 공백을 제거하세요(빈 문자열인 경우 var='' ... 사용).",
        "check.1008.this.shebang.was.unrecognized.shellcheck.only.supports.sh.bash.dash.ksh.add.a.shell.directive.to.specify": "이 shebang이 인식되지 않았습니다. ShellCheck는 sh/bash/dash/ksh만 지원합니다. 지정하려면 'shell' 지시문을 추가하세요.",
        "check.1009.the.mentioned.parser.error.was.in": "언급된 파서 오류의 위치는 다음과 같습니다...",
        "check.1010.use.semicolon.or.linefeed.before.done.or.quote.to.make.it.literal": "'done' 앞에 세미콜론이나 줄바꿈을 사용하세요(리터럴로 만들려면 따옴표 사용).",
        "check.1011.this.apostrophe.terminated.the.single.quoted.string": "이 아포스트로피는 작은따옴표로 묶인 문자열을 종료했습니다!",
        "check.1012.is.just.literal.t.here.for.tab.use.printf.instead": "`\t`는 여기서 리터럴 `t`입니다. 탭을 추가하려면 대신 \"$(printf '\t')\"를 사용하세요.",
        "check.1014.use.if.cmd.then.to.check.exit.code.or.if.cmd.to.check.output": "종료 코드를 확인하려면 'if cmd; then ...'을 사용하고 출력을 확인하려면 'if [ \"$(cmd)\" = .. ]'를 사용하세요.",
        "check.1015.this.is.a.unicode.double.quote.delete.and.retype.it": "유니코드 큰따옴표입니다. 삭제하고 다시 입력하세요.",
        "check.1016.this.is.a.unicode.single.quote.delete.and.retype.it": "유니코드 작은따옴표입니다. 삭제하고 다시 입력하세요.",
        "check.1017.literal.carriage.return.run.script.through.tr.d": "리터럴 캐리지 리턴입니다. `tr -d '\\n'`을 통해 스크립트를 실행하세요.",
        "check.1018.this.is.a.unicode.non.breaking.space.delete.it.and.retype.as.space": "유니코드 줄바꿈 없는 공백입니다. 삭제하고 스페이스 키로 다시 입력하세요.",
        "check.1019.expected.this.to.be.an.argument.to.the.unary.condition": "이것은 단항 조건의 인수여야 합니다.",
        "check.1020.you.need.a.space.before.the.if.single.then.else": "`]` 또는 `]]` 앞에 공백을 추가하세요.",
        "check.1026.if.grouping.expressions.inside.use": "[[..]] 안에서 표현식을 그룹화하려면 ( .. )를 사용하세요.",
        "check.1028.in.you.have.to.escape.or.preferably.combine.expressions": "[..] 에서는 \\\\( \\\\)를 이스케이프하거나 [..] 표현식을 결합하는 것이 좋습니다.",
        "check.1029.in.you.shouldn.t.escape.or": "`[[..]]` 에서는 `(` 또는 `)`를 이스케이프하면 안 됩니다.",
        "check.1035.you.need.a.space.here": "여기에 공백을 추가하세요.",
        "check.1036.is.invalid.here.did.you.forget.to.escape.it": "여기에서 `(`는 잘못되었습니다. 이스케이프하는 것을 잊으셨습니까?",
        "check.1037.braces.are.required.for.positionals.over.9.e.g.10": "9보다 큰 위치 매개변수 (예: 10)에는 중괄호가 필요합니다.",
        "check.1038.shells.are.space.sensitive.use.cmd.not.cmd": "셸은 공백에 민감합니다. '<<(cmd)'가 아닌 '< <(cmd)'를 사용하세요.",
        "check.1039.remove.indentation.before.end.token.or.use.and.indent.with.tabs": "끝 토큰 앞의 들여쓰기를 제거하세요. (또는 `<<-`를 사용하고 탭으로 들여쓰세요.)",
        "check.1040.when.using.you.can.only.indent.with.tabs": "<<-를 사용할 때는 탭으로 들여쓰세요.",
        "check.1041.found.eof.further.down.but.not.on.a.separate.line": "아래에서 'eof'를 찾았지만 별도의 줄에 있지 않습니다.",
        "check.1042.found.eof.further.down.but.not.on.a.separate.line": "아래에서 'eof'를 찾았지만 별도의 줄에 있지 않습니다.",
        "check.1044.couldn.t.find.end.token.eof.in.the.here.document": "here 문서에서 끝 토큰 `EOF`를 찾을 수 없습니다.",
        "check.1045.it.s.not.foo.bar.just.foo.bar": "'foo \\\\&; bar'에 불필요한 세미콜론이 있습니다. 'foo \\\\& bar'가 되어야 합니다.",
        "check.1046.couldn.t.find.fi.for.this.if": "이 'if'에 대한 'fi'를 찾을 수 없습니다.",
        "check.1047.expected.fi.matching.previously.mentioned.if": "앞서 언급된 'if'와 일치하는 'fi'가 필요합니다.",
        "check.1048.can.t.have.empty.then.clauses.use.true.as.a.no.op": "빈 then 절은 사용할 수 없습니다. (no-op으로 'true' 사용).",
        "check.1049.did.you.forget.the.then.for.this.if": "이 'if'에 대한 'then'을 지정하는 것을 잊으셨습니까?",
        "check.1045.expected.then": "'then'이 필요합니다.",
        "check.1051.semicolons.directly.after.then.are.not.allowed.just.remove.it": "'then' 바로 뒤의 세미콜론은 허용되지 않습니다.",
        "check.1052.semicolons.directly.after.then.are.not.allowed.just.remove.it": "'then' 바로 뒤의 세미콜론은 허용되지 않습니다.",
        "check.1053.semicolons.directly.after.else.are.not.allowed.just.remove.it": "'else' 바로 뒤의 세미콜론은 허용되지 않습니다.",
        "check.1054.you.need.a.space.after.the": "'{' 뒤에 공백을 추가하세요.",
        "check.1058.expected.do": "`do`가 필요합니다.",
        "check.1061.couldn.t.find.done.for.this.do": "이 'do'에 대한 'done'을 찾을 수 없습니다.",
        "check.1062.expected.done.matching.previously.mentioned.do": "앞서 언급된 'do'에 일치하는 'done'이 필요합니다.",
        "check.1064.expected.a.to.open.the.function.definition": "함수 정의를 여는 '{'가 필요합니다.",
        "check.1065.trying.to.declare.parameters.don.t.use.and.refer.to.params.as.1.2": "매개변수를 선언하지 마세요. ()를 사용하고 $1, $2 등의 매개변수를 참조하세요.",
        "check.1066.don.t.use.on.the.left.side.of.assignments": "할당의 왼쪽에 '$'를 사용하지 마세요.",
        "check.1068.don.t.put.spaces.around.the.in.assignments": "할당에서 '=' 주위에 공백을 두지 마세요."
    }

    filename = "ShBundle.properties"
    found = False
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(ko_dict)
            found = True
            break
    if not found:
        data.setdefault('new_files', []).append({"filename": filename, "keys": ko_dict})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {filename}")

if __name__ == "__main__":
    update_missing_keys()
