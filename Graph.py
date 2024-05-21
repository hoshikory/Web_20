import os
import chardet
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def count_keyword_occurrences(search_keyword, website_dir):
    occurrences = {}
    
    # 指定されたディレクトリからHTMLファイルを読み込む
    for filename in os.listdir(website_dir):
        if filename.endswith(".html"):
            file_path = os.path.join(website_dir, filename)
            encoding = detect_encoding(file_path)
            with open(file_path, "r", encoding=encoding, errors='ignore') as f:
                content = f.read()
                
                # 検索キーワードの出現回数をカウント
                match_count = content.count(search_keyword)
                occurrences[filename[:-5]] = match_count  # .html 拡張子を除去してサイト名のみを取得
    
    return occurrences

# 検索キーワードを入力
search_keyword = input("検索キーワードを入力してください: ")

# Webサイトが保存されているディレクトリ
website_dir = "Web"

# ディレクトリの存在を確認
if not os.path.exists(website_dir):
    raise FileNotFoundError(f"指定されたパスが見つかりません: '{website_dir}'")

# キーワードの出現回数をカウント
keyword_occurrences = count_keyword_occurrences(search_keyword, website_dir)

# 結果の表示
if keyword_occurrences:
    # 日本語フォントの設定
    font_path = 'C:/Windows/Fonts/msgothic.ttc'  # 適切な日本語フォントのパスを指定してください
    font_prop = FontProperties(fname=font_path)

    # 棒グラフを作成
    sites = list(keyword_occurrences.keys())
    counts = list(keyword_occurrences.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sites, counts, color='skyblue')
    plt.xlabel('Webサイト', fontproperties=font_prop)
    plt.ylabel('出現回数', fontproperties=font_prop)
    plt.title(f'キーワード "{search_keyword}" の出現回数', fontproperties=font_prop)
    plt.xticks(rotation=90, fontproperties=font_prop)
    plt.show()
else:
    print("一致するサイトが見つかりませんでした。")
