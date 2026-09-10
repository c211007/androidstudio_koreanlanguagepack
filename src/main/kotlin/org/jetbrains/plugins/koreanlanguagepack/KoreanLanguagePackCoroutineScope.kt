package org.jetbrains.plugins.koreanlanguagepack

import com.intellij.openapi.components.Service
import kotlinx.coroutines.CoroutineScope

/**
 * 앱 생명주기에 묶인 코루틴 스코프. 재시도처럼 오래 걸릴 수 있는 작업을
 * ApplicationInitializedListener.execute()에서 분리해 백그라운드에서 돌리는 데 쓴다
 * (execute()를 오래 붙잡고 있으면 IDE 시작 시퀀스 자체가 느려진다).
 */
@Service(Service.Level.APP)
internal class KoreanLanguagePackCoroutineScope(val coroutineScope: CoroutineScope)
