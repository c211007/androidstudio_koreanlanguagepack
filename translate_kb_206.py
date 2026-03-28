import json

def update_translations():
    with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if "ShBundle.properties" not in data:
        data["ShBundle.properties"] = {}
        
    translations = {
        "quotes.backslashes.will.be.treated.literally.use.an.array": "따옴표와 백슬래시는 문자 그대로 처리됩니다. 배열을 사용하세요.",
        "tilde.does.not.expand.in.quotes.use.home": "물결표는 따옴표 안에서 확장되지 않습니다. $HOME을 사용하세요.",
        "quote.eof.to.make.here.document.expansions.happen.on.the.server.side.rather.than.on.the.client": "클라이언트가 아닌 서버 측에서 here 문서 확장이 수행되도록 'EOF' 주위에 따옴표를 추가하세요.",
        "double.quote.to.prevent.globbing.and.word.splitting": "글로빙 및 단어 분할을 방지하려면 큰따옴표를 사용하세요.",
        "remove.or.use.expr.to.avoid.executing.output": "출력 실행을 방지하려면 '$'를 제거하거나 '_=$((expr))'을 사용하세요.",
        "to.expand.via.indirection.use.name.foo.n.echo.name": "간접 참조를 통해 확장하려면 name=\"foo$n\"; echo \"${!name}\"을 사용하세요.",
        "can.t.match.globs.use.or.grep": "`[ .. ]`는 글롭과 일치할 수 없습니다. `[[ .. ]]` 또는 grep을 사용하세요.",
        "numbers.with.leading.0.are.considered.octal": "0으로 시작하는 숫자는 8진수로 간주됩니다.",
        "doesn.t.support.decimals.use.bc.or.awk": "'(( ))'는 소수를 지원하지 않습니다. 'bc' 또는 'awk'를 사용하세요.",
        "this.expression.is.constant.did.you.forget.a.somewhere": "이 표현식은 상수입니다. 어딘가에 `$`를 잊으셨나요?",
        "you.need.spaces.around.the.comparison.operator": "비교 연산자 주위에 공백이 필요합니다.",
        "don.t.quote.rhs.of.it.ll.match.literally.rather.than.as.a.regex": "=~의 우변을 인용하지 마세요. 정규식 대신 문자 그대로 일치하게 됩니다.",
        "can.t.use.in.use.instead": "`[ ]` 안에서 `=~`를 사용할 수 없습니다. 대신 `[[..]]`를 사용하세요.", 
        "decimals.are.not.supported.either.use.integers.only.or.use.bc.or.awk.to.compare": "소수는 지원되지 않습니다. 정수만 사용하거나 비교를 위해 'bc' 또는 'awk'를 사용하세요.",
        "is.for.string.comparisons.use.gt.instead": "'>'는 문자열 비교용입니다. 대신 '-gt'를 사용하세요.",
        "n.doesn.t.work.with.unquoted.arguments.quote.or.use": "`-n`은 인용되지 않은 인수와 함께 작동하지 않습니다. 인용하거나 `[[ ]]`를 사용하세요.",
        "to.redirect.stdout.stderr.2.1.must.be.last.or.use.cmd.file.2.1.to.clarify": "stdout+stderr를 리디렉션하려면 '2>&1'이 마지막에 와야 합니다(또는 명확성을 위해 '{ cmd > file; } 2>&1'을 사용하세요).",
        "double.quote.array.expansions.to.avoid.re.splitting.elements": "요소가 다시 분할되지 않도록 배열 확장을 큰따옴표로 묶습니다.",
        "missing.or.terminating.exec.you.can.t.use.and.has.to.be.a.separate.quoted.argument": "'-exec'를 종료하는 ';' 또는 '+'가 누락되었습니다. |/||/&&를 사용하지 마시고 ';'에는 따옴표를 사용하세요.",
        "since.you.double.quoted.this.it.will.not.word.split.and.the.loop.will.only.run.once": "이것은 큰따옴표로 묶여 있기 때문에 단어로 분할되지 않으며 루프는 한 번만 실행됩니다.",
        "this.is.interpreted.as.a.shell.file.redirection.not.a.comparison": "이것은 비교가 아닌 셸 파일 리디렉션으로 해석됩니다.",
        "use.single.quotes.otherwise.this.expands.now.rather.than.when.signalled": "신호를 받을 때만 확장하려면 즉시가 아닌 작은따옴표를 사용하세요.",
        "grep.uses.regex.but.this.looks.like.a.glob": "Grep은 정규식을 사용하지만 이것은 글롭처럼 보입니다.",
        "quote.the.grep.pattern.so.the.shell.won.t.interpret.it": "셸이 해석하지 않도록 grep 패턴을 인용하세요.",
        "quote.the.parameter.to.name.so.the.shell.won.t.interpret.it": "셸이 해석하지 않도록 '-name'에 대한 매개변수를 인용하세요.",
        "quote.parameters.to.tr.to.prevent.glob.expansion": "글롭 확장을 방지하려면 'tr'에 매개변수를 인용하세요.",
        "don.t.use.variables.in.the.printf.format.string.use.printf.s.foo": "printf 형식 문자열에 변수를 사용하지 마세요. 대신 다음과 같은 구문을 사용하세요: printf \"..%s..\" \"$foo\".",
        "unknown.unaryoperator": "알 수 없는 단항 연산자입니다.",
        "unknown.binary.operator": "알 수 없는 이항 연산자입니다.",
        "you.probably.wanted.here": "'&&'를 사용하세요.",
        "use.spaces.not.commas.to.separate.array.elements": "배열 요소를 구분하려면 쉼표가 아닌 공백을 사용하세요.",
        "quote.the.rhs.of.in.to.prevent.glob.matching": "글롭 일치를 방지하려면 '[[ ]]' 안에 있는 '=의 우변'을 인용하세요.",
        "bash.doesn.t.support.variables.in.brace.range.expansions": "Bash는 중괄호 범위 확장에서 변수를 지원하지 않습니다.",
        "this.expression.is.constant.did.you.forget.the.on.a.variable": "이 표현식은 상수입니다. 변수의 `$`를 잊으셨나요?",
        "is.for.regex.but.this.looks.like.a.glob.use.instead": "'=~'는 정규식용이지만 이것은 글롭처럼 보입니다. 대신 '='를 사용하세요.",
        "use.with.quotes.to.prevent.whitespace.problems": "공백 문제를 방지하려면 \"$@\"(따옴표 포함)을 사용하세요.",
        "quote.this.to.prevent.word.splitting": "단어 분할을 방지하려면 이것을 인용하세요.",
        "iterating.over.ls.output.is.fragile.use.globs": "ls 출력을 반복하는 것은 취약합니다. 글롭을 사용하세요.",
        "for.loops.over.find.output.are.fragile.use.find.exec.or.a.while.read.loop": "find 출력에 대한 for 루프는 취약합니다. 'find -exec' 또는 while read 루프를 사용하세요.",
        "this.loop.will.only.ever.run.once.for.a.constant.value.did.you.perhaps.mean.to.loop.over.dir.var.or.cmd": "이 루프는 상수 값에 대해 한 번만 실행됩니다. 혹시 'dir/*', '$var' 또는 '$(cmd)'에 대해 반복하려고 하셨나요?",
        "this.is.a.literal.string.to.run.as.a.command.use.instead.of": "이것은 리터럴 문자열입니다. 명령으로 실행하려면 '..' 대신 '$(..)'를 사용하세요.",
        "bin.sh.was.specified.so.is.not.supported.even.when.sh.is.actually.bash": "'#!/bin/sh'가 지정되었으므로 sh가 실제로는 bash이더라도 ____은(는) 지원되지 않습니다.",
        "in.posix.sh.something.is.undefined": "POSIX sh에서는 무엇인가가 정의되지 않습니다.", 
        "use.print0.0.or.find.exec.to.allow.for.non.alphanumeric.filenames": "알파벳 및 숫자가 아닌 파일 이름을 허용하려면 '-print0', '-0' 또는 'find -exec +'를 사용하세요.",       
        "to.assign.the.output.of.a.command.use.var.cmd": "명령의 출력을 할당하려면 'var=$(cmd)'를 사용하세요.",
        "if.you.wanted.to.assign.the.output.of.the.pipeline.use.a.b.c": "파이프라인의 출력을 할당하려면 'a=$(b | c)'를 사용하세요.",
        "use.glob.or.glob.so.names.with.dashes.won.t.become.options": "대시가 포함된 이름이 옵션이 되지 않도록 './*glob*' 또는 '-- *glob*'을 사용하세요.",
        "foo.appears.unused.verify.it.or.export.it": "'foo'가 사용되지 않는 것 같습니다. 확인하거나 내보내세요.",
        "shell.functions.can.t.be.passed.to.external.commands": "셸 함수는 외부 명령에 전달될 수 없습니다.",
        "use.own.script.or.sh.c.to.run.this.from.su": "su에서 이것을 실행하려면 자체 스크립트 또는 sh -c '..'를 사용하세요."
    }
    
    data["ShBundle.properties"].update(translations)
    
    with open('missing_translations/missing_keys_korean.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    update_translations()
