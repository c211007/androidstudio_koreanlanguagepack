import json

def update_translations():
    with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    translations = {
        "this.ln.has.no.destination.check.the.arguments.or.specify.explicitly": "이 'ln'에는 대상이 없습니다. 인수를 확인하거나 '.'을 명시적으로 지정하세요.",      
        "this.cp.has.no.destination.check.the.arguments": "이 'cp'에는 대상이 없습니다. 인수를 확인하세요.",
        "this.mv.has.no.destination.check.the.arguments": "이 'mv'에는 대상이 없습니다. 인수를 확인하세요.",
        "this.default.assignment.may.cause.dos.due.to.globbing.quote.it": "이 기본 할당은 글로빙(globbing)으로 인해 DoS를 유발할 수 있습니다. 할당을 인용하세요.",
        "this.pattern.never.matches.because.of.a.previous.pattern": "이전 패턴으로 인해 이 패턴은 절대로 일치하지 않습니다.",
        "this.pattern.always.overrides.a.later.one": "이 패턴은 항상 이후 패턴보다 우선합니다.",
        "invalid.flags.are.not.handled.add.a.case": "잘못된 플래그는 처리되지 않습니다. `*)` 케이스를 추가하세요.",
        "instead.of.let.expr.prefer.expr": "`let expr` 대신 `(( expr ))`을 사용하는 것이 좋습니다.",
        "this.function.is.only.defined.later.move.the.definition.up": "이 함수는 나중에야 정의됩니다. 정의를 위로 이동하세요.",
        "redirecting.to.echo.a.command.that.doesn.t.read.stdin.bad.quoting.or.missing.xargs": "stdin을 읽지 않는 명령인 'echo'로 리디렉션하고 있습니다. 잘못 인용했거나 xargs가 누락된 건가요?",
        "piping.to.rm.a.command.that.doesn.t.read.stdin.wrong.command.or.missing.xargs": "stdin을 읽지 않는 명령인 'rm'으로 파이핑하고 있습니다. 잘못된 명령이거나 xargs가 누락된 건가요?",
        "this.flag.is.used.as.a.command.name.bad.line.break.or.missing": "이 플래그는 명령 이름으로 사용됩니다. 잘못된 줄 바꿈이거나 `[ .. ]`가 누락된 건가요?",
        "this.case.is.not.specified.by.getopts": "이 경우는 'getopts'에 의해 지정되지 않았습니다.",
        "getopts.specified.n.but.it.s.not.handled.by.this.case": "'getopts'는 '-n'을 지정했지만 이 'case'에서는 처리되지 않습니다.",
        "use.false.instead.of.empty.conditionals": "비어 있는 '[' 및 '[[' 조건문 대신 'false'를 사용하세요.",
        "this.is.a.glob.used.as.a.command.name.was.it.supposed.to.be.in.array.or.is.it.missing.quoting": "이것은 명령 이름으로 사용되는 글롭입니다. '${..}' 또는 배열 안에 있어야 합니까? 그렇지 않다면 따옴표를 사용하세요.",
        "this.is.a.file.redirection.was.it.supposed.to.be.a.comparison.or.fd.operation": "이것은 파일 리디렉션입니다. 비교였습니까 아니면 fd 작업이었습니까?",
        "use.var.command.to.assign.output.or.quote.to.assign.string": "출력을 할당하려면 'var=$(command)'를 사용하세요(또는 문자열을 할당하려면 따옴표를 사용하세요).",
        "use.or.quote.arguments.to.v.to.avoid.glob.expansion": "글롭 확장을 방지하려면 `[[ ]]`를 사용하거나 '-v' 옵션의 인수를 인용하세요.",
        "prefer.mapfile.or.read.a.to.split.command.output.or.quote.to.avoid.splitting": "명령 출력을 분할하려면 'mapfile' 또는 'read -a'를 사용하는 것이 좋습니다(또는 분할을 피하려면 인용).",
        "quote.to.prevent.word.splitting.or.split.robustly.with.mapfile.or.read.a": "단어 분할을 방지하기 위해 따옴표를 사용하거나 'mapfile' 또는 'read -a'를 사용하여 견고하게 분할하세요.",
        "is.a.subshell.did.you.mean.a.test.expression": "'(..)'는 하위 셸입니다. 테스트 표현식인 '[ .. ]'을(를) 의미하셨나요?",
        "globs.are.ignored.in.except.right.of.use.a.loop": "'=' 및 '!=' 의 오른쪽을 제외하고 `[[ ]]`에서 글롭은 무시됩니다. 루프를 사용하세요.",
        "globs.don.t.work.as.operands.in.use.a.loop": "글롭은 '[ ]'에서 피연산자로 작동하지 않습니다. 루프를 사용하세요.",
        "brace.expansion.doesn.t.happen.in.use.a.loop": "중괄호 확장은 `[[ ]]`에서 발생하지 않습니다. 루프를 사용하세요.",
        "brace.expansions.don.t.work.as.operands.in.use.a.loop": "중괄호 확장은 '[ ]'에서 피연산자로 작동하지 않습니다. 루프를 사용하세요.",
        "error.message.can.t.find.info.in.your.path": "$PATH 변수에서 관련 정보를 찾을 수 없습니다.",
        "line.marker.run.0": "{0} 실행",
        "i.do.mind.path.placeholder": "상관없습니다",
        "display.name.shell.check": "ShellCheck",
        "sh.markdown.runner.title": "터미널에서 실행"
    }
    
    filename = "ShBundle.properties"
    for file_entry in data.get('new_files', []):
        if file_entry['filename'] == filename:
            file_entry['keys'].update(translations)
            break
    
    with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_translations()
