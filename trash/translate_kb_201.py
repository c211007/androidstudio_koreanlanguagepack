import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "check.1069.you.need.a.space.before.the": "'[' 앞에 공백을 추가하세요.",
        "check.1071.shellcheck.only.supports.sh.bash.dash.ksh.scripts.sorry": "ShellCheck는 sh/bash/dash/ksh 스크립트만 지원합니다.",
        "check.1072.unexpected": "예상치 못한 ..",
        "check.1073.couldn.t.parse.this.thing.fix.to.allow.more.checks": "구문을 분석할 수 없습니다. 더 많은 검사를 허용하려면 수정하세요.",
        "check.1075.use.elif.instead.of.else.if": "'else if' 대신 'elif'를 사용하세요.",
        "check.1077.for.command.expansion.the.tick.should.slant.left.vs": "명령어 확장에는 백틱을 사용하세요: (` 및 \\u00B4).",
        "check.1078.did.you.forget.to.close.this.double.quoted.string": "이 큰따옴표 문자열을 닫는 것을 잊으셨습니까?",
        "check.1079.this.is.actually.an.end.quote.but.due.to.next.char.it.looks.suspect": "이것은 닫는 따옴표이지만 다음 문자로 인해 의심스러워 보입니다.",
        "check.1081.scripts.are.case.sensitive.use.if.not.if": "스크립트는 대소문자를 구분합니다. 'If'가 아닌 'if'를 사용하세요.",
        "check.1082.this.file.has.a.utf.8.bom.remove.it.with.lc.ctype.c.sed.1s.yourscript": "이 파일에는 UTF-8 BOM이 있습니다. 다음 명령으로 제거하세요: LC_CTYPE=C sed '1s/^...//' < yourscript",
        "check.1083.this.is.literal.check.expression.missing.or.quote.it": "이 `{`/`}`는 리터럴입니다. `;`가 누락되었는지 확인하거나 표현식을 따옴표로 묶으세요.",
        "check.1084.use.not.for.the.shebang": "shebang은 '!#'가 아니라 '#!'입니다.",
        "check.1086.don.t.use.on.the.iterator.name.in.for.loops": "for 루프의 반복자 이름에 '$'를 사용하지 마세요.",
        "check.1087.use.braces.when.expanding.arrays.e.g.array.idx.or.var.to.quiet": "배열을 확장할 때 중괄호를 사용하세요(예: ${array[idx]} 또는 경고를 숨기려면 ${var}[.. 사용).",
        "check.1088.parsing.stopped.here.invalid.use.of.parentheses": "여기서 파싱이 중지되었습니다. 괄호 사용이 잘못되었나요?",
        "check.1089.parsing.stopped.here.is.this.keyword.correctly.matched.up": "여기서 파싱이 중지되었습니다. 이 키워드가 올바르게 일치합니까?",
        "check.1090.can.t.follow.non.constant.source.use.a.directive.to.specify.location": "상수가 아닌 소스를 따를 수 없습니다. 위치를 지정하려면 지시문을 사용하세요.",
        "check.1091.not.following.error.message.here": "다음 항목을 따를 수 없습니다: (오류 메시지)",
        "check.1094.parsing.of.sourced.file.failed.ignoring.it": "소스 파일의 구문 분석에 실패했습니다. 무시합니다.",
        "check.1095.you.need.a.space.or.linefeed.between.the.function.name.and.body": "함수 이름과 본문 사이에 공백이나 줄바꿈이 필요합니다.",
        "check.1097.unexpected.for.assignment.use.for.comparison.use": "예기치 않은 '=='입니다. 할당에는 '='를 사용하세요. 비교하려면 대괄호 안에 '==' 표현식을 넣으세요.",
        "check.1098.quote.escape.special.characters.when.using.eval.e.g.eval.a.b": "eval을 사용할 때 특수 문자를 따옴표로 묶거나 이스케이프하세요(예: eval \"a=(b)\").",
        "check.1099.you.need.a.space.before.the": "'#' 앞에 공백을 추가하세요.",
        "check.1100.this.is.a.unicode.dash.delete.and.retype.as.ascii.minus": "이것은 유니코드 대시입니다. 삭제하고 ASCII 마이너스 문자로 다시 입력하세요.",
        "check.1101.delete.trailing.spaces.after.to.break.line.or.use.quotes.for.literal.space": "줄을 나누려면 \\\\ 뒤의 후행 공백을 삭제하세요(또는 리터럴 공백에는 따옴표 사용).",
        "check.1102.shells.disambiguate.differently.or.not.at.all.if.the.first.should.start.command.substitution.add.a.space.after.it": "셸은 $((를 다르게 처리하거나 전혀 구분하지 않습니다. 첫 번째 $(가 명령 대체를 시작해야 하는 경우 그 뒤에 공백을 추가하세요.",
        "check.1104.use.not.just.for.the.shebang": "shebang은 '!'가 아니라 '#!'입니다.",
        "check.1105.shells.disambiguate.differently.or.not.at.all.if.the.first.should.start.a.subshell.add.a.space.after.it": "셸은 ((를 다르게 처리하거나 전혀 구분하지 않습니다. 첫 번째 (가 서브셸을 시작해야 하는 경우 그 뒤에 공백을 추가하세요.",
        "check.1107.this.directive.is.unknown.it.will.be.ignored": "이 지시문은 알 수 없습니다. 무시됩니다.",
        "check.1108.you.need.a.space.before.and.after.the": "'='의 앞과 뒤에 공백을 추가하세요.",
        "check.1109.this.is.an.unquoted.html.entity.replace.with.corresponding.character": "이것은 따옴표로 묶이지 않은 HTML 엔티티입니다. 해당 문자로 바꿉니다.",
        "check.1110.this.is.a.unicode.quote.delete.and.retype.it.or.quote.to.make.literal": "유니코드 따옴표입니다. 삭제하고 다시 입력하세요(또는 리터럴로 만들려면 따옴표로 묶으세요).",
        "check.1111.this.is.a.unicode.quote.delete.and.retype.it.or.ignore.singlequote.for.literal": "유니코드 따옴표입니다. 삭제하고 다시 입력하세요(또는 리터럴로 만들려면 작은따옴표 사용).",
        "check.1112.this.is.a.unicode.quote.delete.and.retype.it.or.ignore.doublequote.for.literal": "유니코드 따옴표입니다. 삭제하고 다시 입력하세요(또는 리터럴로 만들려면 큰따옴표 사용).",
        "check.1113.use.not.just.for.the.sheban": "shebang은 '#'가 아니라 '#!'입니다.",
        "check.1114.remove.leading.spaces.before.the.shebang": "shebang 앞의 선행 공백을 제거하세요.",
        "check.1115.remove.spaces.between.and.in.the.shebang": "shebang의 '#'과 '!' 사이의 공백을 제거하세요.",
        "check.1116.missing.on.a.expression.or.use.for.arrays": "'$((..))' 표현식에서 '$'가 누락되었나요? 배열인 경우 '( ('를 사용하세요.",
        "check.1117.backslash.is.literal.in.prefer.explicit.escaping.n": "\"\\n\"에서 백슬래시는 리터럴입니다. 명시적 이스케이핑(\"\\\\n\")을 사용하는 것이 좋습니다.",
        "check.1118.delete.whitespace.after.the.here.doc.end.token": "here 문서 끝 토큰 뒤의 공백을 삭제하세요.",
        "check.1119.add.a.linefeed.between.end.token.and.terminating": "끝 토큰과 종료하는 ')' 사이에 줄바꿈을 추가하세요.",
        "check.1120.no.comments.allowed.after.here.doc.token.comment.the.next.line.instead": "here 문서 토큰 뒤에는 주석을 사용할 수 없습니다. 대신 다음 줄에 주석을 작성하세요.",
        "check.1121.add.terminators.and.other.syntax.on.the.line.with.the.not.here": "여기가 아니라 '<<'가 있는 줄에 ;/\\\\& 종결자(및 기타 구문)를 추가하세요.",
        "check.1122.nothing.allowed.after.end.token.to.continue.a.command.put.it.on.the.line.with.the": "끝 토큰 뒤에는 아무것도 허용되지 않습니다. 명령어를 계속하려면 '<<'가 있는 줄에 넣으세요.",
        "check.1123.shellcheck.directives.are.only.valid.in.front.of.complete.compound.commands.like.if.not.e.g.individual.elif.branches": "ShellCheck 지시문은 개별 `elif` 분기와 같이 앞이 아닌 `if`와 같은 완전한 복합 명령어 앞에만 유효합니다.",
        "check.1124.shellcheck.directives.are.only.valid.in.front.of.complete.commands.like.case.statements.not.individual.case.branches": "ShellCheck 지시문은 개별 case 분기가 아니라 'case' 문과 같은 완전한 명령어 앞에만 유효합니다.",
        "check.1126.place.shellcheck.directives.before.commands.not.after": "ShellCheck 지시문은 명령어 뒤가 아니라 명령어 앞에 배치하세요.",
        "check.1127.was.this.intended.as.a.comment.use.in.sh": "주석으로 의도된 것이라면 `#`을 사용하세요.",
        "check.1128.the.shebang.must.be.on.the.first.line.delete.blanks.and.move.comments": "shebang은 첫 번째 줄에 있어야 합니다. 빈 줄을 삭제하고 주석을 이동하세요.",
        "check.1129.you.need.a.space.before.the": "'!' 앞에 공백을 추가하세요."
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
