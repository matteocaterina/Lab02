import csv
from csv import reader


def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    Biblioteca = []
    try:
        infile = open(file_path, "r")
        infile.readline()
        csvReader = reader(infile)
        for record in csvReader:
            dizionario = {}
            dizionario['Titolo'] = record[0]
            dizionario['Autore'] = record[1]
            dizionario['Anno'] = record[2]
            dizionario['Pagine'] = int(record[3])
            dizionario['Sezione'] = int(record[4])
            Biblioteca.append(dizionario)
        infile.close()
        return Biblioteca
    except FileNotFoundError:
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    for libro in biblioteca:
        if libro["Titolo"] == titolo:
            return None
    else:
        pass
    if sezione not in range(1, 6):
        return None
    else:
        pass

    file = file_path

    outfile = open(file, "a")

    writer = csv.writer(outfile)

    writer.writerow([titolo, autore, anno, pagine, sezione])

    outfile.close()

    return {"Titolo": titolo, "Autore": autore, "Anno": anno, "Pagine": pagine, "Sezione": sezione}




def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO

    for libro in biblioteca:
        if libro['Titolo'] == titolo or libro['Titolo'].upper() == titolo.upper() or libro['Titolo'].lower() == titolo.lower():
            return f"{libro['Titolo']}, {libro['Autore']}, {libro['Anno']}, {libro['Pagine']}, {libro['Sezione']}"
    return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if sezione not in range(1, 6):
        print("Valore non presente")

        return None

    lista_libri = []

    for libro in biblioteca:
        if libro['Sezione'] == sezione:
            lista_libri.append(libro['Titolo'])

    lista_libri.sort()
    return lista_libri


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            biblioteca = carica_da_file(file_path)
            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
