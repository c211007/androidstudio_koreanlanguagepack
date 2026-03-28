import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "can.only.return.0.255.other.data.should.be.written.to.stdout": "0-255만 반환할 수 있습니다. 다른 데이터는 stdout에 써야 합니다.",
        "only.one.integer.0.255.can.be.returned.use.stdout.for.other.data": "0-255 사이의 단일 정수만 반환할 수 있습니다. 다른 데이터에는 stdout을 사용하세요.",
        "exec.does.not.automatically.invoke.a.shell.use.exec.sh.c.for.that": "'-exec'는 자동으로 셸을 호출하지 않습니다. 대신 '-exec sh -c'를 사용하세요.",
        "remove.for.numeric.index.or.escape.it.for.string": "숫자 인덱스의 경우 '$' 및 '${}'를 제거하고, 문자열의 경우 이스케이프하세요.",
        "tips.depend.on.target.shell.and.yours.is.unknown.add.a.shebang": "도움말은 대상 셸에 따라 다릅니다. shebang을 추가하세요.",
        "literal.tilde.in.path.works.poorly.across.programs": "PATH의 리터럴 물결표는 여러 프로그램에서 제대로 작동하지 않습니다.",
        "this.action.ignores.everything.before.the.o.use.to.group": "이 작업은 '-o' 앞의 모든 것을 무시합니다. 그룹화하려면 \\\\( \\\\)를 사용하세요.",
        "argument.mixes.string.and.array.use.or.separate.argument": "인수에 문자열과 배열이 혼합되어 있습니다. '*'를 사용하거나 인수를 분리하세요.",
        "e.doesn.t.work.with.globs.use.a.for.loop": "'-e'는 glob에서 작동하지 않습니다. for 루프를 사용하세요.",
        "use.grep.q.instead.of.comparing.output.with.n": "출력을 '[ -n .. ]'와 비교하는 대신 'grep -q'를 사용하세요.",
        "aliases.can.t.use.positional.parameters.use.a.function": "별칭은 위치 매개변수를 사용할 수 없습니다. 함수를 사용하세요.",
        "did.you.mean.ifs": "IFS=$'\t'를 의도하셨습니까?",
        "word.is.on.the.form.a.b.c.b.indicated.did.you.mean.abc.or.a.b.c": "\\ 단어가 \"A\"B\"C\" 형태입니다(B가 표시됨). \"ABC\" 또는 \"A\\\\\"B\\\\\"C\"를 의도하셨습니까?",
        "this.expands.when.defined.not.when.used.consider.escaping": "이것은 사용될 때가 아니라 정의될 때 확장됩니다. 이스케이핑을 고려하세요.",
        "eq.is.for.integer.comparisons.use.instead": "'-eq'는 정수 비교용입니다. 대신 '='를 사용하세요.",
        "consider.using.cmd1.cmd2.file.instead.of.individual.redirects": "개별적인 리디렉션 대신 '{ cmd1; cmd2; } >> file'을 사용해 보세요.",
        "expanding.an.array.without.an.index.only.gives.the.first.element": "인덱스 없이 배열을 확장하면 첫 번째 요소만 반환됩니다.",
        "consider.using.grep.c.instead.of.grep.wc": "'grep|wc' 대신 'grep -c'를 사용해 보세요.",
        "brace.expansions.and.globs.are.literal.in.assignments.quote.it.or.use.an.array": "할당에서 중괄호 확장 및 glob은 리터럴입니다. 따옴표나 배열을 사용하세요.",
        "assigning.an.array.to.a.string.assign.as.array.or.use.instead.of.to.concatenate": "배열을 문자열에 할당하려고 합니다! 배열로 할당하거나 연결하려면 '@' 대신 '*'를 사용하세요.",
        "path.is.the.shell.search.path.use.another.name": "PATH는 셸 검색 경로입니다. 다른 이름을 사용하세요.",
        "is.not.a.valid.operator.use.a.b.instead": "'>='는 유효한 연산자가 아닙니다. 대신 '! a < b'를 사용하세요.",
        "to.assign.a.variable.use.just.var.value.no.set": "변수를 할당하려면 'set ..'이 아니라 'var=value' 형태만 사용하세요.",
        "foo.references.arguments.but.none.are.ever.passed": "'foo'가 인수를 참조하지만 아무것도 전달되지 않습니다.",
        "use.foo.if.function.s.1.should.mean.script.s.1": "함수의 '$1' 인수가 스크립트의 '$1' 인수를 의미하는 경우 'foo \"$@\"'를 사용하세요.",
        "to.run.commands.as.another.user.use.su.c.or.sudo": "다른 사용자로 명령을 실행하려면 'su -c' 또는 'sudo'를 사용하세요.",
        "useless.echo.instead.of.cmd.echo.foo.just.use.cmd.foo": "불필요한 echo입니다. 'cmd $(echo foo)' 대신 'cmd foo'를 사용하세요.",
        "use.var.to.ensure.this.never.expands.to": "이것이 결코 /* 로 확장되지 않도록 하려면 \"${var:?}\"를 사용하세요.",
        "warning.deletes.a.system.directory": "경고: 시스템 디렉토리를 삭제합니다.",
        "function.keyword.is.non.standard.delete.it": "'function' 키워드는 비표준입니다. 삭제하세요.",
        "in.use.instead.of.o": "'[\\\\[..]]'에서는 '-o' 대신 '||'를 사용하세요.",
        "instead.of.a.b.use.a.b": "'[ a || b ]' 대신 '[ a ] || [ b ]'를 사용하세요.",
        "in.use.instead.of.a": "'[\\\\[..]]'에서는 '-a' 대신 '\\\\&\\\\&'를 사용하세요.",
        "instead.of.a.b.use.a.b2": "'[ a \\\\&\\\\& b ]' 대신 '[ a ] \\\\&\\\\& [ b ]'를 사용하세요.",
        "sc2106.this.only.exits.the.subshell.caused.by.the.pipeline": "SC2106: 파이프라인으로 인한 서브셸만 종료합니다.",
        "break.is.only.valid.in.loops": "`break`는 루프에서만 유효합니다.",
        "in.functions.use.return.instead.of.break": "함수에서는 'break' 대신 'return'을 사용하세요.",
        "use.a.subshell.to.avoid.having.to.cd.back": "되돌아가는 cd 명령(cd back)을 피하려면 (서브셸)을 사용하세요.",
        "ranges.can.only.match.single.chars.mentioned.due.to.duplicates": "범위는 단일 문자에만 일치할 수 있습니다(중복으로 인해 표기됨).",
        "named.class.needs.outer.e.g.digit": "명명된 클래스에는 바깥쪽 '[]'가 필요합니다(예: [[:digit:]\\\\]).",
        "use.for.arithmetics.e.g.i.i.2": "산술에는 `$((..))`를 사용하세요(예: i=$((i + 2))).",
        "this.expansion.will.not.see.the.mentioned.assignment": "이 확장은 앞서 언급된 할당을 볼 수 없습니다.",
        "this.assignment.is.only.seen.by.the.forked.process": "이 할당은 포크된 프로세스에서만 볼 수 있습니다.",
        "on.most.os.shebangs.can.only.specify.a.single.parameter": "대부분의 OS에서 shebangs는 단일 매개변수만 지정할 수 있습니다.",
        "add.dev.null.to.prevent.ssh.from.swallowing.stdin": "ssh가 표준 입력을 집어삼키는 것(swallowing stdin)을 방지하려면 '< /dev/null'을 추가하세요.",
        "sc2094.make.sure.not.to.read.and.write.the.same.file.in.the.same.pipeline": "SC2094: 동일한 파이프라인에서 동일한 파일을 읽고 쓰지 마세요.",
        "remove.exec.if.script.should.continue.after.this.command": "이 명령어 이후에도 스크립트가 계속 실행되어야 하는 경우 \"exec \"를 제거하세요.",
        "remove.backticks.to.avoid.executing.output": "출력을 실행하지 않으려면 백틱(`)을 제거하세요.",
        "remove.surrounding.to.avoid.executing.output": "출력을 실행하지 않으려면 주변 '$()'를 제거하세요.",
        "quotes.backslashes.in.this.variable.will.not.be.respected": "이 변수의 분리형 따옴표 및 백슬래시는 무시됩니다."
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
