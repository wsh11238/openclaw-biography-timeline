#!/usr/bin/env python3
"""研究缓存 — 未知人物研究完成后自动缓存，下次直接读取。
缓存格式: research_cache/<人名>.json
TTL: 30天（可配置）
用法:
    from research_cache import ResearchCache
    cache = ResearchCache()
    cached = cache.get("张忠谋")  # 返回 dict 或 None
    cache.set("张忠谋", data)      # 存入缓存
"""
import json
import os
import time
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent / "research_cache"
TTL_SECONDS = 30 * 24 * 3600  # 30天

class ResearchCache:
    def __init__(self, cache_dir: Path = None, ttl: int = TTL_SECONDS):
        self.cache_dir = cache_dir or CACHE_DIR
        self.ttl = ttl
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_path(self, name: str) -> Path:
        safe_name = name.replace("/", "_").replace("\\", "_")
        return self.cache_dir / f"{safe_name}.json"

    def get(self, name: str) -> dict | None:
        """读取缓存，如果过期或不存在返回 None"""
        path = self._cache_path(name)
        if not path.exists():
            return None
        try:
            meta_path = path.with_suffix(".meta.json")
            if meta_path.exists():
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                cached_at = meta.get("cached_at", 0)
                if time.time() - cached_at > self.ttl:
                    return None  # 过期
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, KeyError):
            return None

    def set(self, name: str, data: dict) -> None:
        """存入缓存"""
        path = self._cache_path(name)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        meta_path = path.with_suffix(".meta.json")
        meta_path.write_text(json.dumps({
            "cached_at": time.time(),
            "cached_at_display": time.strftime("%Y-%m-%d %H:%M:%S"),
            "person": name,
            "events_count": len(data.get("events", [])),
            "sources_count": len(data.get("sources", [])),
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    def list_cached(self) -> list[dict]:
        """列出所有缓存条目"""
        result = []
        for meta_file in self.cache_dir.glob("*.meta.json"):
            try:
                result.append(json.loads(meta_file.read_text(encoding="utf-8")))
            except json.JSONDecodeError:
                continue
        return sorted(result, key=lambda x: x.get("cached_at", 0), reverse=True)

    def clear_expired(self) -> int:
        """清除过期缓存，返回清除数量"""
        count = 0
        for meta_file in self.cache_dir.glob("*.meta.json"):
            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
                if time.time() - meta.get("cached_at", 0) > self.ttl:
                    name = meta.get("person", "")
                    if name:
                        cache_path = self._cache_path(name)
                        cache_path.unlink(missing_ok=True)
                        meta_file.unlink(missing_ok=True)
                        count += 1
            except (json.JSONDecodeError, OSError):
                continue
        return count

    def clear_all(self) -> int:
        """清除所有缓存"""
        count = 0
        for f in self.cache_dir.glob("*"):
            if f.is_file():
                f.unlink()
                count += 1
        return count


if __name__ == "__main__":
    import sys
    cache = ResearchCache()
    if len(sys.argv) < 2:
        print("Usage: python research_cache.py <list|clear|get <name>|clear-expired>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "list":
        items = cache.list_cached()
        if not items:
            print("Cache is empty")
        for item in items:
            print(f"  {item.get('person','?')}: cached at {item.get('cached_at_display','?')}, {item.get('events_count',0)} events")
    elif cmd == "clear":
        n = cache.clear_all()
        print(f"Cleared {n} cache files")
    elif cmd == "clear-expired":
        n = cache.clear_expired()
        print(f"Cleared {n} expired cache files")
    elif cmd == "get":
        if len(sys.argv) < 3:
            print("Usage: python research_cache.py get <name>")
            sys.exit(1)
        data = cache.get(sys.argv[2])
        if data:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(f"Cache miss for: {sys.argv[2]}")
    else:
        print(f"Unknown command: {cmd}")
