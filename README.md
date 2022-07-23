# Kefmong web analyzer

Cílem je vytvořit aplikaci, která bude sbírat interakce uživatelů na webu a
ukládat je do Mongo databáze. Interakce je informace o tom, který uživatel, kdy
a odkud otevřel webovou stránku.

Aplikace bude sestávat ze dvou komponent které poběží jako samostatné Docker
kontejnery a budou spolu komunikovat skrz Apache Kafka.

- První komponenta bude poskytovat REST API na které bude moci uživatel API
  (webová stránka) poslat request s informací, že došlo k interakci.
  Komponenta pak v zprávu v Kafce.
- Druhá komponenta bude číst Kafku a na základě zpráv z ní vytvoří
  záznamy v Mongu.

Aplikace by měla být nějak jednoduše spustitelná – např. pomocí Docker Compose
který všechny potřebné kontejnery nastartuje.

API navrhněte, jak uznáte za vhodné. Mělo by to být REST API ale ostatní
detaily jsou na vás.

Příklad použití – návštěvník otevře webovou stránku a stránka pomocí JS odešle
na toto API informaci o IP adrese a webové adrese. Web samozřejmě implementovat
nemusíte, stačí přiložit nějaký příklad, jak mohu API zavolat
