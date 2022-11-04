import sys
import json
import re

# applescript で Google Chrome の メニューバー -> プロファイル 内の
# UI element を取得し、文字列として受け取ることを想定

# alfred から argv を受け取ったときは argv[2] に入る

# example
# profiles = "menu item EXAMPLE of menu プロファイル of menu bar item プロファイル of menu bar 1 of application process Google Chrome, ..."

if len(sys.argv) == 2:
    profiles = str(sys.argv[1])
    q = ""
elif len(sys.argv) == 3:
    profiles = sys.argv[1]
    q = sys.argv[2]

profiles = profiles.split(", ")

# 最後の4項目には profile としての意味がないので削除しておく
profiles = profiles[:-4]


def profile_to_name(profile):
    # ユーザーに表示するために profile の名前部分を取り出す関数
    name = profile
    name = name.removeprefix("menu item ")
    name = name.removesuffix(
        " of menu プロファイル of menu bar item プロファイル of menu bar 1 of application process Google Chrome")
    return name


items = {}
item_list = []
for profile in profiles:
    name = profile_to_name(profile)
    if q and q not in name:
        continue
    item = {}
    item["title"] = name
    item["subtitle"] = f"Open Google Chrome with [ {name} ] profile"
    item["arg"] = name
    item_list.append(item)

items["items"] = item_list

print(json.dumps(items))

# print(names)
