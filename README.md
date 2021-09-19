# GroupB
グループ開発B
### 9/17(金)以降触ってない人用
```
1. $git pull --all ※自分のブランチ上で
2. featureブランチに移動
3. $git pull origin feature 
4. 自分のブランチに移動
5. $git merge origin feature
その後settings.pyやurls.pyに必要なやつはコメントアウトしてあるので、自分の所で必要なやつのみコメントアウトを外して使用してください
```
### 9/17(金)以降触った人
* そのまま開発を進めてください
### Djangoコマンド
```
$python manage.py runserver 0.0.0.0:8000
ブラウザに行き http://127.0.0.1:8000/<urls> で見ることができると思います
```
# Dockerを使った開発開始コマンド
```
1. $git pull --all (後日変わる可能性有)
2. $docker-compose up --build -d #コンテナ内に入ります
3. $docker-compose exec app bash
4. $pipenv install --system ※コンテナ内であることを確認
```
# Dockerを使った開発終了コマンド
```
1. $exit ※コンテナ内であることを確認
2. $git add .
3. $git commit -m "<コメント>"
4. $git push origin <ブランチ名>
5. $docker-compose down
```
# 学校用PCで使う開発開始コマンド
```
1. $git pull --all
2. $pipenv shell #仮想環境に入る
```
# 学校用PCで使う開発終了コマンド
```
1. $exit ※仮想環境であることを確認
2. $git add .
3. $git commit -m "<コメント>"
4. $git push origin <ブランチ名>
```
# その他コマンド
```
$docker ps -a
$docker images
$docker container prune -a
$docker image prune
$pipenv install <パッケージ名>
$git update-index --skip-worktree Pipfile Pipfile.lock config/settings.py
$git update-index --no-skip-worktree  Pipfile Pipfile.lock config/settings.py
```