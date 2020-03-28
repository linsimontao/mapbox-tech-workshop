# Mapbox Tech Workshop 5 - Travel Itinerary

## はじめに

このモジュールでは、引き続き、実際に想定される課題をもとに、GLJSやAPIを用いた解決方法について学んでいただきます。  
このモジュールを通じて学んでいただくこと:

1. 顧客の想定をどのようにソリューションとして落とし込んでゆくか
2. サンプルの作成
3. 3rd パーティモジュール(Turf)の利用
4. GLJSを使ったコーディング
5. Githubなどでコードを共有

## 事前準備
1. テキストエディタの準備
2. 想定されるユースケース(旅程を表示するマップ)を考える

例: Contiki

![User-uploaded image: image.png](https://paper-attachments.dropbox.com/s_3764116D87D7754FD5D048D56D8F607EA3772BC5826DC4F07922B5A58D3327A9_1568823821030_image.png)

![User-uploaded image: image.png](https://paper-attachments.dropbox.com/s_3764116D87D7754FD5D048D56D8F607EA3772BC5826DC4F07922B5A58D3327A9_1568823923384_image.png)


## 1. 必要事項の整理
1. ポイント間に線を引く方法
2. 各都市毎にポイントを配置する方法
3. 選択されているポイントにより、国のハイライトをon/offする方法
4. 各都市の緯度経度
5. 都市にラベルをつける方法
6. カスタムスタイルの導入方法
7. ダイナミックなマップの表示方法

参考: [Style Specification](https://docs.mapbox.com/mapbox-gl-js/style-spec/)

## 2. 課題をソリューションに落とし込む
1. SDKをロード、Mapbox GLJSの最新バージョンを利用
2. マップの初期化を、以下の属性を使って実施
    1. 中心の指定
    2. ズームレベル
    3. Style IDの指定
    4. コンテナの指定
3. サークル
    1. データソースの追加
    2. レイヤの追加
4. 線
    1. データソースの追加
    2. レイヤの追加    
5. ラベル
    1. データソースの追加
    2. レイヤの追加
6. ハイライト
    1. エリアの特定
    2. Expressionを利用したデータ・ドリブンな表示

## 3. サンプルのビルド例
1. サンプルを選ぶ  
- https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
2. 任意のテキストエディタを使って、ソースをコピーして保存。動作確認の実施
3. 以下のプロパティをカスタマイズ
    1. Style:
    2. Center:
    3. Zoom:
    4. Access Token:

4. マップがロードされているかを確認  

    ```
    map.on("load", function() {...});
    ```

5. ソースの追加:

    出発地、経由地、最終地として、三つの都市を指定
    - 以下では、バルセロナ、パリ、フィレンツェを指定
  　
    ```
    map.addSource("itinerary", {
                "type": "geojson",
                "data": {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [2.17694, 41.3825]
                        },
                        "properties": {
                            "type": "origin",
                            "nights": 3,
                            "name": "Barcelona"
                        }
                    }, {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [2.35183, 48.85658]
                        },
                        "properties": {
                            "type": "waypoint",
                            "nights": 5,
                            "name": "Paris"
                        }
                    }, {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [11.25417, 43.77139]
                        },
                        "properties": {
                            "type": "destination",
                            "nights": 2,
                            "name": "Florence"
                        }
                    }]
                }
            });
    ```

6. レイヤの追加
    ```
    map.addLayer({
            "id": "itinerary-stops",
            "type": "circle",
            "source": "itinerary",
            "paint": {
                "circle-radius": 10,
                'circle-color': [
                    'match',
                    ['get', 'type'],
                    'origin', '#F72125',
                    '#000A52'
                ],
                'circle-stroke-width': [
                    'match',
                    ['get', 'type'],
                    'destination', 4,
                    0.5
                ],
                'circle-stroke-color': [
                    'match',
                    ['get', 'type'],
                    'destination', "#F72125",
                    "#000000"
                ]

            }
        });
    ```

7. ラインの設定
    ```
    var route = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [2.17694, 41.3825],
                    [2.35183, 48.85658],
                    [11.25417, 43.77139]
                ]
            }
        }]
    };
    ```

8. 3rdパーティモジュール(Turf)のインポート
    
    曲線を表示をより豊かにするために、3rdパーティーのツールを利用
    
    ```
        <script src='https://npmcdn.com/@turf/turf/turf.min.js' charset='utf-8'></script>
    ```

9. ラインの作成:
    ```
    var line = turf.lineString(route.features[0].geometry.coordinates, { name: 'itinerary' })
                var bezier = turf.bezier(line)
    ```

10. 経路用のソースを追加
    ```
    var routeLineSource = {
                "type": "geojson",
                "data": {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": {
                            "type": "LineString",
                            "coordinates": bezier.geometry.coordinates
                        }
                    }]
                }
            }
    ```

11. 経路のためのレイヤを追加
    ```
    map.addLayer({
        "id": "routeLine",
        "type": "line",
        "source": routeLineSource,
        "paint": {
            "line-width": 1.5,
            "line-color": "#000"
        }
    });
    ```

12. 国のハイライト(イベント+データ・ドリブン)

- 国データの取得

  - 例1: 公開サイトなどから、データをインポートして編集

  　- GeoJSON Maps of the globe
  　https://geojson-maps.ash.ms/
  　*領土も含まれるので注意（フランスの場合、ニューカレドニア、コルシカ島など）*

  - 例2: Mapbox StudioやQGISなどでGeoJSONを作成
  　
    - Polygon(MultiPolygon)としてGeoJSONを作成

- StudioにおけるGeoJSONの編集

　以下のAあるいはBのやり方で、プロパティとして`"country_name": "France"`をもつGeoJSONを作成してみましょう  
　 
  **A. 1つのMultiPolygonとして結合**

  |フランス本土|コルシカ島|結合|
  |-|-|-|
  |<image width=300 src=https://paper-attachments.dropbox.com/s_0992B7314255B9FE8249940C3BDD85DC68A017DD3968E64AB10DAC229577229F_1579404080352_image.png>|<image width=300 src=https://paper-attachments.dropbox.com/s_0992B7314255B9FE8249940C3BDD85DC68A017DD3968E64AB10DAC229577229F_1579404111588_image.png>|<image width=200 src=./assets/combine_polygon.png>|

  GeoJSON

  ```JSON

      {
        "type": "Feature",
        "properties": {
          "country_name": "France"
        },
        "geometry": {
          "coordinates": [
            [
              [...]
            ],
            [
              [...]
            ]
          ],
          "type": "MultiPolygon"
        }
      },
  ```

  *MultiPolygonとせずに、一つのPolygonとしていると、後半の区域が含まれないので注意*

  **B. 別々のPolygonにて、同じpropertiesを持つことで、同じ国として認識させる**

  ```JSON
  {
    "type": "Feature",
    "properties": {
      "country_name": "France"
    },
    "geometry": {
      "coordinates": [
        [
          [3.588184, 50.378992],
          ...
          [3.588184, 50.378992]
        ]
      ],
      "type": "Polygon"
    }
  }
  ```

  ```json
  {
    "type": "Feature",
    "properties": {
      "country_name": "France"
    },
    "geometry": {
      "coordinates": [
        [
          [9.560016, 42.152491],
          ...
          [9.560016, 42.152491]
        ]
      ],
      "type": "Polygon"
    }
  }
  ```

- TilesetとしてExport
    ([補足情報](#補足情報)を確認してください）

- コードの追加

  準備する情報:
  - `YOUR_TILESET_ID` tileset id (例:`tichimura.ck5kgpt2r0dxq2tmn7vl4x0kc-44ac4`)
  - `YOUR_LAYER_NAME` Layer名 例:`francespainitaly`  

  ```javascript
  map.addSource('countries', {
      'type': 'vector',
      'url': 'mapbox://YOUR_TILESET_ID'
  });

  map.addLayer({
      'id': 'country-fills',
      'type': 'fill',
      'source': 'countries',
      'source-layer': 'YOUR_LAYER_NAME',
      'layout': {},
      'paint': {
          'fill-color': '#627BC1',
          'fill-opacity': 0.5
      }
    },
      'itinerary-stops'
  );

  map.addLayer({
      'id': 'country-borders',
      'type': 'line',
      'source': 'countries',
      'source-layer': 'YOUR_LAYER_NAME',
      'layout': {},
      'paint': {
          'line-color': '#627BC1',
          'line-width': 2
      }
    },
    'itinerary-stops'
  );

  ```

  マウスクリックでハイライトをon/offさせる

  ```javascript

  map.on('click', 'itinerary-stops', function(e) {
      if (e.features.length > 0) {

          map.setFilter('country-fills', [
              'in',
              'country_name',
              e.features[0].properties.country_name
          ]);
      }
  });

  ```

- 最終イメージ

  <image width=200 src=https://paper-attachments.dropbox.com/s_0992B7314255B9FE8249940C3BDD85DC68A017DD3968E64AB10DAC229577229F_1579404318434_image.png>

- イタリア、スペインについてもやってみましょう

　参考: 

## 4. やってみよう

13. 都市のラベルを表示する　(イベント・ドリブン)

## 5. お疲れ様でした!

実際に動かしたものを、他のメンバーと共有しましょう
（チャットウィンドウ or ワークシート)

# 補足情報

Mapbox Studioで、datasetからtileset を作成すると、Zoom extentが以下のようになっている

Studio > Tileset > Details

```text
Zoom extent
z0 ~ z6
Data will be visible above zoom 6, but may appear simplified. Learn how to adjust zoom extent
```
https://docs.mapbox.com/help/troubleshooting/adjust-tileset-zoom-extent/

Zoomレベルで、うまく表示されない場合は、以下のいずれかで設定変更が可能

### Tippecanoeを使ってアップロード

*注: Windowsはサポート外です*

こちらを参照
Transform data with Tippecanoe
https://docs.mapbox.com/help/troubleshooting/adjust-tileset-zoom-extent/#transform-data-with-tippecanoe

### Tileset recipe を使ってアップロード

*注: pythonの環境が必要です*

tileset cliを利用
https://github.com/mapbox/tilesets-cli/blob/master/README.md#update-recipe

  - sourceのアップロード
  
  `tilesets add-source tichimura day5-source ./day5/francespainitaly.json`

  - sourceのリスト
  
  `tilesets list-sources tichimura`

  - sourceの確認
  
  `tilesets view-source tichimura day5-source`

  - tilesetの確認
  
  `tilesets status tichimura.day5tileset`

  - tilesetの作成
  
  `tilesets create tichimura.day5tileset --recipe ./day5/recipe.json --name "Day5 tileset"`
    
  - tilesetのpublish
  
  `tilesets publish tichimura.day5tileset`

　- 参考: recipe.jsonの例

```json
{
  "version": 1,
  "layers": {
    "francespainitaly": {
        "source": "mapbox://tileset-source/tichimura/day5-source",
      "minzoom": 0,
      "maxzoom": 12
    }
  }
}  
```


----------
