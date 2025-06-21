# SWS Chatbot Context Repo

Questo repository genera ogni notte il file `context/sws_context.txt` con i testi puliti di **https://www.sitowebsicuro.com/it/** usando [Crawl4AI](https://github.com/unclecode/crawl4ai).

Il file viene usato dal plugin WordPress **sws-chatbot** per rispondere alle domande degli utenti.

## Come funziona
1. Il workflow GitHub Actions (`.github/workflows/crawl.yml`) gira ogni giorno alle 02:00 UTC.
2. Installa Crawl4AI, esegue `generate_context.py`, aggiorna il file.
3. Se il file cambia, effettua commit automatico.

## Uso nel plugin
Sul server WordPress, carica (o aggiorna) `sws_context.txt` in:
```
wp-content/plugins/sws-chatbot/data/sws_context.txt
```
Il plugin lo leggerà automaticamente come contesto preferenziale.

Puoi anche premere il pulsante "Inizia scansione" dentro l'admin del plugin per rigenerare localmente se lo desideri. 