import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "check.1130.you.need.a.space.before.the": "':' 앞에 공백을 추가하세요.",
        "check.1131.use.elif.to.start.another.branch": "다른 분기를 시작하려면 `elif`를 사용하세요.",
        "this.terminates.the.command.escape.it.or.add.space.after.to.silence": "이 `\\\\&`는 명령어를 종료합니다. 이스케이프하거나 `\\\\&` 뒤에 공백을 추가하여 무시하도록 하세요.",
        "unexpected.start.of.line.if.breaking.lines.should.be.at.the.end.of.the.previous.one": "예기치 않은 새 줄의 시작입니다. 줄을 나눌 경우 |/||/\\\\&\\\\&는 이전 줄의 끝에 있어야 합니다.",
        "arrays.implicitly.concatenate.in.use.a.loop.or.explicit.instead.of": "배열은 `[[ ]]`에서 암시적으로 연결됩니다. 루프를 사용하세요(또는 '@' 대신 명시적 '*' 사용).",
        "arrays.don.t.work.as.operands.in.use.a.loop.or.concatenate.with.instead.of": "배열은 '[ ]'에서 피연산자로 작동하지 않습니다. 루프를 사용하세요(또는 '@' 대신 '*'와 연결).",
        "fgrep.is.non.standard.and.deprecated.use.grep.f.instead": "fgrep은 비표준이며 더 이상 사용되지 않습니다. 대신 grep -F를 사용하세요.",
        "egrep.is.non.standard.and.deprecated.use.grep.e.instead": "egrep은 비표준이며 더 이상 사용되지 않습니다. 대신 grep -E를 사용하세요.",
        "this.pattern.will.never.match.the.case.statement.s.word.double.check.them": "이 패턴은 case 문의 단어와 절대 일치하지 않습니다.",
        "this.word.is.constant.did.you.forget.the.on.a.variable": "이 단어는 상수입니다. 변수에 '$' 문자를 잊으셨습니까?",
        "the.arguments.to.this.comparison.can.never.be.equal.make.sure.your.syntax.is.correct": "이 비교에 대한 인수는 절대 같을 수 없습니다. 구문이 올바른지 확인하세요.",
        "this.array.element.has.no.value.remove.spaces.after.or.use.for.empty.string": "이 배열 요소에는 값이 없습니다. '=' 뒤의 공백을 제거하거나 빈 문자열에 \"\"를 사용하세요.",
        "the.here.is.literal.to.assign.by.index.use.index.value.with.no.spaces.to.keep.as.literal.quote.it": "여기서 등호 '='는 리터럴입니다. 인덱스로 할당하려면 공백 없이 ( [index]=value )를 사용하세요. 리터럴로 유지하려면 따옴표를 사용하세요.",
        "elements.in.associative.arrays.need.index.e.g.array.index.value": "연관 배열의 요소에는 인덱스가 필요합니다(예: array=( [index]=value )).",
        "you.can.t.have.between.this.redirection.and.the.command.it.should.apply.to": "이 리디렉션과 적용되는 명령 사이에 '|'를 가질 수 없습니다.",
        "this.redirection.doesn.t.have.a.command.move.to.its.command.or.use.true.as.no.op": "이 리디렉션에는 명령어가 없습니다. 해당 명령어로 이동하세요(또는 no-op으로 'true' 사용).",
        "ash.scripts.will.be.checked.as.dash.add.shellcheck.shell.dash.to.silence": "Ash 스크립트는 Dash로 검사됩니다. 경고를 숨기려면 '# shellcheck shell=dash'를 추가하세요.",
        "tempfile.is.deprecated.use.mktemp.instead": "tempfile은 사용되지 않습니다. 대신 mktemp를 사용하세요.",
        "some.finds.don.t.have.a.default.path.specify.explicitly": "일부 find에는 기본 경로가 없습니다. 명시적으로 '.'를 지정하세요.",
        "quote.arguments.to.unset.so.they.re.not.glob.expanded": "글로브 구문을 무시하려면 인수를 따옴표로 묶으세요.",
        "this.format.string.has.2.variables.but.is.passed.1.arguments": "이 형식 문자열에는 변수가 2개 있지만 인수 1개가 전달됩니다.",
        "this.printf.format.string.has.no.variables.other.arguments.are.ignored": "이 printf 형식 문자열에는 변수가 없습니다. 다른 인수는 무시됩니다.",
        "check.exit.code.directly.with.e.g.if.mycmd.not.indirectly.with": "'$'?로 간접적으로 확인하지 말고 'if mycmd;'로 직접 종료 코드를 확인하세요.",
        "bash.does.not.support.multidimensional.arrays.use.1d.or.associative.arrays": "Bash는 다차원 배열을 지원하지 않습니다. 1차원 배열이나 연관 배열만 사용하세요.",
        "use.array.item.to.append.items.to.an.array": "배열에 항목을 추가하려면 'array+=(\"item\")'을 사용하세요.",
        "variable.was.used.as.an.array.but.is.now.assigned.a.string": "변수가 배열로 사용되었지만 지금은 문자열이 할당되었습니다.",
        "time.is.undefined.for.compound.commands.time.sh.c.instead": "복합 명령어에 대해 'time'이 정의되어 있지 않습니다. 대신 'time sh -c'를 사용하세요.",
        "time.is.undefined.for.pipelines.time.single.stage.or.bash.c.instead": "파이프라인에 대해 'time'이 정의되어 있지 않습니다. 대신 단일 단계 또는 `time bash -c`에서 `time`을 사용하세요.",
        "quote.this.invalid.brace.expansion.since.it.should.be.passed.literally.to.eval": "이 잘못된 중괄호 확장은 eval에 리터럴로 전달되어야 하므로 따옴표로 묶으세요.",
        "when.used.with.p.m.only.applies.to.the.deepest.directory": "'-p'와 함께 사용할 경우 '-m'은 가장 깊은 디렉토리에만 적용됩니다.",
        "sigkill.sigstop.can.not.be.trapped": "SIGKILL 및 SIGSTOP은 트랩할 수 없습니다.",
        "trapping.signals.by.number.is.not.well.defined.prefer.signal.names": "숫자로 신호를 트랩하는 것은 잘 정의되어 있지 않습니다. 신호 이름을 사용하는 것이 좋습니다.",
        "numerical.eq.does.not.dereference.in.expand.or.use.string.operator": "숫자 '-'eq는 [..]에서 역참조하지 않습니다. 확장하거나 문자열 연산자를 사용하세요.",
        "in.dash.something.is.not.supported": "이 기능은 dash에서 지원되지 않습니다.",
        "local.is.only.valid.in.functions": "'local'은 함수에서만 유효합니다.",
        "this.parent.loop.has.its.index.variable.overridden": "이 상위 루프의 인덱스 변수가 재정의되었습니다.",
        "prefer.p.q.as.p.a.q.is.not.well.defined": "'[ p -a q ]'는 잘 정의되어 있지 않으므로 '[ p ] \\\\&\\\\& [ q ]'를 사용하는 것이 좋습니다.",
        "this.nested.loop.overrides.the.index.variable.of.its.parent": "이 중첩된 루프는 상위 루프의 인덱스 변수를 재정의합니다.",
        "use.cd.exit.in.case.cd.fails": "cd가 실패할 경우에 대비해 cd ... || exit를 사용하세요.",
        "this.does.not.export.foo.remove.for.that.or.use.var.to.quiet": "이것은 'FOO'를 내보내지 않습니다. 이를 위해 '$' 및 '${}'를 제거하거나 모르게 하려면 '${var?}'를 사용하세요.",
        "read.without.r.will.mangle.backslashes": "'-r'이 없는 'read'는 백슬래시를 망가뜨립니다.",
        "instead.of.1.use.true": "'[ 1 ]' 대신 'true'를 사용하세요.",
        "instead.of.true.just.use.true": "'[ true ]' 대신 'true'를 사용하세요.",
        "0.is.true.use.false.instead": "'[ 0 ]'은 true입니다. 대신 'false'를 사용하세요.",
        "false.is.true.remove.the.brackets": "'[ false ]'는 true입니다. 괄호를 제거하세요.",
        "argument.to.implicit.n.is.always.true.due.to.literal.strings": "암시적 '-n'에 대한 인수는 리터럴 문자열로 인해 항상 true입니다.",
        "injecting.filenames.is.fragile.and.insecure.use.parameters": "파일 이름 주입은 취약하고 불안전합니다. 매개변수를 사용하세요.",
        "declare.and.assign.separately.to.avoid.masking.return.values": "반환 값을 가리는 것을 방지하려면 개별적으로 선언하고 할당하세요.",
        "var.is.referenced.but.not.assigned": "'var'가 참조되었지만 할당되지 않았습니다.",
        "possible.misspelling.myvariable.may.not.be.assigned.but.my.variable.is": "철자 오류 가능성: MYVARIABLE은 할당되지 않았지만 MY_VARIABLE은 할당되었을 수 있습니다."
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
