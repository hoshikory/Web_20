import os

def find_best_match(search_keyword, website_dir):
    best_match = None
    max_count = 0
    
    for filename in os.listdir(website_dir):
        if filename.endswith(".html"):
            with open(os.path.join(website_dir, filename), "r") as f:
                content = f.read()
                match_count = content.count(search_keyword)
                if match_count > max_count:
                    max_count = match_count
                    best_match = filename[:-5]  # .html 拡張子を削除してサイト名のみを取得
    
    return best_match

# 検索キーワードを入力
search_keyword = input("検索キーワードを入力してください: ")

# Webサイトが保存されているディレクトリ
website_dir = "Web"

# 最も一致するサイト名を検索
best_match_site = find_best_match(search_keyword, website_dir)

# 結果の表示
if best_match_site:
    print(f"最も一致するサイトは {best_match_site} です。")
else:
    print("一致するサイトが見つかりませんでした。")
