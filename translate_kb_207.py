import json

def update_translations():
    with open('missing_translations/missing_keys_korean.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    translations = {
        "var.was.modified.in.a.subshell.that.change.might.be.lost": "'var'가 하위 셸에서 수정되었습니다. 해당 변경 사항이 손실될 수 있습니다.",
        "modification.of.var.is.local.to.subshell.caused.by.pipeline": "'var' 수정은 로컬입니다(파이프라인으로 인해 발생한 하위 셸에 대해).",
        "note.that.unescaped.this.expands.on.the.client.side": "이스케이프되지 않은 경우 이것은 클라이언트 측에서 확장됩니다.",
        "echo.won.t.expand.escape.sequences.consider.printf": "'echo'는 이스케이프 시퀀스를 확장하지 않습니다. 'printf'를 고려하세요.",
        "the.surrounding.quotes.actually.unquote.this.remove.or.escape.them": "주변 따옴표가 실제로 이것의 따옴표를 제거합니다. 제거하거나 이스케이프하세요.",
        "this.word.is.outside.of.quotes.did.you.intend.to.nest.single.quotes.instead": "이 단어는 따옴표 밖에 있습니다. 대신 작은따옴표를 중첩하려고 하셨나요?",
        "make.sure.all.escape.sequences.are.enclosed.in.to.prevent.line.wrapping.issues": "줄 바꿈 문제를 방지하려면 모든 이스케이프 시퀀스가 `\\[..\\]` 안에 포함되어 있는지 확인하세요.",
        "sudo.doesn.t.affect.redirects.use.sudo.tee.file": "`sudo`는 리디렉션에 영향을 주지 않습니다. `..| sudo tee file`을 사용하세요.",
        "note.that.unlike.globs.o.here.matches.ooo.but.not.oscar": "글롭과 달리 여기서 'o*'는 'ooo'와 일치하지만 'oscar'와는 일치하지 않습니다.",
        "don.t.use.around.ranges.in.tr.it.replaces.literal.square.brackets": "'tr'의 범위 주위에 '[]'를 사용하지 마세요. 리터럴 대괄호가 대체됩니다.",
        "tr.replaces.sets.of.chars.not.words.mentioned.due.to.duplicates": "'tr'은 단어가 아닌 문자 집합을 대체합니다(중복되어서 언급됨).",
        "use.upper.to.support.accents.and.foreign.alphabets": "악센트 및 외국어 알파벳을 지원하려면 '[:upper:]'를 사용하세요.",
        "use.lower.to.support.accents.and.foreign.alphabets": "악센트 및 외국어 알파벳을 지원하려면 '[:lower:]'를 사용하세요.",
        "increase.precision.by.replacing.a.b.c.with.a.c.b": "'a/b\\*c'를 'a\\*c/b'로 대체하여 정밀도를 높이세요.",
        "expressions.don.t.expand.in.single.quotes.use.double.quotes.for.that": "표현식은 작은따옴표 안에서 확장되지 않습니다. 큰따옴표를 사용하세요.",
        "note.that.a.b.c.is.not.if.then.else.c.may.run.when.a.is.true": "'A \\&\\& B || C'는 'if-then-else'가 아닙니다. A가 참일 때 C가 실행될 수 있습니다.",
        "this.will.expand.once.before.find.runs.not.per.file.found": "이것은 찾은 파일당이 아니라 find가 실행되기 전에 한 번 확장됩니다.",
        "to.read.lines.rather.than.words.pipe.redirect.to.a.while.read.loop": "단어가 아닌 줄을 읽으려면 파이프를 사용하거나 출력을 'while read' 루프로 리디렉션하세요.", 
        "use.find.instead.of.ls.to.better.handle.non.alphanumeric.filenames": "알파벳이나 숫자가 아닌 파일 이름을 더 잘 처리하려면 `ls` 대신 `find`를 사용하세요.",
        "don.t.use.ls.grep.use.a.glob.or.a.for.loop.with.a.condition.to.allow.non.alphanumeric.filenames": "'ls | grep'을 사용하지 마세요. 알파벳이나 숫자가 아닌 파일 이름을 허용하려면 글롭이나 조건이 있는 for 루프를 사용하세요.",
        "sc2009.consider.using.pgrep.instead.of.grepping.ps.output": "SC2009: ps 출력을 grep하는 대신 pgrep 사용을 고려하세요.",
        "echo.doesn.t.read.from.stdin.are.you.sure.you.should.be.piping.to.it": "'echo'는 stdin에서 읽지 않습니다. 이 명령으로 파이핑하는 것은 권장되지 않습니다.",
        "use.instead.of.deprecated": "더 이상 사용되지 않는 '$[..]' 대신 '$((..))'를 사용하세요.",
        "use.notation.instead.of.legacy.backticked": "기존의 백틱(`` `...` ``) 대신 '$(...)' 표기법을 사용하세요.",
        "useless.echo.instead.of.echo.cmd.just.use.cmd": "불필요한 `echo`가 있나요? `echo $(cmd)` 대신 `cmd`를 사용하세요.",
        "is.unnecessary.on.arithmetic.variables": "산술 변수에는 '$' 및 '${}'가 불필요합니다.",
        "expr.is.antiquated.consider.rewriting.this.using.or": "'expr'는 오래되었습니다. '$((..))', '${}' 또는 '\\[\\[ \\]\\]'를 사용하여 다시 작성하는 것을 고려하세요.",    
        "useless.cat.consider.cmd.file.or.cmd.file.instead": "불필요한 'cat'입니다. 대신 'cmd < file | ..' 또는 'cmd file | ..'을 고려하세요.",
        "sc2001.see.if.you.can.use.variable.search.replace.instead": "SC2001: 대신 ${variable//search/replace}를 사용할 수 있는지 확인하세요.",
        "consider.adding.a.default.case.even.if.it.just.exits.with.error": "단순히 오류와 함께 종료되더라도 기본 '*)' 케이스를 추가하는 것을 고려하세요.",
        "flip.leading.and.if.this.should.be.a.quoted.substitution": "명령 치환을 인용하려면 선행 '$'와 '\"'를 뒤집으세요.",
        "this.shebang.specifies.a.directory.ensure.the.interpreter.is.a.file": "이 shebang은 디렉토리를 지정합니다. 인터프리터가 파일인지 확인하세요.",
        "d.only.applies.to.the.first.expansion.of.this.glob.use.a.loop.to.check.any.all": "'-d'는 이 글롭의 첫 번째 확장에만 적용됩니다. 루프를 사용하여 전체 또는 일부를 확인하세요.",
        "prefer.explicit.n.to.check.non.empty.string.or.use.ne.to.check.boolean.integer": "비어 있지 않은 문자열을 확인하려면 명시적 '-n'을 사용하는 것이 좋습니다. 부울 및 정수를 확인하려면 '=' 또는 '-ne'를 사용하세요.",
        "prefer.explicit.n.to.check.for.output.or.run.command.without.to.check.for.success": "출력을 확인하려면 명시적 '-n'을 사용하는 것이 좋습니다. 성공 여부를 확인하려면 '[' 및 '[[' 없이 명령을 실행하세요.",
        "can.only.exit.with.status.0.255.other.data.should.be.written.to.stdout.stderr": "상태 0-255로만 종료할 수 있습니다. 다른 데이터는 stdout/stderr에 작성되어야 합니다.",
        "the.exit.status.can.only.be.one.integer.0.255.use.stdout.for.other.data": "종료 상태는 0에서 255 사이의 정수 하나만 될 수 있습니다. 다른 데이터에는 stdout을 사용하세요.",       
        "the.dot.command.does.not.support.arguments.in.sh.dash.set.them.as.variables": "점(.) 명령은 sh/dash에서 인수를 지원하지 않습니다. 변수로 설정하세요.",
        "ensure.the.shebang.uses.the.absolute.path.to.the.interpreter": "shebang에서 인터프리터의 절대 경로를 사용하는지 확인하세요.",
        "redirecting.to.from.command.name.instead.of.file.did.you.want.pipes.xargs.or.quote.to.ignore": "파일 대신 명령 이름으로/에서 리디렉션 중입니다. 파이프나 xargs를 대신 사용하세요(무시하려면 인용하세요).",
        "use.n.instead.of.z": "`! [ -z .. ]` 대신 `[ -n .. ]`을 사용하세요.",
        "use.n.instead.of.z2": "`! -z` 대신 `-n`을 사용하세요.",
        "use.instead.of.to.avoid.subshell.overhead": "하위 셸 오버헤드를 방지하려면 `(..)` 대신 `{ ..; }`를 사용하세요.",
        "remove.superfluous.around.test.command": "test 명령 주위의 불필요한 `(..)`를 제거하세요.",
        "remove.superfluous.around.condition": "조건 주위의 불필요한 `(..)`를 제거하세요.",
        "can.t.use.sudo.with.builtins.like.cd.did.you.want.sudo.sh.c.instead": "'cd'와 같은 내장 명령과 함께 'sudo'를 사용할 수 없습니다. 대신 'sudo sh -c'를 사용하시겠습니까?",
        "quote.expansions.in.this.for.loop.glob.to.prevent.wordsplitting.e.g.dir.txt": "예를 들어 \"$dir\"/*.txt와 같이 단어 분할을 방지하려면 이 for 루프 글롭의 확장을 인용하세요.",
        "which.is.non.standard.use.builtin.command.v.instead": "'which'는 비표준입니다. 대신 기본 제공되는 'command -v'를 사용하세요.",
        "this.does.not.read.foo.remove.for.that.or.use.var.to.quiet": "이것은 'foo'를 읽지 않습니다. 이를 위해 '$' 및 '${}'를 제거하거나 조용히 하려면 '${var?}'를 사용하세요.",
        "redirection.applies.to.the.find.command.itself.rewrite.to.work.per.action.or.move.to.end": "리디렉션이 'find' 명령 자체에 적용됩니다. 작업별로 작동하도록 다시 작성하세요(또는 끝으로 이동하세요)."
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
