#!/usr/bin/env python3
"""Xinnova GitHub Traffic Reporter"""
import json, urllib.request
from datetime import datetime, timezone

TOKEN_FILE = "C:\\Users\\YAW\\.workbuddy\\xinnova_gh_token.txt"
OWNER = "Photonwealth"
REPO = "Xinnova"

def get_token():
    try:
        with open(TOKEN_FILE) as f: return f.read().strip()
    except: return None

def gh_api(endpoint):
    token = get_token()
    if not token: return None
    req = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{REPO}/{endpoint}",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "Xinnova-Traffic-Bot"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp: return json.loads(resp.read())
    except Exception as e:
        print(f"API error: {e}")
        return None

def fmt(n):
    return f"{n:,}"

def main():
    views = gh_api("traffic/views")
    clones = gh_api("traffic/clones")
    popular = gh_api("traffic/popular/paths")

    print("=" * 44)
    print("  Xinnova - GitHub Traffic Report")
    print(f"  {OWNER}/{REPO}")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 44)

    if views:
        print(f"\n  Page Views:  {fmt(views['count']):>8}  |  Unique: {views['uniques']}")
    else:
        print("\n  Page Views:  --  (check token)")

    if clones:
        print(f"  Clones:      {fmt(clones['count']):>8}  |  Unique: {clones['uniques']}")
    else:
        print("  Clones:      --  (check token)")

    if popular:
        print(f"\n  Top Content:")
        for i, p in enumerate(popular[:6], 1):
            title = p.get('title', p['path'])
            print(f"  {i}. {title}")
            print(f"     Views: {p['count']} | Unique: {p['uniques']}")

    print(f"\n  https://github.com/{OWNER}/{REPO}")
    print("=" * 44)

if __name__ == "__main__":
    main()
