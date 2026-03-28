import json
import os

translated_keys = {
  "vm.option.enable.assertions.description": "지정된 세분화 수준으로 어설션을 활성화합니다.",
  "vm.option.enable.system.assertions.description": "시스템 어설션을 활성화합니다.",
  "vm.option.disable.assertions.description": "지정된 세분화 수준으로 어설션을 활성화합니다.",
  "vm.option.disable.system.assertions.description": "시스템 어설션을 비활성화합니다.",
  "vm.option.agentpath.description": "\\\\&lt;pathname\\\\&gt;으로 네이티브 에이전트 라이브러리를 로드합니다.",
  "vm.option.agentlib.description": "\\\\&lt;libname\\\\&gt;으로 네이티브 에이전트 라이브러리를 로드합니다.",
  "vm.option.javaagent.description": "\\\\\\&lt;jarpath\\\\\\&gt;로 Java 프로그래밍 언어 에이전트를 로드합니다.",
  "vm.option.system.property.description": "\\\\&lt;name\\\\&gt;=\\\\&lt;value\\\\&gt; 형식으로 시스템 속성을 설정합니다.",
  "vm.option.advanced.option.description": "표준이 아닌 JVM 관련 옵션을 지정합니다.",
  "vm.option.batch.description": "백그라운드 컴파일을 비활성화합니다.",
  "vm.option.bootclasspath.a.description": "부트스트랩 클래스 경로의 끝에 추가합니다.",
  "vm.option.check.jni.description": "JNI 함수에 대한 추가 검사를 수행합니다.",
  "vm.option.comp.description": "첫 번째 호출 시 메서드 컴파일을 강제합니다.",
  "vm.option.debug.description": "아무 작업도 수행하지 않습니다. 이전 버전과의 호환성을 위해 제공됩니다.",
  "vm.option.diag.description": "추가 진단 메시지를 표시합니다.",
  "vm.option.future.description": "향후 기본값이 될 것을 예상하여 가장 엄격한 검사를 활성화합니다. 이 옵션은 사용 중단되었으며 향후 릴리스에서 제거될 수 있습니다.",
  "vm.option.int.description": "애플리케이션을 인터프리터 전용 모드로 실행합니다.",
  "vm.option.internalversion.description": "-version 옵션보다 더 자세한 JVM 버전 정보를 표시합니다.",
  "vm.option.log.description": "Java 가상 머신(JVM) 통합 로깅 프레임워크를 사용하여 로깅을 구성하거나 활성화합니다. 자세한 내용은 -Xlog:help를 사용하세요.",
  "vm.option.loggc.description": "타임스탬프와 함께 파일에 GC 상태를 기록합니다. 이 옵션은 사용 중단되었으며 향후 릴리스에서 제거될 수 있습니다. -Xlog:gc:\\\\&lt;file\\\\&gt;로 대체됩니다.",
  "vm.option.mixed.description": "혼합 모드 실행(기본값).",
  "vm.option.mn.description": "젊은 세대(nursery)를 위한 힙의 초기 및 최대 크기(바이트)를 설정합니다.",
  "vm.option.ms.description": "초기 Java 힙 크기를 설정합니다.",
  "vm.option.mx.description": "최대 Java 힙 크기를 설정합니다.",
  "vm.option.noclassgc.description": "클래스 가비지 컬렉션을 비활성화합니다.",
  "vm.option.rs.description": "Java/VM의 OS 신호 사용을 줄입니다(문서 참조).",
  "vm.option.share.auto.description": "가능한 경우 공유 클래스 데이터를 사용합니다(기본값).",
  "vm.option.share.off.description": "공유 클래스 데이터를 사용하려고 시도하지 않습니다.",
  "vm.option.share.on.description": "공유 클래스 데이터를 사용해야 하며 그렇지 않으면 실패합니다. 이것은 테스트 옵션이며 간헐적인 실패로 이어질 수 있습니다. 프로덕션 환경에서는 사용하지 마세요.",
  "vm.option.showSettings.description": "모든 설정을 표시하고 계속합니다.",
  "vm.option.showSettings.all.description": "모든 설정을 표시하고 계속합니다.",
  "vm.option.showSettings.locale.description": "모든 로케일 관련 설정을 표시하고 계속합니다.",
  "vm.option.showSettings.properties.description": "모든 속성 설정을 표시하고 계속합니다.",
  "vm.option.showSettings.vm.description": "모든 vm 관련 설정을 표시하고 계속합니다.",
  "vm.option.showSettings.system.description": "(Linux 전용) 호스트 시스템 또는 컨테이너 구성을 표시하고 계속합니다.",
  "vm.option.ss.description": "java 스레드 스택 크기를 설정합니다. 실제 크기는 운영 체제의 요구에 따라 시스템 페이지 크기의 배수로 올림될 수 있습니다.",
  "vm.option.verify.description": "바이트코드 검증기의 모드를 설정합니다. -Xverify:none 옵션은 사용 중단되었으며 향후 릴리스에서 제거될 수 있습니다.",
  "vm.option.bootclasspath.description": "부트스트랩 클래스 및 리소스에 대한 검색 경로를 설정합니다.",
  "vm.option.bootclasspath.p.description": "부트스트랩 클래스 경로의 앞에 추가합니다.",
  "vm.option.incgc.description": "증분 가비지 컬렉션을 활성화합니다.",
  "vm.option.prof.description": "CPU 프로파일링 데이터를 출력합니다.",
  "vm.option.add.reads.description": "모듈 선언에 관계없이 \\\\&lt;module\\\\&gt;이 \\\\&lt;target-module\\\\&gt;을 읽도록 업데이트합니다. \\\\&lt;target-module\\\\&gt;은 ALL-UNNAMED로 설정하여 모든 명명되지 않은 모듈을 읽을 수 있습니다.",
  "vm.option.add.opens.description": "모듈 선언에 관계없이 \\\\&lt;module\\\\&gt;이 \\\\&lt;target-module\\\\&gt;로 \\\\&lt;package\\\\&gt;를 열도록 업데이트합니다.",
  "vm.option.limit.modules.description": "관찰 가능한 모듈의 범위를 제한합니다.",
  "vm.option.patch.module.description": "JAR 파일 또는 디렉토리의 클래스와 리소스로 모듈을 재정의하거나 늘립니다.",
  "vm.option.finalization.description": "JVM이 객체의 최종화를 수행할지 여부를 제어합니다. 여기서 \\\\&lt;value\\\\&gt;는 \"enabled\" 또는 \"disabled\" 중 하나입니다. 최종화는 기본적으로 활성화되어 있습니다.",
  "vm.option.add.exports.description": "모듈 선언에 관계없이 \\\\&lt;module\\\\&gt;이 \\\\&lt;target-module\\\\&gt;로 \\\\&lt;package\\\\&gt;를 내보내도록 업데이트합니다. \\\\&lt;target-module\\\\&gt;은 ALL-UNNAMED로 설정하여 모든 명명되지 않은 모듈로 내보낼 수 있습니다.",
  "vm.option.source.description": "형식 파일 모드에서 소스의 \\\\&lt;version\\\\&gt;을 설정합니다.",
  "vm.option.disable.files.description": "추가 인수 파일 확장을 비활성화합니다.",
  "vm.option.illegal.access.description": "명명되지 않은 모듈의 코드가 명명된 모듈의 형식 멤버에 액세스하는 것을 허용하거나 거부합니다. \\\\&lt;value\\\\&gt;는 \"deny\", \"permit\", \"warn\" 또는 \"debug\" 중 하나입니다. 이 옵션은 향후 릴리스에서 제거됩니다."
}

file_path = "c:/Users/klanary/Desktop/vscode 모음/android_korean/androidstudio_koreanlanguagepack/missing_translations/missing_keys_korean.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_found = False
for item in data["new_files"]:
    if item["filename"] == "VMOptionsBundle.properties":
        item["keys"].update(translated_keys)
        file_found = True
        break

if not file_found:
    data["new_files"].append({
        "filename": "VMOptionsBundle.properties",
        "keys": translated_keys
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("VMOptionsBundle translated successfully.")