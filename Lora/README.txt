・実行環境
Python2.7.2

・ライブラリ
pyaudio
pyserial
（予めportaudioとserialのインストールが必要）

・出力ファイル
binaryfile.bin, decodedraefile.raw, rawfile.raw, rcvfile.bin は一時的な受け渡しファイルなので削除して構わない．

・SERIALPORT：TX.pyの18行目，RX.pyの16行目
ES920LRの接続されたUSBポートを指定．
windowsならCOM1とか．debian系なら/dev/ttyUSB0とかになる．
ES920LRのテストボード上のシリアル変換チップFT232のドライバについてはCDROMを参照のこと．

・実行の仕方
ES920LRのテストボードのRESETボタンを押してから実行したほうが安全．
RX.py→TX.pyの順に実行．