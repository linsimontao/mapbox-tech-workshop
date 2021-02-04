# Mapbox Tech Workshop 2 - Store Map in Code with Animation

## はじめに

Mapbox GL JSを使ったコーディングと、SDKやAPIの利用について学びます。本モジュールにおいては、store locator web アプリケーションの基本的な部分を実装します。
本モジュールを終了することで、

1. GLJSのExampleを探して、どのように組み合わせるかを理解する
2. インタラクティブなマップの構築
3. マップにアニメーションを追加

といった内容が、カバーされることになります。

## 事前準備
1. テキストエディタ ( [SublimeText](https://www.sublimetext.com/)など)
2. ブラウザ ( [Google Chrome](https://www.google.com/chrome/) を推奨)

## テキストエディタにて
1. 新規ファイルを作成
1. 以下のコードを入力して下さい。（なるべくタイプしましょう。今回実施しない場合でも、以降のワークショップではタイプして下さい! )
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8' />
        <title>Display starbucks in US</title>
        <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v2.0.1/mapbox-gl.js'></script>
        <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v2.0.1/mapbox-gl.css' rel='stylesheet' />
        <style>
        body {
            margin: 0;
            padding: 0;
        }

        #map {
            position: absolute;
            top: 0;
            bottom: 0;
            width: 100%;
        }
        </style>
    </head>
    ```

1. BodyとDivタグを追加しましょう（タイプしましょう 🙂 )
    ```
    <body>
        <div id='map'></div>
        <script>
    ```

1. マップの初期化を実装します (タイプしましょうね 🙂 )
      - `YOUR TOKEN HERE` ご自身のTokenを入力してください。
      - ` YOUR MAP STYLE HERE` 前回作成したStyleを入力してください。(mapbox://)
    ```
        mapboxgl.accessToken = YOUR_TOKEN_HERE;
            var map = new mapboxgl.Map({
                style: YOUR_MAP_STYLE_HERE,
                center: [-74.0066, 40.7135],
                zoom: 15.5,
                pitch: 45,
                bearing: -17.6,
                container: 'map'
            });
    ```

1. コードの内容を確認して、以下を追加して、ブラウザからアクセスしてみましょう。
    ```
            </script>
        </body>
        </html>
    ```
    実行が確認できたら、上記の追加した3行を削除して次に進みましょう。

1. クリック機能を追加しましょう

    `starbucks-us-locations-test`の部分は前回追加したLayer名(LayerID)になります。
    Layer名がMapbox Studioと一致しているか再度確認しましょう。

    ```
    map.on('click', 'starbucks-us-locations-test', function(e) {
                const clickedCoordinates = e.features[0].geometry.coordinates
                map.flyTo({ center: clickedCoordinates });
                
                new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML(e.features[0].properties.name)
                .addTo(map);
            });
    ```
1. DrawされたLayerに対して、mouseenter/mouseleaveのeventを追加しましょう。
    ```
    // Change the cursor to a pointer when the it enters a feature in the 'symbols' layer.
    map.on('mouseenter', 'starbucks-us-locations-poly', function () {
            map.getCanvas().style.cursor = 'pointer';
        });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', 'starbucks-us-locations-poly', function () {
        map.getCanvas().style.cursor = '';
    });
    ```

1. コードの内容を確認して、以下を追加して、ブラウザからアクセスしてみましょう。
    ```
            </script>
        </body>
        </html>
    ```

## 主なコンセプトとポイント

- Fly To
- On Load
- On Click
- Mouse Enter
- Mouse Leave

## 追加の質問

- `bearing`とは
- `container`とは

https://docs.mapbox.com/help/glossary/
