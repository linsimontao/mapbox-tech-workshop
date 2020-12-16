# Mapbox Tech Workshop 1 - Store Map                                                                                                           
## はじめに

Mapbox Studioを利用して、マップのデザインや、ウェブアプリケーションをビルドする方法を学びます


1. Mapbox Studioへのデータアップロード
2. Mabpox Stuidoでのカスタムデータのスタイル化
3. GLJSコードとの連携  

## 事前準備
1. テキストエディタ([SublimeText](https://www.sublimetext.com/), Atom等)
2. Mapboxアカウント https://account.mapbox.com

## Mapbox Studioへのアクセス
1. ブラウザからMapbox Studioにアクセス
    https://studio.mapbox.com
2. `Datasets` を選択する
3. 別のタブを開いて、以下のサイトにアクセスします  
    - 米国Starbucksの店舗(CSV):  https://gist.github.com/dankohn/09e5446feb4a8faea24f
4. `Download Zip`からZipファイルをダウンロード
5. ダウンロードしたファイルを展開して、テキストエディタでCSVファイルを開けるようにします
6. Studioを開いているブラウザタブにて、`New dataset`ボタンを押して、`Upload`タブを押して、`Select a file`からファイルを選択して、Datasetにアップロードします
![New datasetを押した後](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578640572600_image.png)


![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578640774647_image.png)

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578640897293_image.png)

7. CSVの場合は、ヘッダをチェックして、必要に応じて修正してください。終了後再度Uploadを試してみてください
    - https://docs.mapbox.com/help/troubleshooting/csv-upload-errors/
    - https://docs.mapbox.com/help/troubleshooting/uploads/
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578641245986_image.png)

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578641279822_image.png)

8. アップロードが成功したら、`Confirm`を押して、Dataset nameの画面に遷移したら、`Create`を押してください
    (環境にもよりますが 数秒かかります）
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578641444224_image.png)

9. 上記の画面が出たら、`Start editing`をクリックして、レビューを確認後、datasetを編集してみてください。なお、`View details`をクリックすると以下のような画面が表示され、ポップアップは消えてしまうので、Tilesetから`starbucks_us_locations`をクリックしてください。

![view deatils](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578641511216_image.png)

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643737791_image.png)

10. 任意のポイントをクリックして、プロパティとGeoJSONフォーマットを確認してください

| プロパティの表示 | GeoJSONの表示 |
|-|-|
|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578642131633_image.png)|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578642200039_image.png) |

11. ポリゴン(polygon)を描画し、以下の値を挿入

![](https://paper-attachments.dropbox.com/s_CBE5405AAD47D887439AD2718B584FF2A376280108350D5048B8F703EEF561B0_1566275525235_image.png)

12. `Save`をクリックしたのち、`export`をクリック  

  新しいTilesetとしてexportします。
  Tilesetについては[こちら](https://docs.mapbox.com/help/glossary/tileset/)

  | Saveをクリック | 変更内容が表示される | 次にExportをクリック |
  |-|-|-|
  |<img src="https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578642969885_image.png" />|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643166763_image.png)|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643340378_image.png)|
  | **new tilesetとしてexport** |　**処理中**　|　**完了**　|
  |![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643471190_image.png)|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643490577_image.png)|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578643605199_image.png)|


13. (Option) 同様に、以下のファイルについても実施してみてください。

- 日本のマクドナルドの店舗(JSON):  https://gist.github.com/tichimura/4f4dd6dce826f68526d3652d89e9de0c


## スタイルの作成

Studioのメイン画面に戻って、Light Templateを利用して新しいMapStyleを作成します。  
Streets, Light, Basicなどの任意のスタイルを選んでください。

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578644013666_image.png)

14. レイヤを追加して、先ほど作成したTilesetを選択して下さい

|レイヤの追加|データの確認|
|-|-|
|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578644126461_image.png)|![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578644240970_image.png)|

15. Styleを選択して、circleを緑(starbuck green #036635) に変更、strokeを編集して、白で縁取りをし、blurなどを設定してみてください

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578646353775_image.png)


16. 新しいレイヤを追加。Tilesetと同様に、polygonタイプを追加してみてください

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578646412727_image.png)


17. Sytleを選んで、色を編集、Opacityで透明度を変更してみてください

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578646739691_image.png)


18. レイヤの順序を変更して、polygonレイヤがcircleの下になるように設定

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578646816885_image.png)


19. 陸地をクリックして、landcoverレイヤをgreen tintに変更

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578647196285_image.png)
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578647291724_image.png)

20. `publish`を押してマップを出力

![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578647384139_image.png)

21. *Optional*: DatasetsタブでアップロードしたDatasetのGeoJSONフォーマットをエクスポートして、CSVとの違いを確認してみてください ( `Download`をクリック)
<center>
<img src=https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578647512039_image.png width=200></center>

22. *Optional*: 13で作成したtilesetについても、別のスタイルとして追加を実施してみて下さい。
　(McDonald Color: #ffcc00)

## コードへの追加

23. GLJS Example ページに移動

     https://docs.mapbox.com/mapbox-gl-js/examples/

1.  `Display buildings in 3D`をページ内で検索
1. クリップボードのアイコンをクリックして、コードをコピー
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578668479212_image.png)

1. テキストエディタで、新規ファイルを作成して、コピーしたコードをペースト
1. `index.html`として任意のフォルダに保存
1. 保存したフォルダ内のファイルを選んで、(ダブルクリックで)ブラウザにて表示
1. 地図が表示されたら成功です。最初の地図が表示されました。
1. 次に、このコードが何をしているかを確認しましょう
    1. SDKの場所
    2. Mapのインストール
    3. Layerの追加
1. スタイル(Style)がどこで呼ばれるか確認しましょう
1. 呼ばれているスタイルへのURLを、先ほど作成したスタイルへのURLで置き換えてみましょう
    作成したスタイルのリンクはStylesタブから、当該のスタイルを右クリックしたのち、クリップボードのアイコンをクリックすることでコピーできます
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578669560572_image.png)

1. 編集したindex.htmlを保存して、ブラウザをリロードしてみてください  
![](https://paper-attachments.dropbox.com/s_409822E5C193F50F3D9102DC2BEDC00A528737A25466437481175CBD03DE6048_1578669859969_image.png)

1. zoomと中心部の設定を変えてみてください
```
        mapboxgl.accessToken = '<YOUR TOKEN>';
        var map = new mapboxgl.Map({
            style: 'mapbox://styles/tichimura/ck57xw93e0qq41cntzk51wgy2',
            center: [-122.400, 37.791],
            zoom: 12,
            pitch: 45,
            bearing: -17.6,
            container: 'map',
            antialias: true
```

1. buildingレイヤで、opacityという属性を変更してください。値は0から1の間で変更してみてください
2. index.htmlを保存して、ブラウザをリロードしてください
3. *Optional:*: 22で追加したスタイルについても、確認してみて下さい。その前に、日本に合わせる必要があります。

# 🎉 終了です、お疲れさまでした。
# 参考情報

- [Data Uploads Errors](https://docs.mapbox.com/help/troubleshooting/csv-upload-errors/)
- [GLJS Examples](https://docs.mapbox.com/mapbox-gl-js/examples/)
- [GLJS API Reference](https://docs.mapbox.com/mapbox-gl-js/api/)
- [Mapbox Style Specification](https://docs.mapbox.com/mapbox-gl-js/style-spec/)
