import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    ko_dict = {
        "mdn.documentation.section.compat.support_of": "<code>{0}</code> 지원:",
        "mdn.documentation.section.compat.supported_by.none": "없음",
        "mdn.documentation.section.parameters": "매개변수",
        "mdn.documentation.section.returns": "반환",
        "mdn.documentation.section.throws": "예외",
        "mdn.documentation.section.syntax": "구문",
        "mdn.documentation.section.values": "값",
        "mdn.documentation.baseline.not-supported": "주요 브라우저에서 지원되지 않음",
        "mdn.documentation.baseline.limited-availability": "주요 브라우저에서 제한적으로 사용 가능",
        "mdn.documentation.baseline.newly-available": "주요 브라우저에서 새로 사용 가능",
        "mdn.documentation.baseline.widely-available": "주요 브라우저에서 널리 사용 가능",
        "mdn.documentation.baseline.since": "{0} 이후 기준선",
        "mdn.documentation.baseline.not-supported-by": "{0}에서 지원되지 않음",
        "mdn.documentation.section.compat.browser_compatibility": "지원 브라우저:",
        "mdn.documentation.section.compat.flex_context": "Flex 레이아웃",
        "mdn.documentation.section.compat.grid_context": "Grid 레이아웃",
        "mdn.documentation.section.compat.block_context": "Block 레이아웃",
        "mdn.documentation.section.compat.multicol_context": "다중 열 레이아웃",
        "mdn.documentation.section.compat.paged_context": "페이지 미디어",
        "mdn.documentation.section.compat.position_absolute_context": "절대 위치 컨텍스트",
        "mdn.documentation.section.compat.supported_in_grid_layout": "Grid 레이아웃",
        "mdn.documentation.section.compat.2d_context": "2D 컨텍스트",
        "mdn.documentation.section.compat.3d_context": "3D 컨텍스트",
        "mdn.documentation.section.compat.bitmaprenderer_context": "<code>bitmaprenderer</code> 컨텍스트",
        "mdn.documentation.section.compat.webgl2_context": "WebGL 2 컨텍스트",
        "mdn.documentation.section.compat.webgl_context": "WebGL 컨텍스트",
        "mdn.documentation.section.compat.webgpu_context": "Web GPU 컨텍스트",
        "mdn.documentation.section.compat.supported_for_width_and_other_sizing_properties": "크기 조정 속성",
        "mdn.documentation.section.compat.support_of_multi-keyword_values": "다중 값",
        "mdn.documentation.section.compat.support_of_WOFF": "<code>WOFF</code>",
        "mdn.documentation.section.compat.support_of_WOFF_2": "<code>WOFF 2</code>",
        "mdn.documentation.section.compat.support_of_dialog_elements": "대화 상자 요소에서 <code>beforetoggle</code> 이벤트 발생",
        "mdn.documentation.section.compat.support_of_details_elements": "세부 정보 요소에서 <code>toggle</code> 이벤트 발생",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar": "<code>::-webkit-scrollbar</code>",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar-button": "<code>::-webkit-scrollbar-button</code>",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar-thumb": "<code>::-webkit-scrollbar-thumb</code>",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar-track": "<code>::-webkit-scrollbar-track</code>",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar-track-piece": "<code>::-webkit-scrollbar-track-piece</code>",
        "mdn.documentation.section.compat.support_of_-webkit-scrollbar-corner": "<code>::-webkit-scrollbar-corner</code>",
        "mdn.documentation.section.compat.support_of_-webkit-resizer": "<code>::-webkit-resizer</code>",
        "mdn.documentation.section.compat.support_of_fit-content": "<code>fit-content()</code>",
        "mdn.documentation.section.compat.support_of_fit-content_function": "<code>fit-content()</code>",
        "mdn.documentation.section.compat.support_of_hsl": "<code>hsl()</code>(HSL 색상 모델)",
        "mdn.documentation.section.compat.support_of_hwb": "<code>hwb()</code>(HWB 색상 모델)",
        "mdn.documentation.section.compat.support_of_lch": "<code>lch()</code>(LCH 색상 모델)",
        "mdn.documentation.section.compat.support_of_oklch": "<code>oklch()</code>(OKLCH 색상 모델)",
        "mdn.documentation.section.compat.support_of_scope": "<code>@scope</code>",
        "mdn.documentation.section.compat.support_of_at-scope": "<code>@scope</code> 블록에서 <code>&amp;</code>가 <code>:where(:scope)</code>로 처리됨",
        "mdn.documentation.section.compat.support_of_loadend_event": "<code>loadend</code> 이벤트",
        "mdn.documentation.section.compat.support_of_loadstart_event": "<code>loadstart</code> 이벤트"
    }
    
    filename = "MdnBundle.properties"
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
