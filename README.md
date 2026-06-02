# Sprawozdanie - Zadanie 2

1. Tagowanie: Obraz aplikacji jest budowany i wypychany bezpośrednio do rejestru GitHub Container Registry (`ghcr.io`) pod tagiem `:latest`.
2. Cache: Zgodnie z wymaganiami, dane cache (w trybie `max`) są przesyłane i przechowywane w dedykowanym, zewnętrznym repozytorium na moim profilu DockerHub. Przyspiesza to kolejne uruchomienia potoku.
3. Skanowanie CVE: Po zbudowaniu i wypchnięciu obrazu, wewnątrz potoku uruchamiane jest narzędzie Trivy, które skanuje obraz pod kątem podatności o statusie HIGH oraz CRITICAL.