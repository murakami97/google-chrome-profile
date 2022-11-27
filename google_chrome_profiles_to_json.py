import sys
import json
import re

# applescript で Google Chrome の メニューバー -> プロファイル 内の
# UI element を取得し、文字列として受け取ることを想定

# alfred から argv を受け取ったときは argv[2] に入る

# example
# profiles = "menu item EXAMPLE of menu プロファイル of menu bar item プロファイル of menu bar 1 of application process Google Chrome, ..."

profiles = str(sys.argv[1])
# クエリが存在する場合は q_list として受け取る
# クエリがないときは q_list は空のリストになる
q_list = sys.argv[2:]

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
    is_matched = True
    # クエリが存在する場合は、名前がすべてのクエリ文字列を含む profile だけ抽出する。大文字小文字は区別しない。
    for q in q_list:
        if q.lower() not in name.lower():
            is_matched = False
            break
    if not is_matched:
        continue
    item = {}
    item["title"] = name
    item["subtitle"] = f"Open Google Chrome with [ {name} ] profile"
    item["arg"] = name
    item_list.append(item)

items["items"] = item_list

print(json.dumps(items))

# print(names)
