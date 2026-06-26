import os
import subprocess
import sys

def main():
    tex_file = "spiegami.tex"
    pdf_file = "spiegami.pdf"
    
    if not os.path.exists(tex_file):
        print(f"Errore: il file {tex_file} non esiste.")
        sys.exit(1)
        
    print(f"Avvio compilazione di {tex_file} con pdflatex...")
    
    # Eseguiamo pdflatex due volte per risolvere correttamente i riferimenti incrociati e i posizionamenti dei box/figure.
    for i in range(2):
        print(f"Passaggio {i+1} di 2...")
        try:
            # -interaction=nonstopmode evita che LaTeX si blocchi a chiedere input in caso di errori minori.
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", tex_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            print(f"Passaggio {i+1} completato con successo.")
        except subprocess.CalledProcessError as e:
            print(f"Errore durante la compilazione al passaggio {i+1}:")
            print(e.stdout)
            print(e.stderr)
            sys.exit(e.returncode)
            
    # Verifica che il PDF sia stato creato
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
        print(f"\nPDF generato con successo: {pdf_file} ({os.path.getsize(pdf_file)} byte)")
        
        # Pulizia dei file temporanei generati da LaTeX
        temp_extensions = [".aux", ".log", ".out", ".toc"]
        base_name = os.path.splitext(tex_file)[0]
        cleaned_files = []
        
        for ext in temp_extensions:
            temp_file = base_name + ext
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                    cleaned_files.append(temp_file)
                except Exception as ex:
                    print(f"Avviso: non è stato possibile rimuovere {temp_file}: {ex}")
                    
        if cleaned_files:
            print(f"File temporanei rimossi: {', '.join(cleaned_files)}")
            
        sys.exit(0)
    else:
        print("\nErrore: Il file PDF non è stato generato o ha dimensione zero.")
        sys.exit(1)

if __name__ == "__main__":
    main()
