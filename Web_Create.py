import os
import random

# Webサイトの数
num_websites = 20

# 保存先のディレクトリ
output_dir = "Web"

# キーワードリスト
keywords = ["いちご", "ガンダム", "刺身"]

# 各キーワードの最大出現回数
max_occurrences = 10

# 保存先ディレクトリの作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Webサイトを生成して保存
for i in range(1, num_websites + 1):
    site_name = f"site_{i}"
    site_content = f"<html><head><title>{site_name}</title></head><body>"
    
    # 各キーワードの出現回数をランダムに設定
    keyword_occurrences = {keyword: random.randint(0, max_occurrences) for keyword in keywords}
    
    site_content += "<ul>"
    for keyword, occurrences in keyword_occurrences.items():
        # 各キーワードの出現回数分だけ追加
        for _ in range(occurrences):
            site_content += f"<li>{keyword}</li>"
    site_content += "</ul></body></html>"
    
    with open(os.path.join(output_dir, f"{site_name}.html"), "w") as f:
        f.write(site_content)
