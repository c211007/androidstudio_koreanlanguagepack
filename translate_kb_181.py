import json
from pathlib import Path

def update_missing_keys():
    file_path = Path("missing_translations/missing_keys_korean.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ko_dict = {
        "sml.studiobot.indexer.tool.bm25Search.running": "코드베이스 검색 중...",
        "sml.studiobot.indexer.tool.bm25Search.completed": "코드베이스 검색됨",
        "sml.studiobot.indexer.tool.bm25FindFiles.running": "“{0}”과(와) 일치하는 파일 검색 중...",
        "sml.studiobot.indexer.tool.bm25FindFiles.completed": "“{0}”과(와) 일치하는 파일 검색됨",
        "sml.studiobot.indexer.tool.bm25Grep.running": "“{0}”에 대한 Grep 실행 중...",
        "sml.studiobot.indexer.tool.bm25Grep.completed": "“{0}”에 대한 Grep 실행됨",
        "sml.studiobot.indexer.tool.embeddingSearch.running": "임베딩을 기반으로 코드베이스 검색 중...",
        "sml.studiobot.indexer.tool.embeddingSearch.completed": "임베딩 기반 코드베이스 검색됨",
        "sml.studiobot.indexer.tool.kbSearch.running": "문서 검색 중...",
        "sml.studiobot.indexer.tool.kbSearch.completed": "문서 검색됨",
        "sml.studiobot.indexer.tool.kbArticleLookup.running": "문서 문서 조회 중...",
        "sml.studiobot.indexer.tool.kbArticleLookup.completed": "문서 문서 조회됨"
    }

    filename = "RagIndexer.properties"
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
