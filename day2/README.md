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
        <title>Display buildings in 3D</title>
        <meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no' />
        <script src='https://api.tiles.mapbox.com/mapbox-gl-js/v2.0.0/mapbox-gl.js'></script>
        <script src='src/my.js'></script>
        <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v2.0.0/mapbox-gl.css' rel='stylesheet' />
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
                container: 'map',
                antialias: true
            });
    ```

1. コードの内容を確認して、以下を追加して、ブラウザからアクセスしてみましょう。
    ```
            </script>
        </body>
        </html>
    ```
    実行が確認できたら、上記の追加した3行を削除して次に進みましょう。

1. 次のコードをペーストしましょう。
    ```
        var size = 200;
        var clickedCoordinates = [0, 0];

        var pulsingDot = {
            width: size,
            height: size,
            data: new Uint8Array(size * size * 4),

            onAdd: function() {
                var canvas = document.createElement('canvas');
                canvas.width = this.width;
                canvas.height = this.height;
                this.context = canvas.getContext('2d');
            },

            render: function() {
                var duration = 1000;
                var t = (performance.now() % duration) / duration;

                var radius = size / 2 * 0.3;
                var outerRadius = size / 2 * 0.7 * t + radius;
                var context = this.context;

                // draw outer circle
                context.clearRect(0, 0, this.width, this.height);
                context.beginPath();
                context.arc(this.width / 2, this.height / 2, outerRadius, 0, Math.PI * 2);
                context.fillStyle = 'rgba(255, 200, 200,' + (1 - t) + ')';
                context.fill();

                // draw inner circle
                context.beginPath();
                context.arc(this.width / 2, this.height / 2, radius, 0, Math.PI * 2);
                context.fillStyle = 'rgba(255, 100, 100, 1)';
                context.strokeStyle = 'white';
                context.lineWidth = 2 + 4 * (1 - t);
                context.fill();
                context.stroke();

                // update this image's data with data from the canvas
                this.data = context.getImageData(0, 0, this.width, this.height).data;

                // keep the map repainting
                map.triggerRepaint();

                // return `true` to let the map know that the image was updated
                return true;
            }
        };
    ```

1. マップがロードされた時にレイヤも追加しましょう:
    ```
    map.on('load', function() {
            // Insert the layer beneath any symbol layer.
            var layers = map.getStyle().layers;

            var labelLayerId;
            for (var i = 0; i < layers.length; i++) {
                if (layers[i].type === 'symbol' && layers[i].layout['text-field']) {
                    labelLayerId = layers[i].id;
                    break;
                }
            }

            map.addLayer({
                'id': '3d-buildings',
                'source': 'composite',
                'source-layer': 'building',
                'filter': ['==', 'extrude', 'true'],
                'type': 'fill-extrusion',
                'minzoom': 15,
                'paint': {
                    'fill-extrusion-color': '#aaa',

                    // use an 'interpolate' expression to add a smooth transition effect to the
                    // buildings as the user zooms in
                    'fill-extrusion-height': [
                        "interpolate", ["linear"],
                        ["zoom"],
                        15, 0,
                        15.05, ["get", "height"]
                    ],
                    'fill-extrusion-base': [
                        "interpolate", ["linear"],
                        ["zoom"],
                        15, 0,
                        15.05, ["get", "min_height"]
                    ],
                    'fill-extrusion-opacity': .6
                }
            }, labelLayerId);
          });
    ```

1. クリック機能を追加しましょう

    `starbucks-us-locations-test`の部分は前回追加したLayer名(LayerID)になります。

    ```
    map.on('click', 'starbucks-us-locations-test', function(e) {
                clickedCoordinates = e.features[0].geometry.coordinates
                map.flyTo({ center: clickedCoordinates });
                map.addImage('pulsing-dot', pulsingDot, { pixelRatio: 2 });

                map.addLayer({
                    "id": "points",
                    "type": "symbol",
                    "source": {
                        "type": "geojson",
                        "data": {
                            "type": "FeatureCollection",
                            "features": [{
                                "type": "Feature",
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": clickedCoordinates
                                }
                            }]
                        }
                    },
                    "layout": {
                        "icon-image": "pulsing-dot"
                    }
                });

            });
    ```

1. インタラクティブな要素を追加しましょう (タイプしましょう 🙂 )
   `starbucks-us-locations-test`の部分は前回追加したLayer名(LayerID)になります。

    ```
    map.on('click', 'landcover', function(e) {
                map.removeLayer('points')
                map.removeSource('points')
                map.removeImage('pulsing-dot')
                console.log("landcover")
            })

            // Change the cursor to a pointer when the it enters a feature in the 'symbols' layer.
            map.on('mouseenter', 'starbucks-us-locations-test', function() {
                map.getCanvas().style.cursor = 'pointer';
            });

            // Change it back to a pointer when it leaves.
            map.on('mouseleave', 'starbucks-us-locations-test', function() {
                map.getCanvas().style.cursor = '';
            });
    ```

1. コードの内容を確認して、以下を追加して、ブラウザからアクセスしてみましょう。
    ```
            </script>
        </body>
        </html>
    ```

1. 地図のスクリーンショットをとって下さい。
1. チャットウィンドウ、あるいはGoogle Docに共有して下さい！


## 主なコンセプトとポイント

- Fly To
- On Load
- On Click
- Add a Layer
- Remove a Layer
- Mouse Enter
- Mouse Leave

## 追加の質問

- `bearing`とは
- `container`とは
- `antialias`とは

https://docs.mapbox.com/help/glossary/
